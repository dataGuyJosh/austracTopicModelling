import nltk
import numpy as np
import glob

# modelling
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import CoherenceModel

# lemmatization
import spacy
from nltk.corpus import stopwords

# visualisation
import pyLDAvis
import pyLDAvis.gensim


# read documents
# this subset represents the first 9000 documents in the corpus, restricted due to memory constraints
with open('20newsgroups_9000.txt', 'r') as file:
    # Read file contents, splitting into a list using the delimiter "|~|~|"
    docs = file.read().split('|~|~|')

'''
# Preprocessing
- words to lower case
- punctuation removal
- stop word removal
- character accent removal
- stemming/lemmatization
- n-grams (bi/tri)
- TF-IDF i.e. removal of terms used frequently throughout the corpus
'''
nltk.download('stopwords')
stopwords = stopwords.words('english')

# allowed_pos_tags: part-of-speech i.e. do we allow nouns, verbs, adjectives etc...


def lemmatization(docs, allowed_pos_tags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
    new_docs = []
    for d in docs:
        # tokenization, part-of-speech tagging
        doc = nlp(d)
        new_doc = []
        # remove words based on part-of-speech
        for token in doc:
            if token.pos_ in allowed_pos_tags:
                new_doc.append(token.lemma_)
        lem_doc = " ".join(new_doc)
        new_docs.append(lem_doc)
    return new_docs


# Convert a document into a list of tokens. This lowercases, tokenizes and de-accents
def gensim_preprocessing(docs):
    return [gensim.utils.simple_preprocess(d, deacc=True) for d in docs]


lem_docs = lemmatization(docs[:500])
print(lem_docs[0][0:90])
doc_words = gensim_preprocessing(lem_docs)
print(doc_words[0][0:20])

# generate bag-of-words for each document i.e. word frequency lists for each document
id2word = corpora.Dictionary(doc_words)
corpus = [id2word.doc2bow(d) for d in doc_words]

'''# LDA Topic Model'''
lda_model = gensim.models.ldamodel.LdaModel(
    corpus=corpus,
    id2word=id2word,
    num_topics=30,
    random_state=100,
    update_every=1,
    chunksize=100,
    passes=10,
    alpha="auto"
)

'''# Model Visualization'''
vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word, mds='mmds', R=30)
pyLDAvis.show(vis, local=False)