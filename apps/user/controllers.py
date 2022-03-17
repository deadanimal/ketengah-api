# Import flask dependencies
from flask import Blueprint, request, render_template, jsonify, flash, abort
from sqlalchemy import desc
import time
from apps.user.models import User
from apps import db

user_bp = Blueprint('user', __name__, url_prefix='/user')


@user_bp.route('/', methods=['GET', 'POST', 'PUT'])
def user():
    data = {}
    if request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    
    return jsonify(data)