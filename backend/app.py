from flask import Flask, request, jsonify
from validations.password_validation import validate_password
from validations.email_validation import validate_email
from validations.username_validation import validate_username
from validations.phone_validation import validate_phone
from flask_cors import CORS


app = Flask(__name__)

CORS(app)  

@app.route('/api/numbers', methods=['GET'])

def get_numbers():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
11, 12, 13, 14, 15, 16, 17, 18, 19, 20,
21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
51, 52, 53, 54, 55, 56, 57, 58, 59, 60,
61, 62, 63, 64, 65, 66, 67, 68, 69, 70,
71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
81, 82, 83, 84, 85, 86, 87, 88, 89, 90,
91, 92, 93, 94, 95, 96, 97, 98, 99, 100]
    return jsonify(numbers)

@app.route('/validate', methods=['POST'])

def validate_input():
    data = request.json
    
    # Password validation
    password = data.get('password')
    password_error = validate_password(password)
    if password_error:
        return jsonify({'error': password_error}), 400

    # Email validation
    email = data.get('email')
    email_error = validate_email(email)
    if email_error:
        return jsonify({'error': email_error}), 400

    # Username validation
    username = data.get('username')
    username_error = validate_username(username)
    if username_error:
        return jsonify({'error': username_error}), 400

    # Phone number validation
    phone = data.get('phone')
    phone_error = validate_phone(phone)
    if phone_error:
        return jsonify({'error': phone_error}), 400

    # All checks passed
    return jsonify({'message': 'All inputs are valid'}), 200


if __name__ == '__main__':
    app.run(debug=True)