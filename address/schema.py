from marshmallow import Schema, fields


class AddressSchema(Schema):
    id = fields.Str(dump_only=True)
    country = fields.Str(required=True)
    city = fields.Str(required=True)
    street_address = fields.Str(required=True)
    zip_code = fields.Int(required=True)


class AddressUpdateSchema(Schema):
    country = fields.Str(required=True)
    city = fields.Str(required=True)
    street_address = fields.Str(required=True)
    zip_code = fields.Int(required=True)
