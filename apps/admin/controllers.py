# Import flask dependencies
from flask import Blueprint, request, render_template, jsonify, flash, abort
from sqlalchemy import desc
import time
from apps.admin.models import Admin
from apps import db

admin_bp = Blueprint('admin', __name__, url_prefix='/admin')


@admin_bp.route('/', methods=['GET', 'POST'])
def senarai_admin():
    data = {}
    if request.method == 'POST':
        request_data = request.get_json()
        nama = request_data['nama']
        no_telefon = request_data['no_telefon']
        email = request_data['email']
        password = request_data['password']
        admin = Admin(nama, no_telefon, email, password)
        db.session.add(admin)
        db.session.commit()   

    list_ = []
    senarai_admin = Admin.query.all()
    for admin in senarai_admin:
        satu_admin = {
            'nama': admin.nama,
            'no_telefon': admin.no_telefon,
            'email': admin.email,
            'password': admin.password
        }
        list_.append(satu_admin)
    return jsonify(list_)

@admin_bp.route('/<int:id>', methods=['GET', 'PUT'])
def satu_admin(id):
    admin = Admin.query.get(id)

    if request.method == 'PUT':        
        request_data = request.get_json()
        admin.nama = request_data['nama']
        admin.no_telefon = request_data['no_telefon']
        admin.email = request_data['email']
        admin.password = request_data['password']  
        db.session.commit()                         

    satu_admin = {
            'nama': admin.nama,
            'no_telefon': admin.no_telefon,
            'email': admin.email,
            'password': admin.password
    }       
    return jsonify(satu_admin)      