from flask import Flask

app = Flask(__name__)  # 创建一个wsgi应用


@app.route('/')  # 添加路由：根
def hello_world():
    return 'Hello World!'  # 输出一个字符串


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
