from flask import Flask, render_template
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def index():
    title = "自由時報財經新聞"

    #TODO
    news_list = []
    
    return render_template('index.html', title=title, news_list=news_list)

if __name__=="__main__":
    app.run(debug=True)
