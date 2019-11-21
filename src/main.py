from blockchain import Blockchain
import json
from uuid import uuid4
from flask import Flask, jsonify


app = Flask(__name__)


# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')
# Instantiate the Blockchain
blockchain = Blockchain()
@app.route("/")
def home():
    return "Hello, Flask!"


@app.route('/mine', methods=['GET'])
def mine():
    return "We'll mine a new Block"


@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    return "We'll add a new transaction"


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain)
    }
    return jsonify(response), 200


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, threaded=True)
