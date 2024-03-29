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
* How come BERT is worse? Haven't looked into it yet
* Next task: Look into using the bigger dataset

Meeting notes:
* When reporting results, take mean of multiple runs
* * Also when comparing models (but keep split of train-test consistent)
* Look into splitting bigger dataset by topic, start with topic-specific models (possible approach: filter by mentioned keywords, like "climate change", etc)
* Investigate emojis and how they could disguise fake news (could (preferable to) replace with written meaning to use in the model)
* Instead of following gut feelings, test different approaches (features like author (weighted less than text?), date & time (don't forget about timezones), location, etc)
* Immediate task: import bigger Twitter dataset, try to filter it by topic, apply BERT to it


## 28 Oct 2022

Before meeting:
* Is the article-focused dataset okay?
* What to do with links?
* Include gossip cop or not?

Meeting notes:
* A lot of work done on the datasets, and that is completely expected and understandable (on average, 60% of work goes into dataset analysis)
* Regarding the two sources of data in dataset: use PolitiFact (politics-focused posts) first, then try Gossip Cop (celebrity-focused posts) only, then combine in a single model
* Regarding the presence of a (shortened) link to a news article in every Tweet in the dataset: Try removing the link first, but it might be important to include it as a point of data. Basically, experiment with both.
* Regarding the problem with representation of real and fake posts: real posts are almost 3x as many as fake ones. Solution: filter real posts by a weight according to how many fake posts there are. Other alternatives: duplicate the fake ones randomly to have more of them; or train the model with weights that represent the unequal proportion.
* Most immediate task: fetch and store Twitter data, apply BERT and Logistic Regression if there's time


## 4 Nov 2022

Before meeting:
* How to avoid/reduce bias against people (political ideology, race, etc.) arising from features (user location, description, etc.)?
* General dissertation discussion points (if applicable to supervisor): literature review, talking about bias, **research question**?

Meeting notes:
* If models take too long on laptop, building models with university-owned GPUs on stlinux-11 and stlinux-12 is possible. I'll start with laptop first, then try Google Colab, and if both are too slow, I'll let you know about the need for the university-owned servers.
* Good to start with limited number of real news Tweets (big enough number, similar representation to fake Tweets)
* Leave in the user descriptions as features because they are very useful pieces of information; regarding location, try with and without
* Narrowing dissertation research question to Twitter specifically (motivation: similar input text length, accessible API)
* It is alright to talk about bias and discuss possibilities to mitigate it, also talk about dataset makers and my own bias
* Lit review: summarise, read low double-figure amount fully, skim-read unimportant ones
* Immediate task: build model with dataset with one feature (text) (BERT-processed), then add more features (as mentioned)


## 14 Nov 2022

Before meeting:
* How to explain the incredible results?
* Can I start working on the Django website, or should I improve the model to include other features?

Notes:
* In order to fix the literally incredible results, group Tweets by article (dataset is already ordered by article) and randomly put into train/test sets until the Tweets are roughly 50/50. Additionally, implement the previously discussed method (weighted filtering) to make real Tweets less representative (to equal the representation of fake Tweets).
* In order to improve performance, research CUDA and look into how to use it on the laptop to utilise the GPU. If it takes too much time setting up, use Google Colab or university servers.
* Regarding general focus, have believable/trustworthy results first (80-90%), then focus more on the software development part of it.
* Immediate task: first bullet point (to not have the same article in both sets)


## 21 Nov 2022

Before meeting:
* Am I right in saying that these results (71%) are better than previous (98%) because they're more believable and there is room for much growth?
* With Twitter possibly breaking down because of Musk, should I be relying on the API for the tool?
* How okay is it to narrow down 

Notes:
* Twitter collapsing because of Musk and possibly ending the usefulness of the further use of the project - not the point of the project. The project is about the research and work that goes into developing the model(s) and the tool, so it's okay since the dataset is there.
* The code of the project is open-source, so there are no problems with continuing in the future if I ever want.
* Fix imbalanced data (easiest and most immediate to hardest): 1) get rid of random real Tweets (by actually just taking enough out to use) (don't get rid of whole articles), 2) generate fake ones with BERT (from the ones I've got), 3) GANs
* For Twitter API possibly breaking, keep old model just in case as backup, but develop better model with more features to use alongside Twitter API in the tool. Talk about Twitter breaking 2FA in dissertation as a precedence for the concern of API failing.
* In terms of increasing features used and thus narrowing the models down to be more Twitter-specific, it is okay to do so because that is the dataset I have and a big part of the project is the research of the dataset and how to include multiple features in a model.
* Most immediate tasks: 1) fix imbalance (methods in order of ease), 2) apply BERT, 3) increase features used (username, user description, etc.)


## 28 Nov 2022

Notes:
* Look into confusion matrices and how to fix their imbalance by, e.g., researching the cut-off point
* Start doing BERT, keeping in mind skewed confusion matrices


## 13 Jan 2023

Notes:
* Text-only/Unimodal model with multiple features is okay to continue to work on, no need to worry about weights of the features, but investigation option: don't put full sentences for features, just say the feature (like "not verified" instead of "I am not verified").
* Will write the dissertation while working on code (rest from one by working on the other), but dissertation progress is satisfactory.
* Most immediate tasks: Finish unimodal model, put into website, then include Twitter API and submit on PythonAnywhere.


## 20 Jan 2023

Notes:
* Try setting up a venv in stlinux-11/12 and see if I can use CUDA to GPU-accelerate training
* Able to look through lit review (earlier the better)


## 27 Jan 2023

Before meeting:
* High F1 score
* Background - literature review + explanations?
* Complex model size is half a gigabyte. Any other options than PythonAnywhere?
* Models seem to not do well with current fake news, but that's understandable right?

Notes:
* To check why the model works with only certain recent fake news (like the Bill Gates one), look into certain phrases that appear in the dataset and whether they might influence the accuracy of the model for recent fake news.
* To better understand the F1 score, look at accuracy and confusion matrix (and the text behind the wrongly classified Tweets) of the model. Should do by hand to truly understand.
* If PythonAnywhere is too small of a storage space to host the weights of the complex model, ask school support if I can host there. Hopefully, 512 MBs will be enough with the complex model being 422 MBs.
* Topics that can be added in literature review: classification in general (semantic, e.g., depression example by the other student), machine learning (tailor to average Computer Scientist).
* Since the focus of the project has mainly been to build the best model, the dissertation should focus more on research and background, not the tool, which is why most research papers also do not mention the practical aspect of their model. Can write about this in the dissertation.


## 3 Feb 2023

Before meeting:
* Any look through background section for dissertation?
* What to do if part of my dataset is in other languages?
* What to do about my complex model being the standard BERT?

Notes:
* Regarding dissertation: You said that you'll get around to reading the background section of my dissertation soon, maybe even this afternoon.
* Regarding the confusion matrix: It is not surprising that the errors are quite skewed towards mislabelling real news, especially because 1) the test dataset is skewed itself (more real than fake), and 2) it is not uncommon in other research either. Generally, an impressive confusion matrix which should be improved even more by percentages/balance.
* Regarding phrases in dataset: it makes sense for less popular topics (like 'Pelosi' and 'Bill Gates') to be spoken more by one group than for more popular topics (like 'Trump' and 'Clinton'), which are discussed by both real and fake news.
* Regarding foreign languages apparent in dataset: If I have time to leave my laptop running to train the model again from scratch, throw away the other languages. Otherwise, keep them. In either case, discuss in dissertation (as either dataset operations or limitations).
* Regarding BERT not being 'latest and greatest': That's not what the project is about, it's more about research and writing about learning (and the process), so I shouldn't worry so much about not using the best model. Also because BERT is already great.


## 24 Feb 2023

Notes:
* Regarding mentioning someone as a source for the opinion about the distribution of work in a data analytics project: I will find an original source to avoid mentioning you in that part
* Regarding the diagram: separate saved model weights into 2 not to confuse two ML models (actual) with hybrid ML model (apparent)
* Regarding the (now standardised) confusion matrix: add up to 1 for true labels OR leave as numbers for easier analysis.


## 3 Mar 2023

Notes:
* Think about adding more visual representation, especially between big text sections
* Diagram is fine now
* Bibliography: 3 pages is fine, alphabetical is fine
* Immediate tasks: Write abstract, host website on PythonAnywhere (and add pictures of it in dissertation), emphasise over-fitting in Conclusion, keep uppercase letters in Bibliography


## 10 Mar 2023

Notes:
* Suggestions for figures to add to dissertation: confusion matrix for Logistic Regression (would be a great/necessary addition), sigmoid (optional)
* Add an explanation to Evaluation section why the model might be over-fitted: 140 vs 280 Twitter character limit, different political topics, phrase analysis as in Appendix
* Immediate tasks: Remove BERT from production website (put link to repo), improve dissertation as previously mentioned (figures, over-fitting explanation) 