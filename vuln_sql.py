import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/user")
def get_user():
    username = request.args.get("username", "")
    # ❌ Vulnerable: unsanitized string concatenation into SQL
    query = f"SELECT * FROM users WHERE username = '{username}'"
    conn = sqlite3.connect("app.db")
    cur = conn.cursor()
    cur.execute(query)         # Expect SAST to flag injection sink here
    return {"ok": True}
