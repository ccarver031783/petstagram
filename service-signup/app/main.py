from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    email = data.get("email", "placeholder@example.com")

    # Basic validation
    if not username or not password:
        return jsonify({
            "status": "error",
            "message": "Username and password are required."
        }), 400

    # Simulate storing user
    print(f"New signup: {username}, {email}")

    return jsonify({
        "status": "success",
        "username": username,
        "email": email
    }), 200

@app.route('/signup', methods=['GET'])
def signup_form():
    return '''
    <h2>Signup Page</h2>
    <form method="POST" action="/signup">
      Username: <input name="username"><br>
      Password: <input name="password" type="password"><br>
      Email: <input name="email"><br>
      <button type="submit">Sign Up</button>
    </form>
    '''



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
