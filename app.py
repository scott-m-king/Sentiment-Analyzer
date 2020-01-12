from flask import Flask, flash, jsonify, redirect, render_template, request

from nlp import analyze_entity_sentiment

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


searchterms = []
socialmedias = []


# Homepage
@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        searchterm = request.form.get("searchTerms")
        socialmedia = request.form.get("socialMedia")
        searchterms.append(searchterm)
        socialmedias.append(socialmedia)
        print(searchterm)
        return redirect("/results")
    else:
        return render_template("index.html")


# Results page
@app.route('/results', methods=["GET", "POST"])
def results():
    print(searchterms[-1])
    entity_sentiment = analyze_entity_sentiment(str(searchterms[-1]))
    print('got here')
    sentiments = sorted(entity_sentiment.entities[:8], key=entity_sentiment.salience)
    print('got here also')

    sentiment_names = [sentiment.name for sentiment in sentiments]
    sentiment_saliences = [sentiment.salience for sentiment in sentiments]
    sentiment_scores = [sentiment.sentiment.score for sentiment in sentiments]
    sentiment_magnitude = [sentiment.sentiment.magnitude for sentiment in sentiments]
    print(sentiment_names)
    print(sentiment_saliences)
    print(sentiment_scores)
    print(sentiment_magnitude)

    return render_template("results.html", searchterm=searchterms[-1], socialmedia=socialmedias[-1])


if __name__ == '__main__':
    app.run()
