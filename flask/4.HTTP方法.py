from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('welcome.html')


@app.route('/welcome/<name>')
def welcome(name):
    return f'welcome {name}'


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        return redirect(url_for('welcome', name=user))
    else:
        # GET方法获取数据，args是包含表单参数对及其对应值对的列表的字典对象。
        user = request.args.get('username')
        return redirect(url_for('welcome', name=user))


if __name__ == '__main__':
    app.run(debug=True)
