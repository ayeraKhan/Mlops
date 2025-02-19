from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Flask App Successfully Deployed on Vercel!"

if __name__ == "__main__":
    app.run()
