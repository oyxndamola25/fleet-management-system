from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/usage-data', methods=['GET'])
def get_usage_data():
    try:
        with open('usage-data.json') as f:
            data = json.load(f)
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
