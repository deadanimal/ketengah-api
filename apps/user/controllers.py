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

    list_ = []
    senarai_user = User.query.all()
    for user in senarai_user:
        satu_user = {
            'name': user.name,
            'no_ic': user.no_ic,
            'no_telefon': user.no_telefon,
            'alamat': user.alamat,
            'poskod': user.poskod,
            'bandar': user.bandar,
            'negeri': user.negeri,
            'email': user.email,
            'password': user.password
        }
        list_.append(satu_user)
    return jsonify(list_)

@user_bp.route('/<int:id>', methods=['GET', 'PUT'])
def satu_user(id):
    user = db.session.query(User).filter_by(id=id).first()

    if request.method == 'PUT':        
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

    satu_user = {
        'name': user.name,
        'no_ic': user.no_ic,
        'no_telefon': user.no_telefon,
        'alamat': user.alamat,
        'poskod': user.poskod,
        'bandar': user.bandar,
        'negeri': user.negeri,
        'email': user.email,
        'password': user.password
    }       
    return jsonify(satu_user)      