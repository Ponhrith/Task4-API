from fastapi import FastAPI
# app =from fastapi import FastAPI
app = FastAPI()

@app.get("/my-first-api")
# def hello(name = None):
#     if name is None:
#         text = 'Hello!'
#     else:
#         text = 'Hello' + name + '!'
#     return text

def get_iris():
    # import panda as pd
    # url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
    # iris = pd.read_csv(url)

    import requests 
    from PIL import Image
    import io

    resp = requests.get('http://127.0.0.1:8000/my-first-api?name=Pony')
    resp.text

    # return iris

