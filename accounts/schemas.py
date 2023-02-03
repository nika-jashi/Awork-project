from marshmallow import Schema, fields


class AccountSchema(Schema):
    id = fields.Int(dump_only=True)
    email = fields.Str(required=True)
    first_name = fields.Str(required=True)
    last_name = fields.Str(required=True)
    password = fields.Str(load_only=True)


class AccountLoginSchema(Schema):
    email = fields.Str(required=True)
    password = fields.Str(load_only=True)
