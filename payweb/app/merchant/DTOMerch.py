from marshmallow import Schema, fields, post_load


class DTORegisteredMerchantsRequest():
    def __init__(self, AppId=None, Key=None, Name=None, MchID=None):
        self.AppId = AppId
        self.Key = Key
        self.Name = Name
        self.MchID = MchID

    def __repr__(self):
        return '<DTORegisteredMerchantsRequest(appid={self.AppId!r})>'.format(self=self)


class DTORegisteredMerchantsRequestSchema(Schema):
    AppId = fields.Str()
    Key = fields.Str()
    Name = fields.Str()
    MchID = fields.Str()

    @post_load
    def make_user(self, data):
        return DTORegisteredMerchantsRequest(**data)
