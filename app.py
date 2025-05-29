from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import math
import os

app = Flask(__name__, template_folder=os.path.abspath('templates'))
CORS(app)  # Enable CORS for all routes

@app.route('/')
def index():
    try:
        print(f"Template folder: {app.template_folder}")  # Debug print
        print(f"Templates available: {os.listdir(app.template_folder)}")  # Debug print
        return render_template('index.html')
    except Exception as e:
        print(f"Error rendering template: {str(e)}")  # Debug print
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
    app.run(debug=True, host='127.0.0.1', port=8080)