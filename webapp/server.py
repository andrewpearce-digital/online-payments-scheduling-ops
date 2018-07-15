from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')
@app.route('/showSearch')
def showSearch():
    return render_template('search.html')
@app.route('/SearchResult',methods=['POST'])
def searchResult():
    # read the posted values from the UI
    _name = request.form['inputTransactionID']

if __name__ == "__main__":
    app.run()