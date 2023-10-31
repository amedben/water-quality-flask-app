from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
import os
from wtforms import Form, StringField, TextAreaField, PasswordField, validators ,SubmitField
from flask_wtf import FlaskForm
import pickle
import numpy as np

model = pickle.load(open('water.pkl','rb'))
scaler = pickle.load(open('scaler.pkl','rb'))
app = Flask(__name__)
app.secret_key = os.urandom(24)

class Form(FlaskForm):
    aluminium = StringField("aluminium", validators=[])
    ammonia = StringField("ammonia", validators=[])
    arsenic = StringField("arsenic", validators=[])
    barium = StringField("barium", validators=[])
    cadmium = StringField("cadmium", validators=[])
    chloramine = StringField("chloramine", validators=[])
    chromium = StringField("chromium", validators=[])
    copper = StringField("copper", validators=[])
    flouride = StringField("flouride", validators=[])
    bacteria = StringField("bacteria", validators=[])
    viruses = StringField("viruses", validators=[])
    lead = StringField("lead", validators=[])
    nitrates = StringField("nitrates", validators=[])
    nitrites = StringField("nitrites", validators=[])
    mercury = StringField("mercury", validators=[])
    perchlorate = StringField("perchlorate", validators=[])
    radium = StringField("radium", validators=[])
    selenium = StringField("selenium", validators=[])
    silver = StringField("silver", validators=[])
    uranium = StringField("uranium", validators=[])
    submit = SubmitField("Submit")


@app.route('/',methods=['GET', 'POST'])
def index():
    fname = None
    lname = None
    form = Form()
    if form.validate_on_submit():
        aluminium=form.aluminium.data
        ammonia=form.ammonia.data
        arsenic=form.arsenic.data
        barium=form.barium.data
        cadmium=form.cadmium.data
        chloramine=form.chloramine.data
        chromium=form.chromium.data
        copper=form.copper.data
        flouride=form.flouride.data
        bacteria=form.bacteria.data
        viruses=form.viruses.data
        lead=form.lead.data
        nitrates=form.nitrates.data
        nitrites=form.nitrites.data
        mercury=form.mercury.data
        perchlorate=form.perchlorate.data
        radium=form.radium.data
        selenium=form.selenium.data
        silver=form.silver.data
        uranium=form.uranium.data
        features=np.array([[aluminium,ammonia,arsenic,barium,cadmium,chloramine,chromium,copper,flouride,bacteria,viruses,lead,nitrates,nitrites,mercury,perchlorate,radium,selenium,silver,uranium,]])
        features = features.astype(np.float)
        features = scaler.transform(features)
        pred= model.predict(features)
        if pred[0] == '0':
            return render_template('notsafe.html')
        else:
            return render_template('safe.html')
    return render_template('home.html',fname=fname,lname=lname,form=form)


if __name__ == '__main__':
    app.run(debug=True)