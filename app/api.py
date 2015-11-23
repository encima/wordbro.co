from app import app
from flask import request, jsonify
import pymongo
import random
import ast

client = pymongo.MongoClient('localhost')
db = client.bro

@app.route("/api/bro", methods=['GET', 'POST'])
def get_bro():
    if request.method == 'GET':
		if db.bros.find_one({}) is not None:
			return jsonify({'bro':random.choice(list(db.bros.find()))['bro']})
		else:
			return jsonify({'bro': 'Bro'})
    elif request.method == 'POST':
        new_bro = request.json
        print new_bro
        match = db.bros.find_one(new_bro)
        if match is None and 'bro' in new_bro['bro'].lower():
             db.bros.insert(new_bro)
        else:
            return jsonify({'msg': 'No dice, bro'}), 400
        return jsonify({'msg': 'Nailed it, broski', 'bro': new_bro['bro']}), 201
