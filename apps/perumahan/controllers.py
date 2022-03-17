# Import flask dependencies
from flask import Blueprint, request, render_template, jsonify, flash, abort
from sqlalchemy import desc
import time
from apps import db

perumahan_bp = Blueprint('perumahan', __name__, url_prefix='/perumahan')


@perumahan_bp.route('/', methods=['GET', 'POST', 'PUT'])
def perumahan():
    data = {}
    return jsonify(data)