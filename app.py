from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return render_template('index.html')

# This is for local development
if __name__ == '__main__':
    app.run(debug=True)

# This is for Vercel
app = app
