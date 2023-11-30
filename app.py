from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["POST","GET"])
def index():
    if request.method == "POST":
        rate = float(request.form.get("rate"))
        print(rate)
        return(render_template("index.html",result=-50.60*rate + 90.22))
    else:
        return(render_template("index.html",result="waiting..........."))

if __name__ == "__main__":
    app.run()
