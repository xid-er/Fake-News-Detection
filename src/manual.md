Either visit http://fakenewsuofg.pythonanywhere.com/
or follow the following instructions:

0. (optional) It is recommended to work in a virtual environment provided either by Anaconda, Python, or any other provider.
1. Download the complex model weights (`complex_model.sav`) from https://mega.nz/file/425hyRjb#Ja2YwEusdyK7ARv_n3Nvhcz6A0PJLE02FhcnQf4xBeI since it is 418 MB, which is too big for uploading to Moodle, and place it in `src/web/fnews/static/models/`.
2. Install the necessary libraries by running the command: `pip install -r requirements.txt`.
3. Go to the base directory of the web service (the one containing `manage.py`) with the `cd` command.
4. Run the server with the command: `python manage.py runserver`.
5. Voilà, the server should start running on your `localhost`.