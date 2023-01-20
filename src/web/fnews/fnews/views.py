from django.shortcuts import render

import os
import re
import pickle
import tweepy
import pandas as pd
from dotenv import load_dotenv

# our home page view
def home(request):    
    return render(request, 'index.html')

def get_prediction(src_text, model_type):
    module_dir = os.path.dirname(__file__)  # get current directory
    static_path = os.path.join(module_dir, '..', 'static')

    if model_type == 'simple_model':
        model_path = os.path.join(static_path, 'models', 'simple_model.sav')
        preprocessing_path = os.path.join(static_path, 'preprocessing', 'tfidf_vectorizer.sav')

        model = pickle.load(open(model_path, "rb"))
        #scaler = pickle.load(open("scaler.sav", "rb"))
        preprocessing = pickle.load(open(preprocessing_path, "rb"))

        feature = preprocessing.transform([src_text])

        #prediction = model.predict(scaler.transform(request.data))
        prediction = model.predict(feature)[0]

    elif model_type == 'complex_model':
        load_dotenv()
        api_key = os.environ.get('APIKey')
        api_key_secret = os.environ.get('APIKeySecret')
        access_token = os.environ.get('AccessToken')
        access_token_secret = os.environ.get('AccessTokenSecret')
        bearer_token = os.environ.get('BearerToken')

        client = tweepy.Client(
            consumer_key=api_key, 
            consumer_secret=api_key_secret,
            access_token=access_token, 
            access_token_secret=access_token_secret,
            bearer_token=bearer_token, 
            wait_on_rate_limit=True,
        )

        # auth = tweepy.OAuth1UserHandler(
        #     api_key, api_key_secret, access_token, access_token_secret
        # )
        # client = tweepy.API(auth)

        tweet_id = re.findall('\d+', src_text)[0]
        response = client.get_tweets(
            tweet_id, 
            tweet_fields=
                ["created_at", "text", "lang", "author_id", "source"],
            user_fields=
                ["location", "description", "verified"],
            expansions="author_id"
        )
        print(response)
        #tweets_dict = response.json()

        fields = ['id', 'text', 'author_id', 'source', 'created_at', 'edit_history_tweet_ids', 'lang', 'description', 'username', 'verified', 'name', 'location']

        tweet_data = response.data[0] # can fail if nans in Tweets
        user_data = response.includes['users'][0]

        print("tweet:",tweet_data)
        print("user:",user_data)

        combined = ""
    
        combined += f"I created this Tweet at {tweet_data.created_at} o'clock " + \
            f"in the {tweet_data.lang} language and in {user_data.location} " + \
            f"from {tweet_data.source}. "
            
        verification_status = "verified" if user_data.verified else "not verified"
        combined += f"My name is {user_data.name}, username is {user_data.username} " + \
            f"and I am {verification_status}. "
        
        combined += f"I would describe myself as {user_data.description}. "
        
        combined += f"I wrote: {tweet_data.text} "
        prediction = combined

    else:
        prediction = "No valid algorithm chosen"
        

    return prediction

def result(request):
    # model_type = request.GET['model_1']

    print(request.GET)

    # print(model_type)
    # print(request.GET['model_2'])
    # print(request.GET['model_select'])
    # print(request.GET['option1'])
    # print(request.GET['option2'])
    model_type = None
    src_text = request.GET['src_text']
    model_type = request.GET['model_select']
    print(model_type)

    prediction = get_prediction(src_text, model_type)

    return render(request, 'prediction.html', {'prediction':prediction})