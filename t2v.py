# import pandas as pd
from top2vec import Top2Vec

# read documents
# this subset represents the first 9000 documents in the corpus, restricted due to memory constraints
with open('20newsgroups_subset.txt', 'r') as file:
    # Read the content of the file
    content = file.read()
    # Split the content into a list using the delimiter "|~|~|"
    docs = content.split("|~|~|")

print(docs[0][:50])

model = Top2Vec(docs)

topic_sizes, topic_nums = model.get_topic_sizes()

topic_words, word_scores, topic_nums = model.get_topics(10)

for t in topic_words:
    print(t[:5])
'''
['edu' 'unix' 'universities' 'acad' 'university']
['mlb' 'espn' 'nhl' 'hockey' 'pittsburgh']
['bmw' 'motor' 'bike' 'bikes' 'car']
['amplifier' 'amps' 'oscillator' 'amp' 'circuits']
['encryption' 'encrypted' 'cryptography' 'algorithms' 'crypto']
['medicine' 'disease' 'physician' 'doctors' 'doctor']
['universities' 'edu' 'university' 'campus' 'college']
['atheism' 'atheists' 'atheist' 'theism' 'theists']
['edu' 'motherboard' 'universities' 'computers' 'macintosh']
['disk' 'disks' 'floppies' 'ssd' 'cdrom']
'''