from flask import Flask, flash, jsonify, redirect, render_template, request

from nlp import analyze_entity_sentiment

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


searchterms = []
socialmedias = []

page_data = {'search_terms': [],
             'social_medias': []}


# Homepage
@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        search_term = request.form.get("searchTerms")
        page_data['search_terms'].append(search_term)
        social_media = request.form.get("socialMedia")
        page_data['social_media'].append(social_media)
        return redirect("/results")
    else:
        return render_template("index.html")


# Results page
@app.route('/results', methods=["GET", "POST"])
def results():
    entity_sentiment = analyze_entity_sentiment(str(page_data['search_terms'][-1]))
    sentiments = sorted(entity_sentiment.entities[:8], key=lambda s: s.salience, reverse=True)

    sentiment_names = [sentiment.name for sentiment in sentiments]
    sentiment_saliences = [sentiment.salience for sentiment in sentiments]
    sentiment_scores = [sentiment.sentiment.score for sentiment in sentiments]
    sentiment_magnitude = [sentiment.sentiment.magnitude for sentiment in sentiments]

    return render_template("results.html", searchterm=searchterms[-1], socialmedia=socialmedias[-1],
                           sentiment_names=sentiment_names, sentiment_saliences=sentiment_saliences,
                           sentiment_scores=sentiment_scores, sentiment_magnitude=sentiment_magnitude)


if __name__ == '__main__':
    app.run()
