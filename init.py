# from flask import Flask
from flask import Flask, render_template, request
import core

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/data_handle", methods=['POST', 'GET'])
def data_handle():
    data = request.form['product']
    a_title, a_price, a_url, f_title, f_price, f_url = core.main(data)
    return render_template("index.html",a_title = a_title, a_price = a_price, a_url = a_url
    ,f_title= f_title, f_price = f_price, f_url = f_url)
# @app.route("/salvador")
# def salvador():
#     return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)