from flask import Flask, flash, jsonify, redirect, render_template, request

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


searchterms = []


# Homepage
@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        searchterm = request.form.get("searchTerms")
        searchterms.append(searchterm)
        print(searchterm)
        return redirect("/results")
    else:
        return render_template("index.html")


# Results page
@app.route('/results', methods=["GET", "POST"])
def results():
    print(searchterms)
    return render_template("results.html", searchterm=searchterms[-1])


if __name__ == '__main__':
    app.run()
