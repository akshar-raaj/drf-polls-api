import json
from flask import Flask, request

from hello_graphene import schema

app = Flask(__name__)

@app.route('/graphql')
def graphql():
    query = request.args.get('query')
    result = schema.execute(query)
    d = json.dumps(result.data)
    return '{}'.format(d)
