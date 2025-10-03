from flask import Flask, request, jsonify, abort
import logging

app = Flask(__name__)

# Setup basic logging
logging.basicConfig(level=logging.INFO)

# ✅ Allow only GET and POST
@app.before_request
def limit_methods():
    if request.method not in ['GET', 'POST']:
        abort(405)

# ✅ Defined endpoint
@app.route("/profile/status", methods=["GET", "POST"])
def profile_status():
    if request.method == "POST":
        # Log method, path, headers, and body
        logging.info(f"POST request received:")
        logging.info(f"Path: {request.path}")
        logging.info(f"Headers: {dict(request.headers)}")
        logging.info(f"Body: {request.get_data(as_text=True)}")
    return jsonify({"message": "OK"}), 200

# ✅ Undefined routes → 404
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": "Not Found"}), 404

# ✅ Handle wrong methods
@app.errorhandler(405)
def method_not_allowed(e):
    return jsonify({"error": "Method Not Allowed"}), 405

if __name__ == "__main__":
    app.run()
