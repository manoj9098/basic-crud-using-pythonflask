import json
from flask import Flask,jsonify

app = Flask(__name__)
@app.route('/')

def index():
    return "Welcome to greendeck"
f = open('C:/Users/manoj/Downloads/Greendeck SE Assignment Task 1.json', )
data = json.load(f)
f.close()
@app.route('/data',methods=['GET'])
def get():
    return jsonify({'data':data})
@app.route('/data/<int:id>',methods=['GET'])
def get_data(id):
    return jsonify({'data':data[id]})

@app.route('/data',methods=['POST'])
def create():
    data1 = {
    "brand_name": "U.s polo assn",
    "classification_l1": "shirts",
    "classification_l2": "fashion",
    "classification_l3": "fashion wear",
    "classification_l4": "",
    "currency": "IND",
    "image_url": "https://www.nnnow.com/us-polo-assn-kids-boys-blue-boys-brand-embroidered-pique-polo-shirt-UHPRD8UM1JP?gclid=CjwKCAjw_Y_8BRBiEiwA5MCBJq7IhNE6B8qwiME5upIoWZ00E7t8objK3EhztwumPYlpzQ4pNosfTRoCa7kQAvD_BwE",
    "name": "Rory Dobner Supersize Love Wild Fig and Grape Scented Candle, 2.86kg",
    "offer_price_value": 750.0,
    "regular_price_value": 1000.0

    }
    data.append(data1)
    return jsonify({'created':data})

@app.route('/data/<int:id>',methods=['PUT'])
def update(id):
    data['id'] ["name"] = "abc"
    return jsonify({'data1':data[id]})

@app.route("/data/<int:id>",methods=['DELETE'])
def delete(id):
    data.remove(data[id])
    return jsonify({'result': True})


if __name__ == "__main__":
    app.run(debug=True)


