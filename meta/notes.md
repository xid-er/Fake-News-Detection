## Twitter API Elevated Access request

### How will you use the Twitter API or Twitter Data?

My dissertation project in my final year as an undergraduate University of Glasgow student is about using Natural Language Processing in Machine Learning to build a model that could tell fake and real news distributed on social media apart. As Twitter is a very widely used platform to spread misinformation by malicious users, I want to extract features from tweets that could be useful in building such a model, like the source text and the time they were posted. With this model, I plan to create a tool (so far the plan is for a website) for users to input the text or URL of a tweet to better understand whether that tweet is likely to be fake news, which would hopefully reduce the spread of misinformation on social media.

GitHub link: https://github.com/xid-er/Fake-News-Detection

### Please describe how you will analyze Twitter data including any analysis of Tweets or Twitter users.

I plan to extract specific features from tweets in the fake and real news-annotated dataset I have to build a machine learning model with BERT preprocessing and a Linear Regression model. The features will be: source text, creation time, user description and verification status.

### Please describe how and where Tweets and/or data about Twitter content will be displayed outside of Twitter.

The information about these tweets will be aggregated into the dataset analysis section of my dissertation, which may or may not be published in the end. The same data mentioned above will be analysed, but any usernames or other types of sensitive information will be removed from publication.


## Accuracy of new 200 Tweet-dataset (FakeNewsNet) by model

Dummy most frequent: 52.0%
Logistic Regression: 97.6%
SVC: 98.0%

## Accuracy of FakeNewsNet by model after splitting by group

Dummy Most-Frequent: 68.3% (+16.3%)
Logistic Regression: 71.7% (-25.9%)
SVC: 70.1% (-17.9%)

## Accuracy [F1 Score] of FakeNewsNet by model after fixing imbalance

Dummy most frequent: 49.5% (-18.8%) \[32.7%]
Logistic Regression: 68.0% (-3.7%) \[66.2%]
SVC: 61.4% (-8.7%) \[56.8%]

## F1 score of FakeNewsNet with BERT

0.986

## Other metrics:

## Dataset phrase analysis

Bill Gates:
* Fake: 608 / 108_930 (0.56%)
* Real: 44 / 296_170 (0.01%)

Trump:
* Fake: 23_161 (21.26%)
* Real: 59_694 (20.16%)

Clinton:
* Fake: 3049 (2.80%)
* Real: 8842 (2.99%)

Pelosi:
* Fake: 1295 (1.19%)
* Real: 1740 (0.59%)

Vaccine:
* Fake: 6040 (5.54%)
* Real: 568 (1.92%)