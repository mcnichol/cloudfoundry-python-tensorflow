"""Cloud Foundry test"""
from __future__ import print_function
from flask import Flask
import tensorflow as tf
import os

'''
HelloWorld example using TensorFlow library.
Author: Aymeric Damien
Project: https://github.com/aymericdamien/TensorFlow-Examples/
'''

# Simple hello world using TensorFlow

# Create a Constant op
# The op is added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.

# Start tf session

# Run the op
app = Flask(__name__)

port = int(os.environ["PORT"])

@app.route('/')
def hello_tensor():
    hello = tf.constant('Hello, TensorFlow!  You were just callled from a TensorFlow Session')
    sess = tf.Session()

    response = sess.run(hello);

    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
