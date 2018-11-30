from marshmallow import Schema, fields,post_load


class DTORegisteredMerchantsRequest():
    def __init__(self, AppId, Key, Name):
        self.AppId = AppId
        self.Key = Key
        self.Name = Name

    def __repr__(self):
        return '<DTORegisteredMerchantsRequest(appid={self.AppId!r})>'.format(self=self)


class DTORegisteredMerchantsRequestSchema(Schema):
    AppId = fields.Str()
    Key = fields.Str()
    Name = fields.Str()

    @post_load
    def make_user(self, data):
        return DTORegisteredMerchantsRequest(**data)