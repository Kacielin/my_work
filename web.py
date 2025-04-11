from flask import Flask
from flask.wrappers import Response

app = Flask(__name__)

@app.route('/')
def hello_world():
    return Response('不要不开心！', mimetype='text/plain')

# 去除不必要的handler函数，直接使用Flask默认请求处理机制
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)