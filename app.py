from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Đường dẫn đến file emails.txt
EMAIL_FILE = 'emails.txt'

SECRET_KEY = "htadz"

# Endpoint kiểm tra API
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'status': 'API is running'})

@app.route('/api/email', methods=['GET'])
def get_email():
    # Lấy tham số key và email từ query string
    provided_key = request.args.get('key')
    email_index = request.args.get('email', type=int)

    # Kiểm tra key trước
    if provided_key is None:
        return jsonify({'error': 'Missing API key. Please provide ?key=<your_key>'}), 401
    if provided_key != SECRET_KEY:
        return jsonify({'error': 'Invalid API key'}), 401

    # Kiểm tra tham số email
    if email_index is None:
        return jsonify({'error': 'Please provide a valid email index using ?email=<number>'}), 400
    
    # Đọc file emails.txt
    try:
        if not os.path.exists(EMAIL_FILE):
            return jsonify({'error': 'Emails file not found'}), 404
            
        with open(EMAIL_FILE, 'r', encoding='utf-8') as file:
            emails = [line.strip() for line in file if line.strip()]
        
        # Kiểm tra nếu index hợp lệ
        if email_index < 1 or email_index > len(emails):
            return jsonify({'error': f'Email index out of range. Valid range: 1 to {len(emails)}'}), 400
            
        # Trả về email tại dòng tương ứng (index bắt đầu từ 1)
        return jsonify({'email': emails[email_index - 1]})
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
<<<<<<< HEAD
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
=======
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
>>>>>>> aa55d18f9b30a980e35748114a8b09af4c325ddd
