from requests.auth import HTTPBasicAuth
from vrchat.binder import bind_api


class API:
    def __init__(self, username, password, host="api.vrchat.cloud", api_root='/api/1',):
        self.username = username
        self.password = password
        self.auth = HTTPBasicAuth(username, password)
        self.host = host
        self.api_root = api_root

    @property
    def get_world_by_id(self):
        return bind_api(
            api=self,
            path="/worlds/{id}",
            allowed_param=["id", "apiKey"]
        )


if __name__ == '__main__':
    api = API(username="test", password="test")
    test_res = api.get_world_by_id(
        id="wrld_5d42e834-24ac-4101-90d1-eaa7138f4399",
        apiKey=""
    )
    print(test_res.text)
