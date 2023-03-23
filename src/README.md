# Fake-News-Detection

The presentation of the video can be accessed from here: https://mega.nz/file/Nq5ESL7L#nVj0fKLeQ5_RMyjmXFRYid3-6WJe8LQL43cGzWzqxnI.
Other files can also be accessed from GitHub: https://github.com/xid-er/Fake-News-Detection.

To see and use the product immediately, visit http://fakenewsuofg.pythonanywhere.com/. However, this production version is limited because of limited storage available on PythonAnywhere and other hosting platforms. Specifically, the more complex BERT model is not available on the live site, and trying to access it will show a warning message on the website. 

The file structure is as follows:
* `web\fnews\` contains a typical file structure for a Django-based web application, which contains:
    * `fnews\` contains the code for processing page information and making use of the models (`views.py`) and general application settings
    * `static\` contains the model and pre-processing files, jQuery, CSS, and images used in the web app
    * `templates\` contains the HTML for the pages in the web app
* `ML_twitter.ipynb` contains the code for training the BERT model
* `simple_model.ipynb` contains the code for training the Logistic Regression model
* `helpers.ipynb` contain useful functions used a few times for transforming the datasets, calling APIs, etc.
* `old_experiments.ipynb` contains code which was helpful for understanding the data, APIs, etc. involved during the development of the project

To get the full feature set, follow the instructions below:

## Instructions


### Requirements

For example:

* Python 3.10.8
* Packages: listed in `requirements.txt` 
* Tested on Windows 10

### Build and Run instructions

0. (optional) It is recommended to work in a virtual environment provided either by Anaconda, Python, or any other provider.
1. Download the complex model weights (`complex_model.sav`) from https://mega.nz/file/425hyRjb#Ja2YwEusdyK7ARv_n3Nvhcz6A0PJLE02FhcnQf4xBeI since it is 418 MB, which is too big for uploading to Moodle, and place it in `src/web/fnews/static/models/`.
2. Install the necessary libraries by running the command: `pip install -r requirements.txt`.
3. Go to the base directory of the web service (the one containing `manage.py`) with the `cd` command.
4. Run the server with the command: `python manage.py runserver`.
5. Voilà, the server should start running on your `localhost`.

### Data directory

The data for both _PHEME_ and _FakeNewsNet_ is available in MEGA.nz: https://mega.nz/folder/IiIzjB7L#L0f3nfJNf5osC4xYkbiQPQ.