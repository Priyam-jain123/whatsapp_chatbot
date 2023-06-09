from flask import Flask, request, jsonify
from ultrabot import ultrachatbot
import json

app =Flask(__name__)
@app.route('/',methods=['POST'])

def home():
    if request.method  == 'POST':
        bot = ultrachatbot(request.json)
        return bot.Processing_incoming_messages()

if (__name__)== '__main__':
    app.run()