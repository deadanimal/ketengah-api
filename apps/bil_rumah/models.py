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

    # F perumahan_id	Perumahan ID	int				Penghubung entiti PERUMAHAN
    perumahan_id = db.Column(db.Integer, db.ForeignKey('perumahan.id'), nullable=False)

    # amaun	Amaun	double				Amaun bil bulanan
    amaun = db.Column(db.Float, nullable=False)

    # bulan	Bulan	varchar	20			Bulan bil
    bulan = db.Column(db.String(256), nullable=False)

    # tahun	Tahun	int				Tahun bil
    tahun = db.Column(db.Integer, nullable=False)



    def __init__(self, perumahan_id, amaun, bulan, tahun):

        self.perumahan_id = perumahan_id
        self.amaun = amaun
        self.bulan = bulan
        self.tahun = tahun

