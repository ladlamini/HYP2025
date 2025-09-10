from flask import Flask, request, jsonify
import subprocess 
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

@app.route('/main.py', methods=['POST'])
def run_script():
    result = subprocess.run([
         'main.py'
    ],
   
    text=True)
    result = {'status': "success", "message": "Training complete"}
    return jsonify(result)
if __name__ == '__main__':
    app.run(port=5173, debug=True)
