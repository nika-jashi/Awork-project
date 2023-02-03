from flask_smorest import Blueprint, abort
from flask_jwt_extended import (
    create_access_token,
    create_refresh_token,
    get_jwt_identity,
    jwt_required, )
from passlib.hash import pbkdf2_sha256
from sqlalchemy.exc import SQLAlchemyError

from db import db
from accounts.models import Account
from accounts.schemas import AccountSchema, AccountLoginSchema

blp = Blueprint("Accounts", __name__)


@blp.route("/register", methods=['POST'])
@blp.arguments(AccountSchema)
def account_registration(account_data):
    if Account.find_by_email(account_data["email"]):
        abort(400, message="Account With This Email Is Already Registered.")

    account = Account(
        email=account_data["email"],
        first_name=account_data["first_name"],
        last_name=account_data["last_name"],
        password=pbkdf2_sha256.hash(account_data["password"]),
    )
    try:
        db.session.add(account)
        db.session.commit()
    except SQLAlchemyError:
        abort(500, message='Error While Inserting data')

    return {"message": "Account created successfully."}, 201


@blp.route("/login", methods=['POST'])
@blp.arguments(AccountLoginSchema)
def account_login(account_data):
    account = Account.find_by_email(account_data["email"])

    if account and pbkdf2_sha256.verify(account_data["password"], account.password):
        access_token = create_access_token(identity=account.id, fresh=True)
        refresh_token = create_refresh_token(account.id)
        return {"access_token": access_token, "refresh_token": refresh_token}, 200

    abort(401, message="Invalid credentials.")


@blp.route("/refresh", methods=['POST'])
@jwt_required(refresh=True)
@jwt_required()
def token_refresh():
    current_account = get_jwt_identity()
    new_token = create_access_token(identity=current_account, fresh=False)
    return {"access_token": new_token}, 200
