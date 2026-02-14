from flask import Flask, jsonify
import os
import psycopg2

app = Flask(__name__)

DATABASE_URL = os.environ.get("DATABASE_URL")

def get_connection():
    return psycopg2.connect(DATABASE_URL, sslmode="require")


@app.route("/")
def home():
    return "Service Restaurants Dakar actif ✅"


@app.route("/restaurants")
def get_restaurants():
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("""
            SELECT name, rating, reviews, price, distance, open, address
            FROM restaurants_dakar
        """)

        rows = cursor.fetchall()

        restaurants = []
        for r in rows:
            restaurants.append({
                "name": r[0],
                "rating": r[1],
                "reviews": r[2],
                "price": r[3],
                "distance": r[4],
                "open": r[5],
                "address": r[6]
            })

        cursor.close()
        conn.close()

        return jsonify(restaurants)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

