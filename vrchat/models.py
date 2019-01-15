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
