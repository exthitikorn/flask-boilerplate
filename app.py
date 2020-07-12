from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
CORS(app)

@app.route('/')
def root():
    return "สวัสดีวันอาทิตย์"

@app.route('/new')
def new_one_faction():
    username = request.args.get('name')
    print(username)
    return 'Hi ' + username

@app.route('/sum')
def sum_faction():
    a = request.args.get('a')
    a = int(a)
    b = int(request.args.get('b'))
    ans = a + b
    return str(ans)

@app.route('/mypage')
def mypage_faction():
    username = request.args.get('name')
    return render_template('home.html',name= username)

if __name__ == "__main__":
    app.run(debug = True, host="0.0.0.0", port=5000)