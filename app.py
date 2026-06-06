from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

data = {"balance": 1000.0}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/action', methods=['POST'])
def handle_action():
    action = request.json.get('action')
    amount = float(request.json.get('amount', 0))
    message = ""
    if action == 'deposit':
        if amount > 0:
            data['balance'] += amount
            message = f"✅ Deposited ${amount:.2f}."
        else:
            message = "⚠️ Invalid amount for deposit."
    elif action == 'withdraw':
        if amount <= 0:
            message = "⚠️ Invalid amount for withdrawal."
        elif amount > data['balance']:
            message = "❌ Insufficient funds."
        else:
            data['balance'] -= amount
            message = f"✅ Withdrawn ${amount:.2f}."
    elif action == 'check':
        message = "🔄 Balance refreshed."
    else:
        message = "❗ Unknown action."

    return jsonify({"balance": round(data['balance'], 2), "message": message})

if __name__ == '__main__':
    app.run(debug=True)
