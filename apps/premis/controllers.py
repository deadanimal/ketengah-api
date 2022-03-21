# Import flask dependencies
from flask import Blueprint, request, render_template, jsonify, flash, abort
from sqlalchemy import desc
import time
from apps.premis.models import Premis
from apps import db

premis_bp = Blueprint('premis', __name__, url_prefix='/premis')


@premis_bp.route('/', methods=['GET', 'POST'])
def senarai_premis():
    if request.method == 'POST':
        request_data = request.get_json()
        no_akaun_premis = request_data['no_akaun_premis']
        no_kad_pengenalan = request_data['no_kad_pengenalan']
        taman = request_data['taman']
        kadar_sewa = request_data['kadar_sewa']
        jumlah_telah_bayar = request_data['jumlah_telah_bayar']
        jumlah_tunggakan = request_data['jumlah_tunggakan']
        tarikh_mula_perjanjian = request_data['tarikh_mula_perjanjian']
        tarikh_tamat_perjanjian = request_data['tarikh_tamat_perjanjian']
        kod_kategori = request_data['kod_kategori']
        kategori = request_data['kategori']
        bandar = request_data['bandar']
        premis = Premis(no_akaun_premis, no_kad_pengenalan, taman, kadar_sewa, jumlah_telah_bayar, 
            jumlah_tunggakan, tarikh_mula_perjanjian, tarikh_tamat_perjanjian, kod_kategori, kategori, bandar, premis)
        db.session.add(premis)
        db.session.commit()  

    list_ = []
    senarai_premis = Premis.query.all()
    for premis in senarai_premis:
        satu_premis = {
            "no_akaun_premis": premis.no_akaun_premis,
            "no_kad_pengenalan": premis.no_kad_pengenalan,
            "taman": premis.taman,
            "kadar_sewa": premis.kadar_sewa,
            "jumlah_telah_bayar": premis.jumlah_telah_bayar,
            "jumlah_tunggakan": premis.jumlah_tunggakan,
            "tarikh_mula_perjanjian": premis.tarikh_mula_perjanjian,
            "tarikh_tamat_perjanjian": premis.tarikh_tamat_perjanjian,
            "kod_kategori": premis.kod_kategori,
            "kategori": premis.kategori,
            "bandar": premis.bandar,
        }           
        list_.append(satu_premis)
    return jsonify(list_) 


@premis_bp.route('/<int:id>', methods=['GET', 'PUT'])
def satu_premis(id):
    
    premis = db.session.query(Premis).filter_by(id=id).first()

    if request.method == 'PUT': 
        request_data = request.get_json()
        premis.no_akaun_premis = request_data['no_akaun_premis']
        premis.no_kad_pengenalan = request_data['no_kad_pengenalan']
        premis.taman = request_data['taman']
        premis.kadar_sewa = request_data['kadar_sewa']
        premis.jumlah_telah_bayar = request_data['jumlah_telah_bayar']
        premis.jumlah_tunggakan = request_data['jumlah_tunggakan']
        premis.tarikh_mula_perjanjian = request_data['tarikh_mula_perjanjian']
        premis.tarikh_tamat_perjanjian = request_data['tarikh_tamat_perjanjian']
        premis.kod_kategori = request_data['kod_kategori']
        premis.kategori = request_data['kategori']
        premis.bandar = request_data['bandar']
        db.session.commit()      

    return jsonify(premis)    