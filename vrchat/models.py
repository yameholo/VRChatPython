from datetime import datetime


class Model(object):

    @classmethod
    def parse(cls, _json):
        raise NotImplementedError


class Config(Model):

    @classmethod
    def parse(cls, _json):
        config = cls()
        for k, v in _json.items():
            setattr(config, k, v)
        return config


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


class Friend(User):

    # ToDo
    # def unfriend(self):
    #     api.unfriend(id=self.id)
    pass


class AnyUser(User):

    # ToDo
    # def send_friend_request(self):
    #     api.friend_request(id=self.id)
    pass


class FriendStatus(Model):

    @classmethod
    def parse(cls, _json):
        status = cls()
        for k, v in _json.items():
            setattr(status, k, v)
        return status


class Notification(Model):

    @classmethod
    def parse(cls, _json):
        notification = cls()
        for k, v in _json.items():
            setattr(notification, k, v)
        return notification


class Favorite(Model):

    @classmethod
    def parse(cls, _json):
        favorite = cls()
        for k, v in _json.items():
            if k == "type":
                if v == "world":
                    setattr(favorite, k, World())
                elif v == "friend":
                    setattr(favorite, k, Friend())
                # ToDo: Add Avatar model
                # elif v == "avatar":
                #     setattr(favorite, k, Avatar())
                continue
            setattr(favorite, k, v)
        return favorite
