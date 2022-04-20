import spacy

from string import punctuation
from collections import Counter
from heapq import nlargest


import os
import re
import math
import operator


def lemmatize_words(words):
    lemmatized_words = []
    for word in words:
        lemmatized_words.append(word.lemma_)
    return lemmatized_words

def remove_special_characters(text):
    regex = r'[^a-zA-Z0-9\s]'
    text = re.sub(regex,'',text)
    return text
def freq(words):
    words = [word.lower() for word in words]
    dict_freq = {}
    words_unique = []
    for word in words:
       if word not in words_unique:
           words_unique.append(word)
    for word in words_unique:
       dict_freq[word] = words.count(word)
    return dict_freq
def pos_tagging(text):
    pos_tagged_noun_verb = []
    for word in text:
        if word.pos_ == "PROPN" or word.pos_ == "NOUN" or word.pos_ == "VERB":
             pos_tagged_noun_verb.append(word)
    return pos_tagged_noun_verb
def tf_score(word,sentence):
    freq_sum = 0
    word_frequency_in_sentence = 0
    len_sentence = len(sentence)
    for word_in_sentence in sentence:
        if word == word_in_sentence:
            word_frequency_in_sentence = word_frequency_in_sentence + 1
    tf =  word_frequency_in_sentence/ len_sentence
    return tf

def idf_score(no_of_sentences,word,sentences, nlp, STOP_WORDS):
    no_of_sentence_containing_word = 0

    for sentence in sentences:
        stopwords = list(STOP_WORDS)
        pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
        sent_doc = nlp(sentence)
        sent_words = []
        for token in sent_doc:
            if (token.text in stopwords or token.text in punctuation):
                continue
            if (token.pos_ in pos_tag):
                sent_words.append(token.lemma_)

        if word in sent_words:
            no_of_sentence_containing_word = no_of_sentence_containing_word + 1
    idf = math.log10(no_of_sentences/no_of_sentence_containing_word)
    return idf

def tf_idf_score(tf,idf):
    return tf*idf

def word_tfidf(dict_freq,word,sentences,sentence, nlp, STOP_WORDS):
    word_tfidf = []
    tf = tf_score(word,sentence)
    idf = idf_score(len(sentences),word,sentences, nlp, STOP_WORDS)
    tf_idf = tf_idf_score(tf,idf)
    return tf_idf

def sentence_importance(sent_words,dict_freq,sentences, nlp, STOP_WORDS):
     sentence_score = 0

     for word in sent_words:
        sentence_score = sentence_score + word_tfidf(dict_freq,word,sentences,sent_words, nlp, STOP_WORDS)
     return sentence_score

def generate_summary(document, lang = 'en', percentage=30):


    if lang == 'en':
        nlp = spacy.load('en_core_web_sm')
        from spacy.lang.en.stop_words import STOP_WORDS
    elif lang == 'de':
        nlp = spacy.load('de_core_news_sm')
        from spacy.lang.de.stop_words import STOP_WORDS

    doc = nlp(document)

    tokenized_sentence = [sent.text for sent in doc.sents]

    keyword = []
    stopwords = list(STOP_WORDS)
    for token in doc:
        if (token.text in stopwords or token.text in punctuation):
            continue
        else:
            keyword.append(token.lemma_)
    word_freq = Counter(keyword)


    no_of_sentences = int((percentage * len(tokenized_sentence))/100)
    print(no_of_sentences)
    c = 1
    sentence_with_importance = {}
    for sent in tokenized_sentence:
        #preprocess sentence
        pos_tagged = []
        stopwords = list(STOP_WORDS)
        pos_tag = ['PROPN', 'ADJ', 'NOUN', 'VERB']
        sent_doc = nlp(sent)
        for token in sent_doc:
            if (token.text in stopwords or token.text in punctuation):
                continue
            if (token.pos_ in pos_tag):
                pos_tagged.append(token.lemma_)
        sentenceimp = sentence_importance(pos_tagged,word_freq,tokenized_sentence, nlp, STOP_WORDS)
        sentence_with_importance[c] = sentenceimp
        c = c+1
    sentence_with_importance = sorted(sentence_with_importance.items(), key=operator.itemgetter(1),reverse=True)
    cnt = 0
    summary = []
    sentence_no = []
    for word_prob in sentence_with_importance:
        if cnt < no_of_sentences:
            sentence_no.append(word_prob[0])
            cnt = cnt+1
        else:
          break
    sentence_no.sort()
    cnt = 1
    for sentence in tokenized_sentence:
        if cnt in sentence_no:
           summary.append(sentence)
        cnt = cnt+1
    #summary = " ".join(summary)
    return summary

if __name__ == '__main__':
    text = """Machine learning (ML) is the scientific study of algorithms and statistical models that computer systems use to progressively improve their performance on a specific task. Machine learning algorithms build a mathematical model of sample data, known as "training data", in order to make predictions or decisions without being explicitly programmed to perform the task. Machine learning algorithms are used in the applications of email filtering, detection of network intruders, and computer vision, where it is infeasible to develop an algorithm of specific instructions for performing the task. Machine learning is closely related to computational statistics, which focuses on making predictions using computers. The study of mathematical optimization delivers methods, theory and application domains to the field of machine learning. Data mining is a field of study within machine learning, and focuses on exploratory data analysis through unsupervised learning.In its application across business problems, machine learning is also referred to as predictive analytics."""
    x = generate_summary(text, 'en')
    print (" ".join(x))