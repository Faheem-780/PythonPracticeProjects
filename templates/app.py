from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Initializing balance
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
            message = f"Ching Chang🤑! Successfully deposited ${amount}"
        else:
            message = "Warning⚠️! Invalid amount."
            
    elif action == 'withdraw':
        if amount > data['balance']:
            message = "Insufficient funds❗"
        elif amount <= 0:
            message = "Invalid Amount❗"
        else:
            data['balance'] -= amount
            message = f"Hurray🎉! Withdrawn ${amount}"
            
    return jsonify({"balance": data['balance'], "message": message})

if __name__ == '__main__':
    app.run(debug=True)