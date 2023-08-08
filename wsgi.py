from main import app, db


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(debug=False, port=5000, host='0.0.0.0')
