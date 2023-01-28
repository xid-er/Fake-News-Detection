from django.shortcuts import render

import os
import re
import pickle
import tweepy
import pandas as pd
import numpy as np
from dotenv import load_dotenv

import torch
from transformers import BertTokenizer

# our home page view
def home(request):    
    return render(request, 'index.html')

def get_prediction(src_text, model_type):
    module_dir = os.path.dirname(__file__)  # get current directory
    static_path = os.path.join(module_dir, '..', 'static')

    if model_type == 'simple_model':
        valid_source = True
        source = src_text
        model_path = os.path.join(static_path, 'models', 'simple_model.sav')
        preprocessing_path = os.path.join(static_path, 'preprocessing', 'tfidf_vectorizer.sav')

        model = pickle.load(open(model_path, "rb"))
        #scaler = pickle.load(open("scaler.sav", "rb"))
        preprocessing = pickle.load(open(preprocessing_path, "rb"))

        feature = preprocessing.transform([src_text])

        prediction = model.predict(feature)[0]

    elif model_type == 'complex_model':
        model_path = os.path.join(static_path, 'models', 'complex_model.sav')
        model = pickle.load(open(model_path, "rb"))

        sentence = fetch_tweet(src_text)
        if sentence == "no data":
            return False, None, "It seems that the Tweet has been removed."
        elif sentence == "no link":
            return False, None, "That does not seem to be a valid link to a Tweet."
        else:
            valid_source = True

        source = sentence
        print(sentence)

        tokenizer = BertTokenizer.from_pretrained('bert-base-uncased', do_lower_case=True)
        encoded_dict = tokenizer.encode_plus(
                        sentence,                      # Sentence to encode.
                        add_special_tokens = True, # Add '[CLS]' and '[SEP]'
                        max_length = 480,           # Pad & truncate all sentences.
                        truncation = True,
                        padding = 'max_length',
                        return_attention_mask = True,   # Construct attn. masks.
                        return_tensors = 'pt',     # Return pytorch tensors.
                )

        print(encoded_dict)

        # Add the encoded sentence to the list.    
        input_ids = encoded_dict['input_ids']
        
        # And its attention mask (simply differentiates padding from non-padding).
        attention_mask = encoded_dict['attention_mask']

        # Convert the lists into tensors.
        input_ids = torch.tensor(input_ids)
        attention_mask = torch.tensor(attention_mask)

        with torch.no_grad():
            # Forward pass, calculate logit predictions.
            result = model(input_ids.cuda(), 
                            token_type_ids=None, 
                            attention_mask=attention_mask.cuda(),
                            return_dict=True)

            logits = result.logits

            # Move logits and labels to CPU
            prediction = logits.detach().cpu().numpy()

            prediction = True if np.argmax(prediction, axis=1).flatten()[0] == 1 else False

    else:
        prediction = "No valid algorithm chosen"

    if prediction is True:
        prediction = "Real News"
    else:
        prediction = "Fake News"

    return valid_source, source, prediction

def result(request):
    print(request.GET)

    model_type = None
    src_text = request.GET['src_text']
    model_type = request.GET['model_select']
    print(model_type)

    valid_source, source, prediction = get_prediction(src_text, model_type)

    return render(
        request, 
        'prediction.html', 
        {
            'valid_source': valid_source, 
            'source': source,
            'prediction':prediction
        })


def fetch_tweet(link):
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

    regex_numbers = re.findall('/status/(\d+)', link)
    if len(regex_numbers) == 0:
        return "no link"
    tweet_id = regex_numbers[0]
    print("Searching tweet with ID", tweet_id)

    response = client.get_tweets(
        tweet_id, 
        tweet_fields=
            ["created_at", "text", "lang", "author_id", "source"],
        user_fields=
            ["location", "description", "verified"],
        expansions="author_id"
    )
    print(response)
    if response.data is None:
        return "no data"

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

    return combined