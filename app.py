from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Hello, World!"

@app.route('/bfhl', methods=['POST'])
def bfhl_post():
    try:
        data = request.get_json().get('data', [])
        numbers = [x for x in data if isinstance(x, int)]
        alphabets = [x for x in data if isinstance(x, str) and x.isalpha()]
        highest_alphabet = max(alphabets) if alphabets else None
        response = {
            "is_success": True,
            "user_id": "john_doe_123",
            "email": "john.doe@example.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_alphabet": highest_alphabet
        }
        return jsonify(response), 200
    except Exception as e:
        return jsonify({"is_success": False, "error": str(e)}), 400

@app.route('/bfhl', methods=['GET'])
def bfhl_get():
    return jsonify({"operation_code": 1}), 200

if __name__ == '__main__':
    app.run(debug=True)
