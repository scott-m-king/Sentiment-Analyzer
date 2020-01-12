from flask import Flask, flash, jsonify, redirect, render_template, request

from nlp import analyze_entity_sentiment
from pipeline import process_search_data, bar_plot_scores

import mpld3

import os

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


searchterms = []


# Homepage
@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        searchterm = request.form.get("searchTerms")
        searchterms.clear()
        searchterms.append(searchterm)
        return redirect("/results")
    else:
        return render_template("index.html")


# Results page
@app.route('/results', methods=["GET", "POST"])
def results():
    entity_sentiment = analyze_entity_sentiment(str(searchterms[-1]))
    urls, sentiments = process_search_data(searchterms[0])

    urls = [str(url) for url in urls]
    sentiments = [round(sentiment, 1) for sentiment in sentiments]

    # fig = bar_plot_scores(sentiments)
    # mpld3.show(fig)

    return render_template("results.html", searchterm=searchterms[-1], sentiments=sentiments, urls=urls, counter=0)


if __name__ == '__main__':
    app.run()
