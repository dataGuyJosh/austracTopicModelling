import nltk

# modelling
import gensim
import gensim.corpora as corpora
from gensim.utils import simple_preprocess
from gensim.models import TfidfModel


# lemmatization
import spacy
from nltk.corpus import stopwords

# visualisation
import pyLDAvis
import pyLDAvis.gensim

'''# ETL'''
# read documents
# this subset represents the first 9000 documents in the corpus, restricted due to memory constraints
with open('data/20newsgroups_9000.txt', 'r') as file:
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

# tokenization, part-of-speech tagging
# remove words based on part-of-speech
# allowed_pos_tags: part-of-speech i.e. do we allow nouns, verbs, adjectives etc...
def lemmatization(docs, allowed_pos_tags=['NOUN', 'ADJ', 'VERB', 'ADV']):
    nlp = spacy.load('en_core_web_sm', disable=['parser', 'ner'])
    # remove email jargon, some of these are covered by stop words but shown here for completeness
    email_stop_words = ['From','Subject','Organization', 'Line']
    new_docs = []
    for d in docs:
        doc = nlp(d)
        new_doc = [w.lemma_ for w in doc if (not w.is_stop) and (w.pos_ in allowed_pos_tags) and (w.text not in email_stop_words)]
        new_docs.append(" ".join(new_doc))
    return new_docs


# Convert a document into a list of tokens. This lowercases, tokenizes and de-accents
def gensim_preprocessing(docs):
    return [gensim.utils.simple_preprocess(d, deacc=True) for d in docs]


print('lemmatization')
# lem_docs = lemmatization(docs[:1000])
lem_docs = lemmatization(docs)
# print(lem_docs[0][0:90])
print('gensim')
docs_words = gensim_preprocessing(lem_docs)
# print(docs_words[0][0:20])


# n-grams
print('n-grams')
bigram_phrases = gensim.models.Phrases(docs_words, min_count=5, threshold=100)
trigram_phrases = gensim.models.Phrases(
    bigram_phrases[docs_words], threshold=100)

bigram = gensim.models.phrases.Phraser(bigram_phrases)
trigram = gensim.models.phrases.Phraser(trigram_phrases)


def make_bigrams(docs):
    return [bigram[d] for d in docs]


def make_trigrams(docs):
    return [trigram[bigram[d]] for d in docs]


docs_bigrams = make_bigrams(docs_words)
docs_bigrams_trigrams = make_trigrams(docs_bigrams)
# print(docs_bigrams_trigrams[0])

# tf-idf
print('tf-idf')
id2word = corpora.Dictionary(docs_bigrams_trigrams)
docs = docs_bigrams_trigrams
corpus = [id2word.doc2bow(d) for d in docs]

tfidf = TfidfModel(corpus, id2word=id2word)
low_value = 0.03
words = []
words_missing_in_tfidf = []

for i in range(0, len(corpus)):
    bow = corpus[i]
    low_value_words = []
    tfidf_ids = [id for id, value in tfidf[bow]]
    bow_ids = [id for id, value in tfidf[bow] if value < low_value]
    drops = low_value_words+words_missing_in_tfidf
    for j in drops:
        words.append(id2word[j])
    words_missing_in_tfidf = [id for id in bow_ids if id not in tfidf_ids]

    new_bow = [b for b in bow if b[0] not in low_value_words and b[0] not in words_missing_in_tfidf]
    corpus[i] = new_bow

# # generate bag-of-words for each document i.e. word frequency lists for each document
# id2word = corpora.Dictionary(docs_words)
# corpus = [id2word.doc2bow(d) for d in docs_words]


'''# LDA Topic Model'''
# given that we're working with 9k documents with no shuffling; we're unlikely to see 20 distinct topics
print('modelling')
lda_model = gensim.models.ldamodel.LdaModel(
    corpus=corpus,
    id2word=id2word,
    num_topics=10,
    random_state=100,
    update_every=1,
    chunksize=100,
    passes=10,
    alpha="auto"
)

'''# Model Visualization'''
vis = pyLDAvis.gensim.prepare(lda_model, corpus, id2word, mds='mmds', R=30)
pyLDAvis.show(vis, local=False)
