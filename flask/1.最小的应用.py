# 导入Flask类库
from flask import Flask

# 创建应用实例
app = Flask(__name__)


# 视图函数（路由）
@app.route("/")
def hello_world():
    return "Hello, World!"


# 启动服务
if __name__ == '__main__':
    app.run(debug=True)
