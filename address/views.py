from flask_jwt_extended import jwt_required
from flask_smorest import Blueprint, abort
from sqlalchemy.exc import SQLAlchemyError

from address.models import Address
from address.schema import AddressSchema, AddressUpdateSchema
from db import db

blp = Blueprint('address', __name__)


@blp.route('/address/create', methods=['POST'])
@blp.arguments(AddressSchema)
@blp.response(200, AddressSchema)
@jwt_required()
def create_addresses(address_data):
    address = Address(**address_data)

    try:
        db.session.add(address)
        db.session.commit()
    except SQLAlchemyError:
        abort(500, message='Error While Inserting data')

    return address


@blp.route('/address/detail/<string:id>', methods=['GET'])
@blp.response(200, AddressSchema)
@jwt_required()
def get_location_detail(id):
    address = Address.query.get_or_404(id)
    return address


@blp.route('/address/edit/<string:id>', methods=['PUT'])
@blp.arguments(AddressUpdateSchema)
@blp.response(200, AddressSchema)
@jwt_required()
def edit_location(address_data, id):
    address = Address.query.get_or_404(id)
    if address:
        address.country = address_data['country']
        address.city = address_data['city']
        address.street_address = address_data['street_address']
        address.zip_code = address_data['zip_code']
    else:
        address = Address(id=id, **address_data)
    db.session.add(address)
    db.session.commit()
    return address


@blp.route('/address/delete/<string:id>', methods=['DELETE'])
@blp.response(200, AddressSchema)
@jwt_required()
def delete_location(id):
    address = Address.query.get_or_404(id)
    db.session.delete(address)
    db.session.commit()
    return {"message", "Address Deleted Successfully"}


@blp.route('/address/all', methods=['GET'])
@blp.response(200, AddressSchema(many=True))
@jwt_required()
def get_all_addresses():
    return Address.query.all()
