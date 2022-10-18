from flask import Flask, jsonify, request, send_file
app = Flask(__name__)

@app.route("/plot-iris")
def plot_iris():

    import panda as pd
    import matplotlib.pyplot as plt
    import os

    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('flask/iris.png')

    return send_file('iris.png')
