from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt/", methods=["POST"])
def caesar_encrypt():
    data = request.json or {}
    plain_text = data.get('plain_text')
    key = data.get('key')

    if plain_text is None or key is None:
        return jsonify({"error": "Missing 'plain_text' or 'key'"}), 400

    key = int(key)
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})


@app.route("/api/caesar/decrypt/", methods=["POST"])
def caesar_decrypt():
    data = request.json or {}
    cipher_text = data.get('cipher_text')
    key = data.get('key')

    if cipher_text is None or key is None:
        return jsonify({"error": "Missing 'cipher_text' or 'key'"}), 400

    key = int(key)
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({"decrypted_text": decrypted_text})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
