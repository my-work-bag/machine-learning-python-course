
# Medium

https://www.freecodecamp.org/news/how-to-build-a-twitter-sentiment-analysis-tool/

# Twitter Sentiment Analysis

This application will get recent tweets on a certain topic and perform sentiment analysis.

## Getting Started

To install all Node packages run the following command. 
```
npm install
```

Create a Twitter Application and copy the API key and Secret in the `index.js` file.

You should set up a Google Platform, enable the Cloud Natural Language API, create a service account and store the service account private key in this directory in a file called `gcloud-private-key.json`

Use the `searchForTweets("Query")` function to get the sentiment score of recent tweets on that topic.

To start the application run the following command:
```
npm run start
```

Enjoy!

- A demo of this application [can be found here](https://coffeecoding.dev/twitter-sentiment-analysis)
- A detailed article on this tool [can be found here](https://www.freecodecamp.org/news/how-to-build-a-twitter-sentiment-analysis-tool/)