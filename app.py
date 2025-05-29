from flask import Flask, request, render_template, jsonify, current_app
from flask_cors import CORS
import math
import os

# Change template folder to relative path
app = Flask(__name__, 
    template_folder='templates',
    static_folder='static')
CORS(app)

# Add error handlers
@app.errorhandler(404)
def not_found_error(error):
    print(f"404 Error: {error}")
    return "Page not found", 404

@app.errorhandler(500)
def internal_error(error):
    print(f"500 Error: {error}")
    return "Internal server error", 500

@app.route('/')
def index():
    try:
        # Add absolute path debug info
        current_dir = os.path.dirname(os.path.abspath(__file__))
        template_path = os.path.join(current_dir, 'templates')
        print(f"Current directory: {current_dir}")
        print(f"Template path: {template_path}")
        print(f"Template exists: {os.path.exists(os.path.join(template_path, 'index.html'))}")
        return render_template('index.html')
    except Exception as e:
        print(f"Error rendering template: {str(e)}")
        return str(e), 500

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form.get('num1', 0))
    num2 = float(request.form.get('num2', 0))
    operation = request.form.get('operation', '')
    
    result = 0
    try:
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            result = num1 / num2
        elif operation == 'sin':
            result = math.sin(math.radians(num1))
        elif operation == 'cos':
            result = math.cos(math.radians(num1))
        elif operation == 'tan':
            result = math.tan(math.radians(num1))
        elif operation == 'log':
            result = math.log10(num1)
        elif operation == 'ln':
            result = math.log(num1)
        elif operation == 'sqrt':
            result = math.sqrt(num1)
        elif operation == 'pow':
            result = math.pow(num1, 2)
        elif operation == 'exp':
            result = math.exp(num1)
        elif operation == 'pi':
            result = math.pi
        elif operation == 'e':
            result = math.e
            
        return jsonify({'result': result})
    except Exception as e:
        return jsonify({'result': 'Error', 'message': str(e)}), 400

if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['DEBUG'] = True
    app.run(host='127.0.0.1', port=8080, use_reloader=True)