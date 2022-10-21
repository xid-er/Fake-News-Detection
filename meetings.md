# Meetings

## 30 Sep 2022

First intro meeting
Discussion points pre-meeting:
* What day to meet?
* Scope of the project?
* Task management tool: is Trello okay?
* Many models already trained, what else can be contributed model training-wise? (discuss research opportunities mentioned in *Oliveira et al.*)
* Programming language for model-training: Python?
* The tool itself (after the model's been trained): website? Input: **URL** (more usable but might be biased towards/against websites) or **text input** (less usable but more focused on the content)?

Discussion results:
* Each next meeting will be scheduled during previous meeting, next at 2:30 pm on Friday
* Meeting minutes should be sent right after the meeting, but work done should be sent every week, preferably day before meeting (can be day of)
* The project consists of two parts: 1) building an NLP model to detect fake news, and 2) creating a tool for users to access this model and make use of it
* * The model will be made in Python, with a topic-specific dataset first to start off with an easier model, which can then be made more general. First topic ideas: COVID, climate change. The dataset might be even more specialised to only include posts from specific social media, e.g., Tweets from Twitter. Additional complexity/topic for novel research might be turning emojis into text to include them as a feature in the model.
* * The tool should be something more or less accessible to non-techy users, i.e., not a command-line interface, but a simple Django web app (to-do: research possibly more accessible tool - browser extension)
* Trello board is made and shared (to-do: link it in email)
* Most immediate task: research datasets to find topic-specific and website-specific ones


## 7 Oct 2022

Discussion points in meeting:
* Discussed what sort of datasets to start with:
* * Twitter vs. Facebook: each has their benefits and drawbacks, but decided to use Twitter dataset because post lengths are more uniform, which will make it easier/more trustworthy to work with the dataset
* * Size of the dataset: start with smaller Twitter dataset with binary truth classification to make the work faster at first; afterwards, possible to sample larger dataset of sample sizes equal to smaller dataset to compare results: maybe the difference won't be that dramatic. Additionally, possible to take extreme ends of the n-ary truth classification of the larger dataset or to group them to convert to a binary classification.
* Discussed accessibility of the tool (Django website vs. browser extension): decided to continue with the Django website idea because many non-techy Internet users don't even know about the existence of browser extensions, and they are the ones who need the tool the most
* Found the emails that we thought were lost in the vast desert of email-verse
* Most immediate task: create a model using the small Twitter dataset


## 14 Oct 2022

Before meeting:
* Any advice on tokenisation considerations?
* * Try many methods, compare and see which ones are most useful
* * Speed vs f1-score/accuracy
* How to host the website/REST API?
* * Free online sources: Python Anywhere
* Thoughts on initial performance of models before tokenisation & fine-tuning / using BERT and more advanced models?

Meeting notes:
* Discussed results of the performance by models made and trained during the week: good results for a start, especially for comparison with a Dummy Classifier. Naturally, more work to be done to improve these results by fine-tuning, tokenisation, and using better models and bigger datasets.
* Regarding the end-tool, might be useful to let the user choose what kind of model to use to predict the truth of the text they input
* Ideally, final model will use a much bigger dataset and a more complex model like BERT, which is much more suitable for NLP
* Immediate tasks: look into tokenisation, start with the bigger dataset first, then try and integrate BERT.


## 21 Oct 2022

Before meeting:
