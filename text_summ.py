


import spacy 
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation




text = "The Internet is the biggest world-wide communication network of computers. The Internet has millions of smaller domestic, academic, business, and government networks, which together carry many different kinds of information. The short form of internet is the 'net'. The World Wide Web is one of its biggest services. It is used by billions of people all over the world. "





stopwords = list(STOP_WORDS)





stopwords




len(stopwords)





nlp = spacy.load('en')





docx = nlp(text)





for token in docx:print(token.text) 




word_frequencies = {}
for word in docx:
    if word.text.lower() not in stopwords:
        if word.text.lower() not in punctuation:
            if word.text not in word_frequencies.keys():
                word_frequencies[word.text]=1
            else:
                word_frequencies[word.text]+=1




maximum_freq = max(word_frequencies.values())











for word in word_frequencies.keys():
    word_frequencies[word] = (word_frequencies[word]/maximum_freq)









sentence_list = [ sentence for sentence in docx.sents ]











sentence_scores = {}
for sent in sentence_list:
    for word in sent:
        if word.text.lower() in word_frequencies.keys():
            #if len(sent.text.split(' ')) < 30:
                if sent not in sentence_scores.keys():
                    sentence_scores[sent] = word_frequencies[word.text.lower()]
                else:
                    sentence_scores[sent] += word_frequencies[word.text.lower()]





from heapq import nlargest









summarized_sentences = nlargest(2,sentence_scores,key=sentence_scores.get)








final_text = [w.text for w in summarized_sentences ]





summary= ' '.join(final_text)





len(text)





len(summary)



summary




