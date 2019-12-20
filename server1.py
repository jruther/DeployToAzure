
from flask import Flask, jsonify, request, abort

from weatherDAO import weatherDAO

app = Flask(__name__,static_url_path='',static_folder='')


#"http://127.0.0.1:5000/weather"
@app.route('/weather')
def getAll():
    results = weatherDAO.getAll()
    return jsonify(results)


if __name__ == '__main__' :
    app.run(debug= True)