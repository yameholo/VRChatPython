from requests.auth import HTTPBasicAuth
from vrchat.binder import bind_api
from vrchat.models import World, Instance


class API:
    def __init__(self, auth, api_key="", host="api.vrchat.cloud", api_root='/api/1',):
        self.auth = auth
        self.apiKey = api_key
        self.host = host
        self.api_root = api_root

    def set_api_key(self, api_key):
        self.apiKey = api_key

    @property
    def get_world(self):
        return bind_api(
            api=self,
            path="/worlds/{id}",
            method="GET",
            model=World,
            allowed_param=["id"],
            require_auth=True
        )

    @property
    def get_instance(self):
        return bind_api(
            api=self,
            path="/worlds/{id}/{instanceId}",
            method="GET",
            model=Instance,
            allowed_param=["id", "instanceId"],
            require_auth=True
        )

    @property
    def list_worlds(self):
        return bind_api(
            api=self,
            path="/worlds",
            method="GET",
            model=World,
            allowed_param=["featured", "sort", "user", "userId", "n", "order", "offset", "search", "tag", "notag",
                           "releaseStatus", "maxUnityVersion", "minUnityVersion", "maxAssetVersion", "minAssetVersion",
                           "platform"],
            require_auth=True
        )

    @property
    def list_active_worlds(self):
        return bind_api(
            api=self,
            path="/worlds/active",
            method="GET",
            model=World,
            allowed_param=["featured", "sort", "user", "userId", "n", "order", "offset", "search", "tag", "notag",
                           "releaseStatus", "maxUnityVersion", "minUnityVersion", "maxAssetVersion", "minAssetVersion",
                           "platform"],
            require_auth=True
        )

    @property
    def list_recent_worlds(self):
        return bind_api(
            api=self,
            path="/worlds/recent",
            method="GET",
            model=World,
            allowed_param=["featured", "sort", "user", "userId", "n", "order", "offset", "search", "tag", "notag",
                           "releaseStatus", "maxUnityVersion", "minUnityVersion", "maxAssetVersion", "minAssetVersion",
                           "platform"],
            require_auth=True
        )

    @property
    def list_favorites_worlds(self):
        return bind_api(
            api=self,
            path="/worlds/favorites",
            method="GET",
            model=World,
            allowed_param=["featured", "sort", "user", "userId", "n", "order", "offset", "search", "tag", "notag",
                           "releaseStatus", "maxUnityVersion", "minUnityVersion", "maxAssetVersion", "minAssetVersion",
                           "platform"],
            require_auth=True
        )


if __name__ == '__main__':
    auth = HTTPBasicAuth(username="", password="")
    api = API(auth=auth, api_key="")
    # world = api.get_world(
    #     id="wrld_b2d24c29-1ded-4990-a90d-dd6dcc440300"
    # )
    # print("name:", world.name)
    # print("description:", world.description)
    # print(world.instances)
    #
    # for ins in world.instances:
    #     instance = api.get_instance(
    #         id="wrld_b2d24c29-1ded-4990-a90d-dd6dcc440300",
    #         instanceId=ins["instanceId"]
    #     )
    api.list_worlds()
