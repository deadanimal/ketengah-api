# Import flask dependencies
from flask import Blueprint, request, render_template, jsonify, flash, abort
from sqlalchemy import desc
import time
from apps.perumahan.models import Perumahan
from apps import db

perumahan_bp = Blueprint('perumahan', __name__, url_prefix='/perumahan')


@perumahan_bp.route('/', methods=['GET', 'POST', 'PUT'])
def perumahan():
    data = {}
    if request.method == 'POST':
        pass
    elif request.method == 'PUT':
        pass
    
    return jsonify(data)