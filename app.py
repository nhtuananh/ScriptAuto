from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Đường dẫn đến file emails.txt
EMAIL_FILE = 'emails.txt'
STT_FILE = 'emails.txt'

# Lấy secret key từ biến môi trường hoặc mặc định là 'htadz'
SECRET_KEY = os.environ.get('API_KEY', 'htadzhehe')

# Endpoint kiểm tra API
@app.route('/', methods=['GET'])
def health_check():
    return jsonify({'status': 'API is running'})

# Endpoint lấy email
@app.route('/api/email', methods=['GET'])
def get_email():
    # Lấy tham số key và email từ query string
    provided_key = request.args.get('key')
    email_index = request.args.get('email', type=int)

    # Kiểm tra key
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

# Endpoint lấy stt
@app.route('/api/stt', methods=['GET'])
def get_email():
    # Lấy tham số key và email từ query string
    provided_key = request.args.get('key')
    email_index = request.args.get('email', type=int)

    # Kiểm tra key
    if provided_key is None:
        return jsonify({'error': 'Missing API key. Please provide ?key=<your_key>'}), 401
    if provided_key != SECRET_KEY:
        return jsonify({'error': 'Invalid API key'}), 401

    # Kiểm tra tham số email
    if email_index is None:
        return jsonify({'error': 'Please provide a valid email index using ?email=<number>'}), 400
    
    # Đọc file stt.txt
    try:
        if not os.path.exists(STT_FILE):
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

# Endpoint xóa email bằng GET
@app.route('/api/email/remove', methods=['GET'])
def remove_email():
    # Lấy tham số key và email từ query string
    provided_key = request.args.get('key')
    email_index = request.args.get('email', type=int)

    # Kiểm tra key
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
            
        # Xóa email tại dòng tương ứng
        deleted_email = emails.pop(email_index - 1)
        
        # Ghi lại danh sách email vào file
        with open(EMAIL_FILE, 'w', encoding='utf-8') as file:
            for email in emails:
                file.write(email + '\n')
        
        return jsonify({'message': f'Email removed successfully'})
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

# Endpoint xóa stt bằng GET
@app.route('/api/stt/remove', methods=['GET'])
def remove_email():
    # Lấy tham số key và email từ query string
    provided_key = request.args.get('key')
    email_index = request.args.get('email', type=int)

    # Kiểm tra key
    if provided_key is None:
        return jsonify({'error': 'Missing API key. Please provide ?key=<your_key>'}), 401
    if provided_key != SECRET_KEY:
        return jsonify({'error': 'Invalid API key'}), 401

    # Kiểm tra tham số email
    if email_index is None:
        return jsonify({'error': 'Please provide a valid email index using ?email=<number>'}), 400
    
    # Đọc file stt.txt
    try:
        if not os.path.exists(STT_FILE):
            return jsonify({'error': 'Emails file not found'}), 404
            
        with open(EMAIL_FILE, 'r', encoding='utf-8') as file:
            emails = [line.strip() for line in file if line.strip()]
        
        # Kiểm tra nếu index hợp lệ
        if email_index < 1 or email_index > len(emails):
            return jsonify({'error': f'Email index out of range. Valid range: 1 to {len(emails)}'}), 400
            
        # Xóa email tại dòng tương ứng
        deleted_email = emails.pop(email_index - 1)
        
        # Ghi lại danh sách email vào file
        with open(EMAIL_FILE, 'w', encoding='utf-8') as file:
            for email in emails:
                file.write(email + '\n')
        
        return jsonify({'message': f'Email removed successfully'})
    
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
