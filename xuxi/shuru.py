from flask import Flask, request, jsonify
from flask_cors import CORS
app = Flask(__name__)

CORS(app)

# 定义根路径的路由，返回一个简单的欢迎信息
@app.route('/')
def index():
    return '欢迎使用姓名输入系统！'

# 定义/check_name接口的处理函数，接收POST请求
@app.route('/check_name', methods=['POST'])
def check_name():
    # 从请求体中获取JSON格式的数据，包括姓名
    name = request.json['name']
    if name.strip() == '': # 判断姓名是否为空
        return jsonify({'success': False, 'message': '姓名不能为空！'}) # 返回JSON格式的响应数据，包括success和message字段
    else:
        # TODO: 保存操作，可以在这里进行保存操作，比如保存到数据库中
        # 校验通过，返回JSON格式的响应数据，包括success字段
        return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug = True, port= 8888) # 启动Flask应用程序