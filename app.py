from flask import Flask, render_template, request
import requests
from dotenv import load_dotenv
import os

app = Flask(__name__)

load_dotenv()

PORT = os.environ.get('PORT')

@app.route('/')
def start():

    return render_template('index.html')

if __name__ == '__main__':
    
    app.run(debug=True, host='0.0.0.0', port=PORT)