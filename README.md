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
- find best hyper-parameters (if relevant) using grid search
- LDA
  - conventional industry standard
  - scales well with corpus size
  - topic needs to be inferred based on output i.e. LDA won't necessarily output a "topic name"
- top2vec
  - python top2vec library makes this a very hands-off approach i.e. easy to implement
  - performs some preprocessing for us (stop words, lemmatization...)
  - automatically decides on number of topics --> hard to say if this is desirable
  - maybe less commonly used than LDA?

# Validation
- k-fold/leave-p-out cross-validation
- topic coherence (how semantically similar are high scoring words within a given topic)

# Interactions
- FastAPI endpoints
  - raw data CRUD (create, read, update, delete)
  - training
  - validation
  - topic view
  - document view
- cluster visualization

# Code Separation
A requirement for this project is that the code does not exceed 1000 lines, as such for simplicity I'll use a single python file, however ordinarily it would be broken down by feature.
- api.py: FastAPI code related to interacting with the app
- modelling.py: LDA or top2vec modelling code
- preprocessing.py: functions related to preprocessing steps
- pull_data.py: functions related to data entry e.g. to read data from CSV or JSON files, maybe pull data from an API etc...
- validation.py: k-fold or leave-p-out cross validation --> is this possible with LDA?

# Future Scope
- perform a literature review of methodologies relevant to topic modelling
  - why is LDA popular?
  - are there better modelling techniques for this dataset?
  - are emails considered short-text classification i.e. do we want to perform less preprocessing?
- ensemble modelling: use multiple modelling techniques (or the same technique on separate data) to better estimate topics e.g. if 9/10 models suggest a document belongs to a topic with similar popular words, they're likely to be correct --> does this apply to LDA?
  - is ensemble equivalent to bootstrap aggregation?
- learn about model validation techniques e.g. topic coherence
- learn more about top2vec: there's a bunch of parameters I haven't explored here and likely also better visualization tools
- source control: if this were to become a larger project, development branches should be used rather than pushing code to master (main) every time, especially when working with other developers

# Resources
- [top2vec](https://www.youtube.com/watch?v=bEaxKSQ4Av8)
- [Python lda](https://www.youtube.com/playlist?list=PL2VXyKi-KpYttggRATQVmgFcQst3z6OlX)
- [LDA Explained](https://www.youtube.com/playlist?list=PLs8w1Cdi-zvYskDS2icIItfZgxclApVLv)
- [20 Newsgroups Dataset](http://qwone.com/~jason/20Newsgroups)