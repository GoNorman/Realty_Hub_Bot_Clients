from flask import Flask, request, jsonify
import requests
import json
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

TOKEN = '6350076372:AAEPWYUmrscmdxYaNyV00U22SoQurdOzVXM'
CHAT_ID = -4149412356

URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

def send_to_telegram_bot(data):
    try:
        formatted_text = f"Предположительно новый клиент:\n\nИмя: {data['first_name']}\nТелефон: {data['phone']}\nEmail: {data['email']}\nИнтересует объект: [{data['currentUrl']}]({data['currentUrl']})"

        params = {'chat_id': CHAT_ID, 'text': formatted_text, 'parse_mode': 'Markdown'}

        response = requests.post(URL, params=params)
        response.raise_for_status()

    except Exception as e:
        print(f"Error sending message to Telegram: {e}")

def send_call_reauest_to_bot(data):
    try:
        result_message = f"У нас новый заказ на звонок:\n\nИмя: {data['first_name']}\nТелефон: {data['phone']}\nEmail: {data['email']}\n"

        params = {'chat_id': CHAT_ID, 'text': result_message, 'parse_mode': 'Markdown'}
        response = requests.post(URL, params=params)
        response.raise_for_status()
    except Exception as e:
        print(f"Error sending message to Telegram: {e}")


@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    send_to_telegram_bot(data)
    return jsonify({'message': 'Data submitted successfully'})

@app.route('/request_call', methods=['POST'])
def submit_call():
    data = request.json
    send_call_reauest_to_bot(data)
    return jsonify({'message': "Data submitted successfully"})

if __name__ == '__main__':
    app.run(port=5000, debug=False)
