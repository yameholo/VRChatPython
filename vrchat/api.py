from requests.auth import HTTPBasicAuth
from vrchat.binder import bind_api
from vrchat.models import World, Instance, User, Player, FriendStatus, Config


class API:
    def __init__(self, auth, api_key="", host="api.vrchat.cloud", api_root='/api/1',):
        self.auth = auth
        self.apiKey = api_key
        self.host = host
        self.api_root = api_root
        self.config = None

    def set_api_key(self):
        if self.config is None:
            self.config = api.remote_config()
        self.apiKey = self.config.apiKey

    @property
    def remote_config(self):
        return bind_api(
            api=self,
            path="/config",
            method="GET",
            model=Config,
            allowed_param=[],
            require_auth=False
        )

    @property
    def me(self):
        return bind_api(
            api=self,
            path="/auth/user",
            model=Player,
            method="GET",
            allowed_param=[],
            require_auth=True
        )

    @property
    def list_friends(self):
        return bind_api(
            api=self,
            path="/auth/user/friends",
            model=User,
            method="GET",
            allowed_param=["offset", "n", "offline"],
            require_auth=True
        )

    @property
    def friend_status(self):
        return bind_api(
            api=self,
            path="/user/{id}/friendStatus",
            model=FriendStatus,
            method="GET",
            allowed_param=["id"],
            require_auth=True
        )

    # ToDo: Notification
    # @property
    # def friend_request(self):
    #     return bind_api(
    #         api=self,
    #         path="/user/{id}/friendRequest",
    #         model=Notification,
    #         method="POST",
    #         allowed_param=["id"],
    #         require_auth=True
    #     )

    # ToDo
    # @property
    # def unfriend(self):
    #     return bind_api(
    #         api=self,
    #         path="/auth/user/friends/{id}",
    #         model=Success_or_Error,
    #         method="DELETE",
    #         allowed_param=["id"],
    #         require_auth=True
    #     )

    @property
    def get_user_by_id(self):
        return bind_api(
            api=self,
            path="/users/{id}",
            model=User,
            method="GET",
            allowed_param=["id"],
            require_auth=True
        )

    @property
    def get_user_by_name(self):
        return bind_api(
            api=self,
            path="/users/{username}/name",
            model=User,
            method="GET",
            allowed_param=["username"],
            require_auth=True
        )

    @property
    def list_any_users(self):
        return bind_api(
            api=self,
            path="/users",
            model=User,
            method="GET",
            allowed_param=["search", "developerType", "n", "offset"],
            require_auth=True
        )

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

    # ToDo: World Meta
    # @property
    # def get_world_meta(self):
    #     return bind_api(
    #         api=self,
    #         path="/worlds/{id}/metadata",
    #         method="GET",
    #         model=WorldMeta,
    #         allowed_param=["id"],
    #         require_auth=True
    #     )

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


if __name__ == '__main__':
    import sys
    username, password, api_key = sys.argv[1:]
    auth = HTTPBasicAuth(username=username, password=password)
    api = API(auth=auth)
    api.set_api_key()
    api.me()
    api.list_friends(offline=True)
    api.friend_status(id="usr_43765314-b18b-407e-ba6b-56113c5d06f1")
    # api.get_user_by_id(id="usr_0d939cc4-e92d-43e8-a060-799d185715b9")
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
    # api.list_worlds()
