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


class Admin(Base):

    __tablename__ = 'admin'    
    
    # nama	Nama	varchar	150			Nama penuh pengguna
    nama = db.Column(db.String(256), nullable=False)

    # no_telefon	Nombor Telefon	int				Nombor telefon
    no_telefon = db.Column(db.Integer, nullable=False)

    # email	Email	varchar	150			Emel pengguna
    email = db.Column(db.String(256), nullable=False)

    # password	Kata laluan	varchar	50			Kata laluan untuk log masuk
    password = db.Column(db.String(256), nullable=False)




    def __init__(self, name, no_telefon, email, password):

            self.name = name
            self.no_telefon = no_telefon
            self.email = email
            self.password = password

