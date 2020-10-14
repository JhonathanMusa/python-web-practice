from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.route("/services")
def services():
    return render_template('services.html')


@app.route("/products")
def products():
    return render_template("products.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


# to keep the server running and apply changes automatically
if __name__ == '__main__':
    app.run()
