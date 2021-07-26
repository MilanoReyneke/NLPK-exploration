#!/usr/bin/env python
# coding: utf-8

# In[1]:


import nltk as nt
from nltk import word_tokenize, pos_tag
from nltk.corpus import wordnet


# In[2]:


#tokenizing sentences and words then doing POS analysis

testPara="Take this kiss upon thy brow, and in parting from you now, thus much let me avow: you are not wrong who deem that my days have been a dream. But if hope is flown away, in night or in day, in vision or in none, is ti therefore the less gone?"
sentences=nt.sent_tokenize(testPara)
tokenized_sent=[nt.word_tokenize(sent) for sent in sentences]
pos_sentences=[nt.pos_tag(sent) for sent in tokenized_sent]
pos_sentences


# In[46]:


"""
CC coordinating conjunction
CD cardinal digit
DT determiner
EX existential there (like: "there is" ... think of it like "there exists")
FW foreign word
IN preposition/subordinating conjunction
JJ adjective    'big'
JJR adjective, comparative    'bigger'
JJS adjective, superlative    'biggest'
LS List marker    1)
MD modal    could, will
NN noun, singular 'desk'
NNS noun plural    'desks'
NNP proper noun, singular    'Harrison'
NNPS proper noun, plural    'Americans'
PDT predeterminer    'all the kids'
POS possessive ending    parent's
PRP personal pronoun    I, he, she
PRP$ possessive pronoun    my, his, hers
RB adverb    very, silently,
RBR adverb, comparative    better
RBS Adverb, superlative    best
RP particle    give up
TO to go 'to' the store.
UH interjection    errrrrrrrm
VB Verb, base form    take
VBD verb, past tense, took
VBG Verb, gerund/present participle    taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d    take
VBZ verb, 3rd person sing. present    takes
WDT wh-determiner  which
WP wh-pronoun    who, what
WP$ possessive wh-pronoun    whose
WRB wh-adverb    where, when"""


# In[6]:


#making lists of nouns, pronouns and verbs in the text, and also finding a 'core' list which is the order of nouns and verbs in the text



core = []


for i in range(len(pos_sentences)):
    for j in range(len(pos_sentences[i])):
        if (pos_sentences[i][j][1] in ('NN','NNS','NNP','NNPS', 'PRP','VB','VBD','VBG','VBN','VBP','VBZ') ):
            core.append(pos_sentences[i][j][0])


nouns = []

for i in range(len(pos_sentences)):
    for j in range(len(pos_sentences[i])):
        if (pos_sentences[i][j][1] in ('NN','NNS','NNP','NNPS', 'PRP') ):
            newNouns.append(pos_sentences[i][j][0])
            

verbs = []
for i in range(len(pos_sentences)):
    for j in range(len(pos_sentences[i])):
        if (pos_sentences[i][j][1] in ('VB','VBD','VBG','VBN','VBP','VBZ')):
            newVerbs.append(pos_sentences[i][j][0])
            

pronouns = [] 
for i in range(len(pos_sentences)):
    for j in range(len(pos_sentences[i])):
        if (pos_sentences[i][j][1] in ('PRP')):
            pronouns.append(pos_sentences[i][j][0])






    


# In[7]:


#making a list of the nouns and their 'possesions'


posessions = [] 
for i in range(len(pos_sentences)):
    for j in range(len(pos_sentences[i])-1):
        if (pos_sentences[i][j][1] in ('POS','PRP$')) and (pos_sentences[i][j+1][1] in ('NN','NNS','NNP','NNPS')):
            posessions.append((pos_sentences[i][j][0], pos_sentences[i][j+1][0]) )
                              
print(posessions)


# In[ ]:


# the nltk does not seem to correctly identify the phrase "thy brow." Possibly because it is archaic English

