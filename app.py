from flask import render_template, jsonify
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    #return render_template('about.html')
    return render_template('templates/about.html') 

@app.route('/api/data')
def api_data():
    data = {
        'name': 'Noel Draxler',
        'age': 20,
        'location': 'Cameroon - Bangangte'
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(port=8080, debug=True)
