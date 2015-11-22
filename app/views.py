from app import app
from app import api
from flask import render_template

@app.route('/')
def index():
  bro = api.get_bro()
  return render_template('index.html', title='Word, Bro', bro=bro)
