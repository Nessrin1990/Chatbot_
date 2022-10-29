# Samsung-Chatbot
using deep learning keras and flask
Here are the 5 steps to create a chatbot in Python from scratch:

    Import and load the data file
    Preprocess data
    Create training and testing data
    Build the model
    Predict the response
    
1. Import and load the data file:
                          First, make a file name as train_chatbot.py. We import the necessary packages for our chatbot and initialize the variables we will use in our Python project. The data file is in JSON format so we used the json package to parse the JSON file into Python.
2. Preprocess data:
                  When working with text data, we need to perform various preprocessing on the data before we make a machine learning or a deep learning model. Based on the requirements we need to apply various operations to preprocess the data. Tokenizing is the most basic and first thing you can do on text data. Tokenizing is the process of breaking the whole text into small parts like words. Here we iterate through the patterns and tokenize the sentence using nltk.word_tokenize() function and append each word in the words list. We also create a list of classes for our tags. Now we will lemmatize each word and remove duplicate words from the list. Lemmatizing is the process of converting a word into its lemma form and then creating a pickle file to store the Python objects which we will use while predicting.
3. Create training and testing data
                  Now, we will create the training data in which we will provide the input and the output. Our input will be the pattern and output will be the class our input pattern belongs to. But the computer doesn’t understand text so we will convert text into numbers.
 4. Build the model
                  We have our training data ready, now we will build a deep neural network that has 3 layers. We use the Keras sequential API for this. After training the model for 200 epochs, we achieved 100% accuracy on our model. Let us save the model as ‘chatbot_model.h5’.
 5. Predict the response 
                   To predict the sentences and get a response from the user to let us create a new file ‘chatapp.py’. create html (present in templates file) for front end. To connect with html we use flask web framework to connect our model with html.
 6. Run the chatbot
          To run the chatbot, we have one main file- python app.py. If we don’t see any error during training, we have successfully created the model. TThe program will open up a local host window within a few seconds. With the help of html front end, you can easily chat with the bot.
          
Output of the chatbot is shown in the chatbot.png file in the above.


 ![image](https://user-images.githubusercontent.com/69139140/120199393-d14b4a80-c240-11eb-89a4-6a793334f36c.png)

                
