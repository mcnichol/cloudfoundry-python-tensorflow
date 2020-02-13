"""Cloud Foundry test"""
from __future__ import print_function
from flask import Flask
import tensorflow as tf
import numpy as np
import random as r
import os

# Simple hello world using TensorFlow

# Create a Constant op
# The op is added as a node to the default graph.
#
# The value returned by the constructor represents the output
# of the Constant op.

# Start tf session

# Run the op
app = Flask(__name__)

port = int(os.environ.get("PORT",8080))

@app.route('/')
def hello_tensor():
    hello = tf.constant('Hello, TensorFlow!  You were just callled from a TensorFlow Session.  Have a numpy array: ')
    sess = tf.compat.v1.Session()

    array = np.array([getRandom(),getRandom(),getRandom()])

    response = sess.run(hello)
    sess.close()

    return str(response.decode('ASCII') + np.array2string(array))

@app.route('/rand')
def getRandom():
    return r.randint(1,100)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
