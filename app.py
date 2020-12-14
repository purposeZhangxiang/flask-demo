from flask import Flask, request, jsonify
from flask_cors import CORS  # 处理跨域包
import json

app = Flask(__name__)
CORS(app, support_credentials=True)  # 允许跨域


@app.route('/get', methods=['GET'])
def hello_world():
    # 路由拦截 处理请求 连接数据库等业务操作
    print(request.args)
    return 'Hello World!'


@app.route("/test", methods=['POST'])
def test():
    # contentType = 'application'  使用request.data去接
    # contentType = ''             使用request.form去接
    data = (request.get_data(as_text=True))
    data1 = request.form

    # username = data['username']

    print(data, type(data), data1['username'])

    return {
        "user": '1233'
    }


if __name__ == '__main__':
    app.run()
