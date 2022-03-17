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


class Premis(Base):

    __tablename__ = 'premis'    
    
    # no_akaun_premis	Nombor akaun premis	varchar	20			Nombor akaun premis
    no_akaun_premis = db.Column(db.String(256), nullable=False)
    
    # no_kad_pengenalan	Nombor kad pengenalan	int				Nombor kad pengenalan
    no_kad_pengenalan = db.Column(db.Integer, nullable=False)
    
    # taman	Taman	varchar				Taman 
    taman = db.Column(db.String(256), nullable=False)

    # kadar_sewa	Kadar sewa	Double				Kadar sewa premis
    kadar_sewa = db.Column(db.Float, nullable=False)

    # jumlah_telah_bayar	Jumlah telah bayar	Double				Jumlah sewa yang telah dibayar
    jumlah_telah_bayar = db.Column(db.Float, nullable=False)

    # jumlah_tunggakan	Jumlah tunggakan	Double				Jumlah tunggakan premis
    jumlah_tunggakan = db.Column(db.Float, nullable=False)

    # tarikh_mula_perjanjian	Tarikh mula perjanjian	Date				Tarikh mula perjanjian sewa premis
    tarikh_mula_perjanjian = db.Column(db.Integer, nullable=False)

    # tarikh_tamat_perjanjian	Tarikh tamat perjanjian	Date				Tarikh tamat perjanjian sewa premis
    tarikh_tamat_perjanjian = db.Column(db.Integer, nullable=False)

    # kod_kategori	Kod kategori	Int				Kod kategori premis
    kod_kategori = db.Column(db.Integer, nullable=False)

    # kategori	Kategori	varchar				Kategori premis
    kategori = db.Column(db.String(256), nullable=False)

    # bandar	Bandar	varchar	50			Bandar
    bandar = db.Column(db.String(256), nullable=False)


    def __init__(self, no_akaun_premis, no_kad_pengenalan, taman, kadar_sewa, 
        jumlah_telah_bayar, jumlah_tunggakan, tarikh_mula_perjanjian, tarikh_tamat_perjanjian, 
        kod_kategori, kategori, bandar):

        self.no_akaun_premis = no_akaun_premis
        self.no_kad_pengenalan = no_kad_pengenalan
        self.taman = taman
        self.kadar_sewa = kadar_sewa
        self.jumlah_telah_bayar = jumlah_telah_bayar
        self.jumlah_tunggakan = jumlah_tunggakan
        self.tarikh_mula_perjanjian = tarikh_mula_perjanjian
        self.tarikh_tamat_perjanjian = tarikh_tamat_perjanjian
        self.kod_kategori = kod_kategori
        self.kategori = kategori
        self.bandar = bandar


