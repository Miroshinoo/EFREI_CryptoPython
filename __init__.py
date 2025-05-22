from flask import Flask, render_template, request
from cryptography.fernet import Fernet

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("crypto.html")

@app.route("/generate_key")
def generate_key():
    key = Fernet.generate_key().decode()
    return {"key": key}

@app.route("/encrypt-form", methods=["POST"])
def encrypt_form():
    key = request.form["key"]
    message = request.form["message"]

    try:
        fernet = Fernet(key.encode())
        encrypted_message = fernet.encrypt(message.encode()).decode()
        return render_template("crypto.html", encrypted_result=encrypted_message)
    except Exception as e:
        return render_template("crypto.html", encrypted_result=f"Erreur : {e}")

@app.route("/decrypt-form", methods=["POST"])
def decrypt_form():
    key = request.form["key"]
    encrypted_message = request.form["message"]

    try:
        fernet = Fernet(key.encode())
        decrypted_message = fernet.decrypt(encrypted_message.encode()).decode()
        return render_template("crypto.html", decrypted_result=decrypted_message)
    except Exception as e:
        return render_template("crypto.html", decrypted_result=f"Erreur : {e}")

if __name__ == '__main__':
    app.run(debug=True)
