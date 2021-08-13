# Spam_Project_Phase_4
![alt text](https://github.com/EmmaChoate/Spam_Project_Phase_4/blob/main/images/spam_clipart.jpeg)

## Overview:
For this project, we used Natural Language Processing to predict whether or not an email is spam. 

## Business Problem:
Anyone who has an email knows how annoying spam is. As students at Birmingham Southern College, we know especially well how annoying they can be. Some spam emails are easy to spot, but as technology advances, the easier it is to fall victim to these emails. Given a data set with examples of spam and non-spam (ham) emails, we were tasked with being able to create a model to accurately detect if an email is spam or not.

## Data:
We used data from Kaggle.com and imported the spam.csv. This data is based the bodies of emails and contains the following information:
**Category:** Indicates whether or not the emails is spam or not
-	Ham is referred to as any email that is not spam
-	Spam emails are as we all know spam
**Message:** The body of the email not including the sender, signature, or attachments 

## Process:
We cleaned and processed the data to eliminate any unnecessary details such as unnecessary punctuation, stop words, capitalized letters, etc. This was achieved by creating a cleaning function that did all of the above in one step. Once the data was cleaned, we were able to stem the data and tokenize it in order to be able to run it through models to see how our data preformed. 

## Methods & Results:
We started by importing the necessary packages we needed to manipulate the data.  Then the first step we took was to use LabelEncoder() to create a binary target column where the “ham” messages were 0’s and the “spam” messages were 1’s.  Now that we established our target variable we set the index of the dataset to the category column so that the ham and spam would not disrupt the model.  Then we established a cleaning function that was able to remove the stop-words in each message, along with tokenizing and stemming each message.  We then removed the white space in the messages before we used the TfidfVectorizer() to Vectorize the messages.  Once the data was run through our tfidf function which established a train-test-split, vectorized the data, and returned test variables we were able to use our classify_text function to easily run our models on the vectorized data.  

Now elaborating on the created functions and some of the terminology used above.  Stop-words refers to all of the most common words used in the all languages, in our case English.  Therefore, when we removed stop-words this means that we removed words like: and, but, like, as, that, etc. The functions that are mentioned above were originally used as many steps in the notebook, but after some careful thinking and condensing the code we were able to just create three functions that did everything with a lot less coding.  

We used a Naïve Bayes Classifier and a Random Forest Classifier to model, the Naïve Bayes Classifier returned with a 96.69% accuracy score and an 85.88% f1 score.  The Random Forest Classifier returned with a 97.63% accuracy score and a 90.26% f1 score.  The accuracy score takes into account the total correct predictions that were made, so for example where the variable was actually a ham email and the model correctly predicted a ham email, and the same for spam then added together, and divided by the total number of predictions the model made.

![alt text](https://github.com/EmmaChoate/Spam_Project_Phase_4/blob/main/images/nb_confusion_matrix.png)


![alt text](https://github.com/EmmaChoate/Spam_Project_Phase_4/blob/main/images/rf_confusion_matrix.png)


For f1 score which is also referred to as precision-recall tradeoff which looks at all the times that an incorrect prediction was made, because it is just as important to make sure that an important email is not wrongly predicted as spam and the same goes for if a dangerous spam email that was wrongly predicted as an important email and sent directly into your inbox, this reasoning is why we prioritized f1 score.  

## Application and Deployment:
Once we established a working model and finalized our notebook, it was on to the deployment phase.  We created and application that was designed around corroboration with our notebook and the elements used inside that notebook.  We used a template Web-Page to establish the code where we edited what we needed to develop the app so that not only the page itself but the code of the app would take an email that is pasted into the cell and run that message through the code the same way the imported data was run through the code to provide an accurate answer of whether the message was spam or not.

![alt text](https://github.com/EmmaChoate/Spam_Project_Phase_4/blob/main/images/web_app_screenshot.png)


## Conclusions:
Looking at the project now that it is finished there are some key aspects that we would hope to be able to continue to work on like making the web application a back-end process where you never see the actual application, but instead it is established where when any email is sent to the account with this application attached to it; it is sent through the model first to determine whether that email is spam or not, if it is spam it is sent from the model to a spam folder, and if the email is not spam then it is sent directly into the receivers inbox.