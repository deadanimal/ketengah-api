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


class User(Base):

    __tablename__ = 'user'    
    
    # name	Nama	varchar	150			Nama penuh pengguna
    name = db.Column(db.String(256), nullable=False)

    # no_ic	Nombor Kad Pengenalan	int				Nombor kad pengenalan pengguna
    no_ic = db.Column(db.Integer, nullable=False)

    # no_telefon	Nombor Telefon	int				Nombor telefon
    no_telefon = db.Column(db.Integer, nullable=False)

    # alamat	Alamat	varchar				Alamat pengguna
    alamat = db.Column(db.String(256), nullable=False)

    # poskod	Poskod	varchar				Poskod
    poskod = db.Column(db.String(256), nullable=False)

    # bandar	Bandar	varchar				Bandar
    bandar = db.Column(db.String(256), nullable=False)

    # negeri	Negeri	varchar				Negeri
    negeri = db.Column(db.String(256), nullable=False)

    # email	Email	varchar	150			Emel pengguna
    email = db.Column(db.String(256), nullable=False)

    # password	Kata laluan	varchar	50			Kata laluan untuk log masuk
    password = db.Column(db.String(256), nullable=False)

    perumahan = db.relationship('Perumahan', backref='user', lazy=True)



    def __init__(self, name, no_ic, no_telefon, alamat, poskod, bandar, 
        negeri, email, password):

            self.name = name
            self.no_ic = no_ic
            self.no_telefon = no_telefon
            self.alamat = alamat
            self.poskod = poskod
            self.bandar = bandar
            self.negeri = negeri
            self.email = email
            self.password = password

