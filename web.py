from flask import Flask

app = Flask(__name__)

@app.route('/')
def web():
    return '不要不开心！'

if __name__ == '__main__':
    # 这里 host 设置为 0.0.0.0 表示可以从外部访问
    app.run(host='0.0.0.0', port=5000)