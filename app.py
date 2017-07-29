from bs4 import BeautifulSoup
from flask import Flask, render_template, request
import requests

AF_URL = 'https://www.abercrombie.com/webapp/wcs/stores/servlet/Search?storeId=10051&catalogId=10901&langId=-1&departmentCategoryId=10000&search-field='
AT_URL = 'https://www.anntaylor.com/search/searchResults.jsp?question='

app = Flask(__name__)


def get_product(html_doc):
    soup = BeautifulSoup(html_doc, "html.parser")
    res = soup.find(id="pid-9947721")
    return res


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        res_html = requests.get(AF_URL + query)
        res = get_product(res_html.text)
        return render_template('index.html', res=res)
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
