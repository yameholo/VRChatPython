import requests
import re


re_path_template = re.compile('{\w+}')


def bind_api(api, path, allowed_param=None, method='GET'):

    def _call(**kwargs):
        if len(kwargs) == 0:
            params = None
        elif allowed_param:
            params = {k: v for k, v in kwargs.items() if k in allowed_param}
        else:
            params = kwargs

        _path = path
        for variable in re_path_template.findall(path):
            _name = variable.strip("{}")
            value = kwargs[_name]

            del params[_name]
            _path = path.replace(variable, value)

        _url = "https://%s%s%s" % (api.host, api.api_root, _path)
        result = requests.get(_url, params=params)

        return result

    return _call
