from flask import Flask, request, render_template, jsonify
from flask_cors import CORS
import math
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

app = Flask(__name__, template_folder='templates')
CORS(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # Get raw inputs
        num1_raw = request.form.get('num1', None)
        num2_raw = request.form.get('num2', None)
        operation = request.form.get('operation', '').strip()

        # Log raw inputs
        logger.debug(f"Raw inputs - num1: {num1_raw}, num2: {num2_raw}, operation: {operation}")

        # Validate and convert inputs
        try:
            num1 = float(num1_raw) if num1_raw else 0
        except ValueError:
            raise ValueError(f"Invalid input for num1: {num1_raw}")
        
        try:
            num2 = float(num2_raw) if num2_raw else 0
        except ValueError:
            raise ValueError(f"Invalid input for num2: {num2_raw}")

        # Validate operation
        valid_operations = ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt', 'pow', 'exp', 'pi', 'e', '+', '-', '*', '/']
        if operation not in valid_operations:
            raise ValueError(f"Invalid operation: {operation}")

        logger.debug(f"Validated inputs - num1: {num1}, num2: {num2}, operation: {operation}")

        # Perform calculation
        if operation in ['sin', 'cos', 'tan', 'log', 'ln', 'sqrt', 'pow', 'exp', 'pi', 'e']:
            result = handle_single_operation(num1, operation)
        else:
            result = handle_binary_operation(num1, num2, operation)

        logger.debug(f"Calculation result: {result}")
        return jsonify({'result': result})

    except ZeroDivisionError:
        return jsonify({'error': 'Division by zero'}), 400
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        logger.error(f"Calculation error: {str(e)}")
        return jsonify({'error': 'Calculation error'}), 500

def handle_single_operation(num, operation):
    if operation in ['log', 'ln', 'sqrt'] and num <= 0:
        raise ValueError(f"Invalid input for {operation}: {num}")
    if operation == 'tan' and (num % 90 == 0 and num % 180 != 0):
        raise ValueError(f"Invalid input for tan: {num} (undefined)")
    
    if operation == 'sin':
        return math.sin(math.radians(num))
    elif operation == 'cos':
        return math.cos(math.radians(num))
    elif operation == 'tan':
        return math.tan(math.radians(num))
    elif operation == 'log':
        return math.log10(num)
    elif operation == 'ln':
        return math.log(num)
    elif operation == 'sqrt':
        return math.sqrt(num)
    elif operation == 'pow':
        return math.pow(num, 2)
    elif operation == 'exp':
        return math.exp(num)
    elif operation == 'pi':
        return math.pi
    elif operation == 'e':
        return math.e

def handle_binary_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 == 0:
            raise ZeroDivisionError("Division by zero")
        return num1 / num2

if __name__ == '__main__':
    print("Starting Flask server...")
    try:
        # Try different host/port combinations if one fails
        try:
            app.run(debug=True, host='127.0.0.1', port=5000)
        except:
            print("Trying alternate port...")
            app.run(debug=True, host='127.0.0.1', port=8080)
    except Exception as e:
        print(f"Server error: {e}")
        print("Try accessing the app at: http://127.0.0.1:5000 or http://127.0.0.1:8080")