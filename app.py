from flask import Flask, request, jsonify, abort

app = Flask(__name__)

# ✅ Allow only GET and POST
@app.before_request
def limit_methods():
    if request.method not in ['GET', 'POST']:
        abort(405)

# ✅ Defined endpoint
@app.route("/profile/status", methods=["GET", "POST"])
def profile_status():
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
    # Normally you'd use `flask run`, but here we will run via Hypercorn for HTTP/2
    app.run()
