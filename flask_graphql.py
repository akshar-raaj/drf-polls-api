import os
from flask import Flask, request, jsonify

from hello_graphene import schema

app = Flask(__name__)

@app.route('/graphql')
def graphql():
    query = request.args.get('query')
    result = schema.execute(query)
    return jsonify(result.data)
