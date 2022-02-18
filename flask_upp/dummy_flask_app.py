from flask import Flask, request, Response
from flask_restful import Resource, Api
import sys
import os
from flask import jsonify


app = Flask(__name__)
api = Api(app)
port = 5100


@app.route('/')
def index():
    return 'Server Works!'


@app.route('/pay/<amount>', methods=['POST'])
def pay(amount):
    return Response(status=200)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=port)