
import nltk

def format_sentence(sent):
  return({word: True for word in nltk.word_tokenize(sent)})

print(nltk.word_tokenize("The cat is very cute"))

total = open('/content/drive/My Drive/Colab Notebooks/Projects/20200602_Twitter_Sentiment_Analysis/pos_tweets.txt')
X_pos = list()
y_pos = list()
#word tokenization
for sentence in total:
  #print(sentence)
  X_pos.append([format_sentence(sentence)])
  y_pos.append(0)
  #saves the sentence in format: [{tokenized sentence}, 'pos]
#X_pos


total = open('/content/drive/My Drive/Colab Notebooks/Projects/20200602_Twitter_Sentiment_Analysis/pos_tweets.txt')
X_neg = list()
y_neg = list()
#word tokenization
for sentence in total:
  #print(sentence)
  X_neg.append([format_sentence(sentence)])
  y_neg.append(1)
  #saves the sentence in format: [{tokenized sentence}, 'pos]
#X_neg

X_pos[0]


X = X_pos + X_neg
y = y_pos + y_neg
print(len(X), len(y))

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
print(len(X_train), len(X_test), len(y_train), len(y_test))




from sklearn.linear_model import SGDClassifier
clf = SGDClassifier()
clf.fit(X_train, y_train)
train_score = clf.score(X_train, y_train)
valid_score = clf.score(X_valid, y_valid)



#   X + y
#se chiamiamo a al di fuori di questo slot non funziona
total = open('/content/drive/My Drive/Colab Notebooks/Projects/20200602_Twitter_Sentiment_Analysis/pos_tweets.txt')
Xy_pos = list()
#word tokenization
for sentence in total:
  #print(sentence)
  Xy_pos.append([format_sentence(sentence), 'pos'])
  #saves the sentence in format: [{tokenized sentence}, 'pos]
#Xy_pos


#   X + y
#se chiamiamo a al di fuori di questo slot non funziona
total = open('/content/drive/My Drive/Colab Notebooks/Projects/20200602_Twitter_Sentiment_Analysis/neg_tweets.txt')
Xy_neg = list()
#word tokenization
for sentence in total:
  #print(sentence)
  Xy_neg.append([format_sentence(sentence), 'neg'])
  #saves the sentence in format: [{tokenized sentence}, 'pos]
#Xy_neg



len(Xy_neg)



Xy_pos[0]



def split(pos, neg, ratio):
  train = pos[:int((1-ratio)*len(pos))] + neg[:int((1-ratio)*len(neg))]
  test = pos[int((ratio)*len(pos)):] + neg[int((ratio)*len(neg)):]
  return train, test

Xy_train, Xy_test = split(Xy_pos, Xy_neg, 0.1)



from nltk.classify import NaiveBayesClassifier

#encoded thorugh dictionaries
classifier = NaiveBayesClassifier.train(Xy_train)
classifier.show_most_informative_features()



example2 = "beautiful"
print(classifier.classify(format_sentence(example2)))



from nltk.classify.util import accuracy
print(accuracy(classifier, Xy_test))

 [markdown]
# ##Movies


import pandas as pd
total = pd.read_csv('/content/drive/My Drive/Colab Notebooks/Projects/20200602_Twitter_Sentiment_Analysis/movie_review.csv')
total



total_positive = total.copy()
total_positive.columns
total_positive = total_positive.loc[total_positive['tag'] == 'pos']
#total_positive = total_positive.pop('text')
total_positive = total_positive.drop(['fold_id', 'cv_tag', 'html_id', 'sent_id'], axis=1)
total_positive



total_negative = total.copy()
total_negative.columns
total_negative = total_negative.loc[total_negative['tag'] == 'neg']
#total_negative = total_negative.pop('text')
total_negative = total_negative.drop(['fold_id', 'cv_tag', 'html_id', 'sent_id'], axis=1)
total_negative



format_sentence('how are you')



#   tokenizer
#input: series, ?lists?
def create_dict(total_positive, total_negative):
  
  positive_reviews = list()
  #word tokenization
  for sentence in list(total_positive.values):
    positive_reviews.append([format_sentence(sentence[0]), 'pos'])
    #saves the sentence in format: [{tokenized sentence}, 'pos]
  
  negative_reviews = list()
  #word tokenization
  for sentence in list(total_negative.values):
    #print(sentence)
    negative_reviews.append([format_sentence(sentence[0]), 'neg'])
    #saves the sentence in format: [{tokenized sentence}, 'pos]
  
  return positive_reviews, negative_reviews

positive_reviews, negative_reviews = create_dict(total_positive, total_negative)



X = pd.concat([total_positive, total_negative], axis=0)
X.columns = ['text', 'sentiment']
X



import seaborn as sns
sns.countplot(x='sentiment', data=X)



y = pd.DataFrame(X.pop('sentiment'))
y



from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)



X_train['text'][0]



##del?
def preprocess_text(sen):
  # Removing html tags
  sentence = remove_tags(sen)

  # Remove punctuations and numbers
  sentence = re.sub('[^a-zA-Z]', ' ', sentence)

  # Single character removal
  sentence = re.sub(r"\s+[a-zA-Z]\s+", ' ', sentence)

  # Removing multiple spaces
  sentence = re.sub(r'\s+', ' ', sentence)

  return sentence

TAG_RE = re.compile(r'<[^>]+>')
#replaces anything between <> with an empty space
def remove_tags(text):
    return TAG_RE.sub('', text)



from keras.preprocessing.text import Tokenizer
tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts(X_train)

X_train = tokenizer.texts_to_sequences(X_train)
X_test = tokenizer.texts_to_sequences(X_test)



tokenizer = Tokenizer(num_words=5000)
tokenizer.fit_on_texts('come stai')
tokenizer.texts_to_sequences('come stai')



#del?
X = []
sentences = list(movie_reviews['review'])
for sen in sentences:
  X.append(preprocess_text(sen))



print(len(positive_reviews))
print(len(negative_reviews))



train = positive_reviews[:int((.9)*len(positive_reviews))] + negative_reviews[:int((.9)*len(negative_reviews))]
test = positive_reviews[int((.1)*len(positive_reviews)):] + negative_reviews[int((.1)*len(negative_reviews)):]
print(len(train), len(test))



print(train[0])



from nltk.classify import NaiveBayesClassifier

classifier = NaiveBayesClassifier.train(train)
classifier.show_most_informative_features()



example2 = "mulan"
print(classifier.classify(format_sentence(example2)))



from nltk.classify.util import accuracy
print(accuracy(classifier, test))


