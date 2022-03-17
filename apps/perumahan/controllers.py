# Import flask dependencies
from flask import Blueprint, request, render_template, jsonify, flash, abort
from sqlalchemy import desc
import time
from apps.perumahan.models import Perumahan
from apps import db

perumahan_bp = Blueprint('perumahan', __name__, url_prefix='/perumahan')


@perumahan_bp.route('/', methods=['GET', 'POST'])
def senarai_perumahan():
    if request.method == 'POST':
        request_data = request.get_json()
        user_id = request_data['user_id']
        nama = request_data['nama']
        no_kad_pengenalan = request_data['no_kad_pengenalan']
        no_rumah = request_data['no_rumah']
        taman = request_data['taman']
        kod_kategori = request_data['kod_kategori']
        kategori = request_data['kategori']
        kadar_sewa = request_data['kadar_sewa']
        jenis_rumah = request_data['jenis_rumah']
        jumah_telah_bayar = request_data['jumah_telah_bayar']
        jumlah_pinjaman = request_data['jumlah_pinjaman']
        tarikh_mula_perjanjian = request_data['tarikh_mula_perjanjian']
        tarikh_tamat_perjanjian = request_data['tarikh_tamat_perjanjian']
        jumlah_tunggakan = request_data['jumlah_tunggakan']
        jumlah_baki = request_data['jumlah_baki']
        no_akaun_rumah = request_data['no_akaun_rumah']
        perumahan = Perumahan(user_id, nama, no_kad_pengenalan, no_rumah, taman, kod_kategori, 
            kategori, kadar_sewa, jenis_rumah, jumah_telah_bayar, jumlah_pinjaman, tarikh_mula_perjanjian, 
            tarikh_tamat_perjanjian, jumlah_tunggakan, jumlah_baki, no_akaun_rumah)
        db.session.add(perumahan)
        db.session.commit()
        return jsonify(perumahan)    
    else:
        list_ = []
        senarai_perumahan = Perumahan.query.all()
        for perumahan in senarai_perumahan:
            list_.append(perumahan)
        return jsonify(list_) 


@perumahan_bp.route('/<int:id>', methods=['GET', 'PUT'])
def satu_perumahan(id):
    
    if request.method == 'PUT':
        pass

    else:
        perumahan = Perumahan.query.get(id)
        return jsonify(perumahan)    