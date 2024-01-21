# Problem Set 6
# Name: Tessa Evers (#10550062)
# Time: 22:00
# application.py: This script creates a  chart based on a positive, negative and neutral percentage.
#
# For running scripts the following key information is necessary
# export API_KEY = dGCFovgkdd8V4CE3gO5TmJfbf
# export API_SECRET = aBCodOi25Z19ERdkFx4Y2WF5OI4ERbCzjG5KB7dAM4gd8BXBqQ

# The following functions or librarys are necessary to run the script.
from flask import Flask, redirect, render_template, request, url_for

import helpers
import os
import sys
from analyzer import Analyzer


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/search")
def search():

    # Validate the screen_name.
    screen_name = request.args.get("screen_name", "")
    if not screen_name:
        return redirect(url_for("index"))

    # It get screen_name's 100 recent tweets.
    tweets = helpers.get_user_timeline(screen_name,100)

    # The absolute paths to lists.
    positives = os.path.join(sys.path[0], "positive-words.txt")
    negatives = os.path.join(sys.path[0], "negative-words.txt")

    # Instantiates analyzer.
    analyzer = Analyzer(positives, negatives)

    # Make variable names for calculating the score.
    positive = 0.0
    negative = 0.0
    neutral = 0.0

    # Determine the score for the chart.
    for tweet in tweets:
        score = analyzer.analyze(tweet)
        if score > 0.0:
            positive += 1
        elif score < 0.0:
            negative += 1
        else:
            neutral += 1

    # Generate the chart.
    chart = helpers.chart(positive, negative, neutral)

    # Render the results.
    return render_template("search.html", chart=chart, screen_name=screen_name)
