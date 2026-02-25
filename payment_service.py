from flask import Flask, request, jsonify
import os

app = Flask(__name__)

SERVICE_ENV = os.getenv("SERVICE_ENV", "production")

@app.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "Payment Service Running",
        "environment": SERVICE_ENV
    })

@app.route("/process-payment", methods=["POST"])
def process_payment():
    data = request.get_json()

    user_id = data.get("user_id")
    amount = data.get("amount")

    if not user_id or not amount:
        return jsonify({"error": "Missing payment details"}), 400

    return jsonify({
        "message": f"Payment of ${amount} processed for user {user_id}",
        "env": SERVICE_ENV
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
