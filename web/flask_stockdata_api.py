#!usr/bin/python
from flask import Flask
from flask import make_response
from flask import jsonify
from flask import request

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/')
def index():
    return "Hello, World!"

# Call as /stockdata/AKER?start=2018-01-01&end=2018-06-08
# If start is missing we start at the first available datapoint.
# If end is missing it is set to today.
@app.route('/stockdata/<string:ticker>', methods=['GET'])
def get_stockdata(ticker):
	start  = request.args.get('start', None)
	end  = request.args.get('end', None)
	return "{} - {} - {}".format(ticker,start,end)

if __name__ == '__main__':
    app.run(debug=True)