from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)

# Define your routes/views
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/error')
def error():
    return render_template('error.html')  # Assuming you have an 'error.html' file in your templates folder

# Custom 404 error handler
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('error'))

if __name__ == '__main__':
    app.run(debug=True)
