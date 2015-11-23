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

@app.route("/api/bro/flag", methods=['POST'])
def flag_bro():
	flag_bro = request.json 
	match = db.bros.find_one(flag_bro)
	msg = 'flagged it, broski'
	new_flag = 1
	if match is not None:
		if 'flags' in match:
			new_flag = match['flags'] + 1
			if new_flag > 5:
				print db.bros.delete_one(match).deleted_count
				msg = 'deleted'
			else:
				db.bros.update_one(match, {'$set': {'flags': new_flag}}, upsert = False)
				print match
		else:
			db.bros.update_one(match, {'$set': {'flags': new_flag}}, upsert = False)
			print match
	else:
		msg = 'No record to flag'
	return jsonify({'msg': msg, 'flags': new_flag})

