from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Homepage
@app.route('/')
def hello_world():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
