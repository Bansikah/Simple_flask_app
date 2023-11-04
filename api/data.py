from flask import jsonify

def api_data():
    data = {
        'name': 'Noel Draxler',
        'age': 20,
        'location': 'Cameroon - Bangangte'
    }
    return jsonify(data)