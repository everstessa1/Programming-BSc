# Problem Set 6
# Name: Tessa Evers (#10550062)
# Time: 22:00
# analyzer.py: This script makes a class called Analyzer in which a list of positive and
# negative words is initialized in list. Afterwards this list is used
# to determine if a given text is in total positive, negative or neutral
# by analyzing each word in the given text.
#
# For running scripts the following key information is necessary
# export API_KEY=dGCFovgkdd8V4CE3gO5TmJfbf
# export API_SECRET=aBCodOi25Z19ERdkFx4Y2WF5OI4ERbCzjG5KB7dAM4gd8BXBqQ

# The following functions or librarys are necessary to run the script.
import nltk

class Analyzer():

    """Implements sentiment analysis."""


    def __init__(self, positives, negatives):

        """Initialize Analyzer."""

        self.setpositive = self.load(positives)
        self.setnegative = self.load(negatives)

    def load(self, file):

        """Open file with given key, strip every word in file and add it to a list."""

        list_of_file = []
        with open(file) as f:
            for word in f:
                if not word.startswith(";"):
                    stripped_word = word.rstrip('\n')
                    list_of_file.append(stripped_word)
        f.close()
        return list_of_file

    def analyze(self, text):

        """Analyze text for sentiment, returning its score."""

        # Use Tweet Tokenizer to split tweet into words
        tokenizer = nltk.tokenize.TweetTokenizer()
        tweet_split = tokenizer.tokenize(text)

        # Transform whole tweet to lower cases.
        tweets_lower = [word.lower() for word in tweet_split]

        # Make variable names for calculating the score.
        positive_points = 0.0
        negative_points = 0.0
        neutral_points = 0.0

        # Check if word in tweet coincides with positive, negative or neutral words.
        for word in tweet_split:
            if word in self.setpositive:
                positive_points += 1
                print(positive_points)
            elif word in self.setnegative:
                negative_points += 1
                print(negative_points)
            else:
                neutral_points += 1
        score_tweet = positive_points - negative_points
        return score_tweet
