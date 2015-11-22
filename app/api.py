from app import app
from flask import request, jsonify
import pymongo

client = pymongo.MongoClient('localhost')
db = client.bro

@app.route("/api/bro", methods=['GET', 'POST'])
def get_bro():
    if request.method == 'GET':
        return 'brobiscuits'
    elif request.method == 'POST':
        new_bro = request.json['bro']
        if not db.bros.find_one({'bro': 'brobeans'}) and 'bro' in new_bro:
             db.bros.insert({'bro': request.data})
        else:
            return jsonify({'msg': 'No dice, bro'}), 400
        return jsonify({'msg': 'Nailed it, broski', 'bro': new_bro}), 201
