import requests
import json
import time
import os

from flask import Flask, render_template, flash, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from decouple import config

from apps import db

class Base(db.Model):

    __abstract__  = True

    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())


class Perumahan(Base):

    __tablename__ = 'perumahan'    
    
    # F user_id	User ID	int				Penghubung Entiti User
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    
    # nama	Nama pemilik	varchar				Nama penuh pemilik rumah
    nama = db.Column(db.String(256), nullable=False)

    # no_kad_pengenalan	Nombor kad pengenalan	int				Nombor kad pengenalan pemilik rumah
    no_kad_pengenalan = db.Column(db.Integer, nullable=False)

    # no_rumah	Nombor rumah	varchar				Nombor rumah
    no_rumah = db.Column(db.String(256), nullable=False)

    # taman	Taman	varchar				Taman perumahan
    taman = db.Column(db.String(256), nullable=False)

    # kod_kategori	Kod kategori	int				Kod kategori perumahan
    kod_kategori = db.Column(db.Integer, nullable=False)

    # kategori	Kategori	varchar				Kategori perumahan
    kategori = db.Column(db.String(256), nullable=False)

    # kadar_sewa	Kadar sewa	double				Kadar sewa rumah
    kadar_sewa = db.Column(db.Float, nullable=False)

    # jenis_rumah	Jenis rumah	varchar				Jenis rumah 
    jenis_rumah = db.Column(db.String(256), nullable=False)

    # jumah_telah_bayar	Jumlah telah bayar	double				Jumlah sewa yang telah dibayar
    jumah_telah_bayar = db.Column(db.Float, nullable=False)

    # jumlah_pinjaman	Jumlah pinjaman	double				Jumlah pinjaman
    jumlah_pinjaman = db.Column(db.Float, nullable=False)

    # tarikh_mula_perjanjian	Tarikh mula perjanjian	date				Tarikh mula perjanjian sewa rumah
    tarikh_mula_perjanjian = db.Column(db.Integer, nullable=False)

    # tarikh_tamat_perjanjian	Tarikh tamat perjanjian	date				Tarikh tamat perjanjian sewa rumah
    tarikh_tamat_perjanjian = db.Column(db.Integer, nullable=False)

    # jumlah_tunggakan	Jumlah tunggakan	double				Jumlah tunggakan sewa rumah
    jumlah_tunggakan = db.Column(db.Float, nullable=False)

    # jumlah_baki	Jumlah baki	double				Jumlah baki yang perlu dibayar
    jumlah_baki = db.Column(db.Float, nullable=False)

    # no_akaun_rumah	Nombor akaun rumah	varchar	20			Nombor akaun rumah
    no_akaun_rumah = db.Column(db.String(256), nullable=False)


    def __init__(self, user_id, nama, no_kad_pengenalan, no_rumah, taman, kod_kategori, 
        kategori, kadar_sewa, jenis_rumah, jumah_telah_bayar, jumlah_pinjaman, tarikh_mula_perjanjian, 
        tarikh_tamat_perjanjian, jumlah_tunggakan, jumlah_baki, no_akaun_rumah):

        self.user_id = user_id
        self.nama = nama
        self.no_kad_pengenalan = no_kad_pengenalan
        self.no_rumah = no_rumah
        self.taman = taman
        self.kod_kategori = kod_kategori
        self.kategori = kategori
        self.kadar_sewa = kadar_sewa
        self.jenis_rumah = jenis_rumah
        self.jumah_telah_bayar = jumah_telah_bayar
        self.jumlah_pinjaman = jumlah_pinjaman
        self.tarikh_mula_perjanjian = tarikh_mula_perjanjian
        self.tarikh_tamat_perjanjian = tarikh_tamat_perjanjian
        self.jumlah_tunggakan = jumlah_tunggakan
        self.jumlah_baki = jumlah_baki
        self.no_akaun_rumah = no_akaun_rumah

