from top2vec import Top2Vec

# read documents
# this subset represents the first 9000 documents in the corpus, restricted due to memory constraints
with open('data/20newsgroups_9000.txt', 'r') as file:
    # Read the content of the file
    content = file.read()
    # Split the content into a list using the delimiter "|~|~|"
    docs = content.split('|~|~|')

model = Top2Vec(docs)

topic_sizes, topic_nums = model.get_topic_sizes()

# get stats about 10 most frequent topics
topic_words, word_scores, topic_nums = model.get_topics(10)

# get the top 10 terms in each topic
for t in topic_words:
    print(t[:10])

# example output
'''
['mlb' 'espn' 'nhl' 'hockey' 'pittsburgh' 'playoffs' 'playoff' 'baseball' 'bruins' 'pitchers']
['bmw' 'motor' 'bike' 'bikes' 'honda' 'car' 'transmission' 'engines' 'motorcycle' 'toyota']
['edu' 'universities' 'university' 'educational' 'campus' 'college' 'academic' 'stanford' 'education' 'professor']
['amplifier' 'amps' 'circuits' 'amp' 'oscillator' 'circuit' 'electronics' 'transmitter' 'resistor' 'frequencies']
['encryption' 'encrypted' 'cryptography' 'algorithms' 'criminals' 'crypto' 'libertarians' 'governments' 'govt' 'algorithm']
['motherboard' 'macintosh' 'edu' 'mac' 'macs' 'svga' 'computers' 'universities' 'linux' 'vga']
['palestinians' 'israelis' 'israeli' 'zionist' 'israel' 'palestinian' 'genocide' 'palestine' 'jews' 'holocaust']
['medicine' 'disease' 'doctors' 'physician' 'doctor' 'doc' 'patients' 'medical' 'infections' 'dr']
['atheism' 'atheists' 'atheist' 'theism' 'theists' 'christianity' 'belief' 'beliefs' 'theology' 'religions']
['xterm' 'unix' 'xdm' 'aix' 'xview' 'ascii' 'xt' 'linux' 'vx' 'dx']
'''
