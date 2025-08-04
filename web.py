from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def index():
    return 'Bot is alive!'

def run():
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
