from app import app
from app import api
from flask import render_template, jsonify
import ast

@app.route('/')
def index():
  bro = api.get_bro()
  return render_template('index.html', bro=ast.literal_eval(bro.data)['bro'], title="Wordbro.co")
