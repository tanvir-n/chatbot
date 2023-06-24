from flask import Flask, render_template, request, jsonify

from chat import get_response

app = Flask(__name__)

@app.get('/')
def func_1():
    return render_template('base.html')

@app.post('/predict')
def func_2():
    text = request.get_json().get('message')
    
    response = get_response(text)
    return jsonify({'answer': response})

if __name__=='__main__':
    app.run(debug=True)
