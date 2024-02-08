# lemmatization
# from nltk.corpus import stopwords
import spacy
# import nltk
# nltk.download('stopwords')

# Basic ETL
# read documents
# this subset represents the first 9000 documents in the corpus, restricted due to memory constraints
with open('data/20newsgroups_9000.txt', 'r') as file:
    # Read file contents, splitting into a list using the delimiter "|~|~|"
    docs = file.read().split('|~|~|')

# print(docs[6000][:250])

# preprocessing
# reduce words to their simplest form, (not stemming as the result is still an actual word)
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

lem_docs = lemmatization(docs[:100])

print(lem_docs[0][:500])
# modelling

# visualization
