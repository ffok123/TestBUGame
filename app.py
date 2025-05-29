from flask import Flask, request, render_template, jsonify
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

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
    app.run(debug=True, host='0.0.0.0', port=5000)