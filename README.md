# SpeechTox

SpeechTox is an application which detects toxicity of words used in a content. It is developed using HTML, CSS, JS and Django, and integrates a Machine Learning model.  

The machine learning model has been trained on the following [Kaggle dataset](https://www.kaggle.com/c/jigsaw-toxic-comment-classification-challenge). The application is used to predict the following categories given any text: toxic, severe_toxic, obscene, threat, insult and identity_hate. The model is trained using Logistic Regression.  

The application serves the following purposes:

1. Given any text, it lists the categories of language content it fits in.
2. Given a song title and artist, it again displays the categories of language content it fits in.
3. Given a billboard playlist and number of items, it classifies the songs in the playlist into two categories: decent and indecent.
