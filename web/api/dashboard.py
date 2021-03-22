from api import app
from flask import jsonify

@app.route('/dashboard/store_count', methods=['GET']) 
def getStoreCount(): 
	return jsonify({
		'store_count': 20
	}),200