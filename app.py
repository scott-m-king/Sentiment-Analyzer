from flask import Flask, flash, jsonify, redirect, render_template, request

from nlp import analyze_entity_sentiment
from pipeline import *

import mpld3

import os

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


searchterms = []


# disable caching
@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    r.headers['Cache-Control'] = 'public, max-age=0'
    return r


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
    urls_social_media, sentiments_social_media = process_search_data(searchterms[0], source='social_media')
    urls_news_feed, sentiments_news_feed = process_search_data(searchterms[0], source='news_feed')

    urls = urls_social_media + urls_news_feed
    sentiments = sentiments_social_media + sentiments_news_feed

    urls = [str(url) for url in urls]
    sentiments = [round(sentiment, 1) for sentiment in sentiments]

    mean = round(bar_plot_scores(sentiments), 1)
    pie_plot_scores(sentiments)

    cleanup_static_folder()

    return render_template("results.html",
                           searchterm=searchterms[-1],
                           sentiments=sentiments,
                           urls=urls,
                           counter=0,
                           mean=mean,
                           bar_filename=bar_plot_most_recent_filename(),
                           pie_filename=pie_plot_most_recent_filename())


if __name__ == '__main__':
    app.run()
