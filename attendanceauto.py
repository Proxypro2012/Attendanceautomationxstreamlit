from flask import Flask, jsonify, request
from flask_cors import CORS
import turtle
app = Flask(__name__)

@app.route('/')
def home():
    return "Backend"



@app.route('/register', methods=['POST'])
def registration_page():
    data = request.get_json()
    userdetails = f"{data.get('name')}, {data.get('networkName')}, {data.get('classname'), {data.get('date')}}"
            
    with open('data.txt', 'w') as file:
        file.write(userdetails)
    if data is None:
        return jsonify({"error":  "No JSON data provided :("}), 400
    print(data)
    return "Data retrieved: Success!" + "" + str(data)










# D E B U G

if __name__ == '__main__':
    app.run(debug=True)



