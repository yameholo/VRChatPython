from datetime import datetime


class Model(object):

    @classmethod
    def parse(cls, _json):
        raise NotImplementedError


class World(Model):

    @classmethod
    def parse(cls, _json):
        world = cls()
        for k, v in _json.items():
            if k == "instances":
                setattr(world, k, [{"instanceId": _id, "people": c} for _id, c in v])
            else:
                setattr(world, k, v)
        return world


class Instance(Model):

    @classmethod
    def parse(cls, _json):
        instance = cls()
        for k, v in _json.items():
            setattr(instance, k, v)
        return instance


class User(Model):

    @classmethod
    def parse(cls, _json):
        user = cls()
        for k, v in _json.items():
            if k == "last_login":
                setattr(user, k, datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%fZ"))
                continue
            elif k == "location":
                if ":" in v:
                    wid, iid = v.split(":")
                    setattr(user, k, {"isOnline": True, "world_id": wid, "instance_id": iid})
                else:
                    setattr(user, k, {"isOnline": False, "value": v})
                continue
            setattr(user, k, v)
        return user


class Player(User):
    pass


class FriendStatus(Model):

    @classmethod
    def parse(cls, _json):
        status = cls()
        for k, v in _json.items():
            setattr(status, k, v)
        return status
