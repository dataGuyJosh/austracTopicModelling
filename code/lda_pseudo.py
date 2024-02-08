'''
# ETL
The dataset is a single text file containing 9000 emails with various topics
- raw data was presented in a folder structure
- merged first 9k documents into a single text file for source control convenience
- topics include atheism, computer graphics, cars, motorcycles, cryptography, medicine, politics etc...
Read email contents into a python list
'''

# num_docs: the number of documents to read, 0 indicates to read all docs
# regex: restrict files using regex on file name e.g. only read .txt files


def read_documents(file_path, num_docs=0, regex=''):
    # read documents with optional parameters
    pass


'''# Preprocessing'''


def word_processing(docs):
    new_docs = []
    '''
    We have a list of files, now to clean the data into a form usable by our chosen model (LDA)
    - removal of
      - stopwords
        - incorporate a generic stopword list
        - additionally remove email-specific stopwords e.g. "subject"
      - punctuation
      - character accents e.g. Ü --> U
    - lemmatization
      - LDA presents as a list of the most "salient" (common?) words in each topic.
        This makes lemmatization preferable to stemming as we produce real words
        making topic interpretation slightly easier.
    - restrict words based on POS e.g. preserve nouns, adjectives, verbs and adverbs
      but discard pronouns, prepositions, conjunctions and interjections
    '''
    return new_docs


def n_grams(docs, n=3):
    '''
    Each document is now effectively a list simplified, lowercase words.
    Model performance will likely see improvement through the addition of n-grams.
    '''
    new_docs = []
    for d in docs:
        # generate n-grams up to n i.e. if n = 3, find bigrams and trigrams
        # add to document d's word list
        pass
    return new_docs

def get_bow(docs):
    '''
    https://radimrehurek.com/gensim/models/ldamodel.html
    The library we're using for LDA requires several data-related arguments
    - corpus: a 2D list of tuples where the first value indicates a term (as an index)
      and the second value indicates the frequency of that term in the document
    - id2word: a list of terms mapping to the indexes in corpus
    Both of these can be generated using gensim
    
    '''
    return [id2word, corpus]


def tf_idf(id2word, corpus, threshold=0.03):
    new_docs = []
    '''
  Term Frequency - Inverse Document Frequency
  - terms with high TF-IDF scores occur frequently within a document 
    but relatively rarely in the rest of the corpus
  - we assume that a high TF-IDF score indicates a given term is important to the context of the document
  - set a threshold score at which we accept/deny terms for being used
  - filter documents to only include terms which pass this threshold
  '''
    return new_docs


'''# Model Training/Validation'''
def train_lda_model(id2word, corpus, hyper_parameters=[10, 1, 100]):
    '''
    At this point we have our data-based inputs, define hyper parameters and run the model.

    It may also be pertinent to implement a grid search here to find the best set of hyper parameters,
    however a prerequisite to this is implementing model quality metrics
    - Perplexity: low values indicate good performance on unseen data
    - Topic Coherence: terms in a topic are similar
    - Topic Diversity: topics are distinct from each other
    '''
    pass


def validate_model(model, id2word, corpus, metric):
    '''
    https://github.com/MIND-Lab/OCTIS
    Using the octis library we can perform model comparisons using various metrics, including Coherence.
    For a given model/metric, return result e.g. average coherence on all topics
    '''
    pass


def grid_search(id2word, corpus):
    '''
    Iterate through all combinations of a set of hyper-parameters,
    evaluating each setup's performance each time to find the best combination
    Example params
    'num_topics': [5, 10, 15, 20]
    'update_every': [1, 2, 3]
    'chunksize': [100, 110, 120]

    for each combinations of hyper parameters
      train model --> train_lda_model
      calculate topic coherences --> validate_model
      summarize model based on coherences e.g. average topic coherence

    return model with highest average coherence
    '''


def visualize_lda_model(model, id2word, corpus):
    '''
    This LDA visualization tool works with gensim models (and was shamelessly stolen from a tutorial, see resources in README.md)
    https://pyldavis.readthedocs.io/en/latest/modules/API.html
    vis = pyLDAvis.gensim.prepare(...)
    pyLDAvis.show(vis)
    '''
    pass


if __name__ == "__main__":
    # read documents
    docs = read_documents('data/20newsgroups_9000.txt')
    # perform term preprocessing
    docs_words = n_grams(word_processing(docs))
    # generate dictionary/word index (bag-of-words?)
    id2word, corpus = get_bow(docs_words)
    # filter words based on tf-idf
    corpus = tf_idf(id2word, corpus)
    # train model
    model = train_lda_model(id2word, corpus)
    # model = grid_search(id2word, corpus)
    # visualize
    visualize_lda_model(model, id2word, corpus)
