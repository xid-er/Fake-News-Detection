from django.shortcuts import render

import os
import pickle

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
        prediction = "Complex chosen (WIP)" # TODO
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