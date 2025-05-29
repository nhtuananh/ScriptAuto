from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Đường dẫn đến file emails.txt
EMAIL_FILE = 'emails.txt'

@app.route('/api/email', methods=['GET'])
def get_email():
    # Lấy tham số email từ query string
    email_index = request.args.get('email', type=int)
    
    # Kiểm tra nếu tham số email không được cung cấp hoặc không phải số
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
    # Chạy ứng dụng với host='0.0.0.0' để Render có thể truy cập
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))