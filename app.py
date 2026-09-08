app.py
from flask import Flask, render_template, request
import sqlite3
from datetime import datetime

app = Flask(__name__)

def db():
    conn = sqlite3.connect("database.db")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS absen(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nama TEXT,
        waktu TEXT
    )
    """)
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/absen")
def absen():
    nama = request.args.get("nama")

    conn = db()
    conn.execute(
        "INSERT INTO absen(nama,waktu) VALUES(?,?)",
        (nama, datetime.now())
    )
    conn.commit()
    conn.close()

    return "Absen berhasil: " + nama
    @app.route("/admin")
def admin():
    conn = db()
    data = conn.execute(
        "SELECT * FROM absen ORDER BY id DESC"
    ).fetchall()
    conn.close()

    return render_template(
        "admin.html",
        data=data
    )

app.run(host="0.0.0.0", port=5000)
