import requests
import re
import json


re_path_template = re.compile('{\w+}')


def bind_api(api, path, method="GET", allowed_param=None, model=None, require_auth=False):

    def _call(**kwargs):
        if len(kwargs) == 0:
            if require_auth:
                params = {}
            else:
                params = None
        elif allowed_param:
            params = {k: v for k, v in kwargs.items() if k in allowed_param}
        else:
            params = kwargs

        if require_auth:
            params["apiKey"] = api.apiKey

        _path = path
        for variable in re_path_template.findall(path):
            _name = variable.strip("{}")
            value = kwargs[_name]

            del params[_name]
            _path = path.replace(variable, value)

        _url = "https://%s%s%s" % (api.host, api.api_root, _path)

        result = requests.request(method, _url, params=params, auth=api.auth)

        if model is None:
            return result

        print(result.text)

        _data = json.loads(result.text)
        if isinstance(_data, list):
            return [model.parse(v) for v in _data]

        return model.parse(_data)

    return _call
