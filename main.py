from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')

# Services 
@app.route("/services")
def services():
    return render_template('services.html')

@app.route("/service_one")
def service_one():
    return render_template("service-one.html")

@app.route("/service_two")
def service_two():
    return render_template("service-two.html")

@app.route("/service_three")
def service_three():
    return render_template("service-three.html")


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
