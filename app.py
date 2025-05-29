from flask import Flask, request, render_template, jsonify
import math

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        num1 = float(request.form['num1'])
        num2 = float(request.form['num2']) if request.form['num2'] else 0
        operation = request.form['operation']
        
        operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
            'sin': lambda x, _: math.sin(math.radians(x)),
            'cos': lambda x, _: math.cos(math.radians(x)),
            'tan': lambda x, _: math.tan(math.radians(x)),
            'sqrt': lambda x, _: math.sqrt(x),
            'log': lambda x, _: math.log10(x),
            'ln': lambda x, _: math.log(x),
            'pow': lambda x, _: math.pow(x, 2),
            'exp': lambda x, _: math.exp(x),
            'pi': lambda _, __: math.pi,
            'e': lambda _, __: math.e,
        }
        
        result = operations[operation](num1, num2)
        
        if isinstance(result, float):
            result = round(result, 6)
        return jsonify({'result': str(result)})
    
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Try different port