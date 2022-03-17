# Import flask dependencies
from flask import Blueprint, request, render_template, jsonify, flash, abort
from sqlalchemy import desc
import time
from apps.user.models import User
from apps import db

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/', methods=['GET', 'POST'])
def senarai_user():
    data = {}
    if request.method == 'POST':
        request_data = request.get_json()
        name = request_data['name']
        no_ic = request_data['no_ic']
        no_telefon = request_data['no_telefon']
        alamat = request_data['alamat']
        poskod = request_data['poskod']
        bandar = request_data['bandar']
        negeri = request_data['negeri']
        email = request_data['email']
        password = request_data['password']
        user = User(name, no_ic, no_telefon, alamat, poskod, bandar, 
        negeri, email, password)
        db.session.add(user)
        db.session.commit()        
    else:
        list_ = []
        senarai_user = User.query.all()
        for user in senarai_user:
            list_.append(user)        
        return jsonify(data)

@user_bp.route('/<int:id>', methods=['GET', 'PUT'])
def satu_user(id):
    if request.method == 'PUT':
        user = User.query.get(id)
        request_data = request.get_json()
        user.name = request_data['name']
        user.no_ic = request_data['no_ic']
        user.no_telefon = request_data['no_telefon']
        user.alamat = request_data['alamat']
        user.poskod = request_data['poskod']
        user.bandar = request_data['bandar']
        user.negeri = request_data['negeri']
        user.email = request_data['email']
        user.password = request_data['password']  
        db.session.commit()                         
    else:
        user = User.query.filter_by(id=id).first()
        return jsonify(user)      