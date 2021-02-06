# from flask import Flask
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/data_handle", methods=['POST', 'GET'])
def data_handle():
    data = request.form['product']
    return render_template("index.html",product = data)
# @app.route("/salvador")
# def salvador():
#     return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)