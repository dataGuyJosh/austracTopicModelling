# AUSTRAC Topic Modelling
Detect topics from text reports

# Dataset
20 News groups
http://qwone.com/~jason/20Newsgroups/20news-bydate.tar.gz

# Potential Preprocessing Steps
- words to lower case
- punctuation removal
- stop word removal
- character accent removal
- stemming/lemmatization
- n-grams (bi/tri)
- TF-IDF i.e. removal of terms used frequently throughout the corpus

# Modelling Techniques
- LDA
  - conventional industry standard
  - scales well with corpus size
  - topic needs to be inferred based on output i.e. LDA won't necessarily output a "topic name"
- top2vec
  - python top2vec library makes this a very hands-off approach i.e. easy to implement
  - performs some preprocessing for us (stop words, lemmatization...)
  - automatically finds number of topics 
  - maybe less commonly used than LDA?
  - possibly less options to tweak than LDA e.g. what if we disagree with number of topics?

# Validation
- k-fold/leave-p-out cross-validation
- topic coherence (how semantically similar are high scoring words within a given topic)

# Interation
- FastAPI endpoints
  - data upload
  - training
  - validation
  - topic view
  - document view
- cluster visualization

# Code Separation
A requirement for this project is that the code does not exceed 1000 lines, as such for simplicity I'll use a single python file, however ordinarily it would be broken down by feature.
- api.py: FastAPI code related to interacting with the app, this would also contain `__main__`
- modelling.py: LDA or top2vec modelling code
- preprocessing.py: functions related to preprocessing steps
- pull_data.py: functions related to data entry e.g. to read data from CSV or JSON files, maybe pull data from an API etc...
- validation.py: model validation code i.e. cross validation, topic coherence


# Resources
- [top2vec](https://www.youtube.com/watch?v=bEaxKSQ4Av8)
- [Python lda](https://www.youtube.com/playlist?list=PL2VXyKi-KpYttggRATQVmgFcQst3z6OlX)
- [LDA Explained](https://www.youtube.com/playlist?list=PLs8w1Cdi-zvYskDS2icIItfZgxclApVLv)
- [20 Newsgroups Dataset](http://qwone.com/~jason/20Newsgroups)
