from flask import Flask, jsonify
from flask_cors import CORS 
import subprocess
import sys

app = Flask(__name__)   
CORS(app)

@app.route("/runML", methods=['GET'])
def runML():
    try:
        # Run  supervised machine learning script
        result = subprocess.run([sys.executable, "..\models\main.py"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            return jsonify({
                "success": True,
                "output": result.stdout,
                "algorithms": ["random_forest"]
            })
        else:
            return jsonify({
                "success": False,
                "error": result.stderr
            })
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

@app.route("/runMLk", methods=['GET'])
def runMLk():
    try:
        # Run  unsupervised machine learning script
        result = subprocess.run([sys.executable, "..\models\knn.py"], 
                              capture_output=True, text=True)
        
        if result.returncode == 0:
            return jsonify({
                "success": True,
                "output": result.stdout,
                "algorithms": ["knn"]
            })
        else:
            return jsonify({
                "success": False,
                "error": result.stderr
            })
            
            
    except Exception as e:
        return jsonify({
            "success": False,
            "error": str(e)
        })

if __name__ == "__main__":
    app.run(debug=True, port=5000) 
