# -*- coding: utf-8 -*-
"""Text Summarization using Word Frequency - NLP.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SfA4F1VihfDDOTGUKsE8I1KKYmszK4e7
"""

## input text article
article_text = input("Enter the text you want to summarize: ")

"""## Import Modules"""

import re
import nltk

"""## Data Preprocessing"""

article_text = article_text.lower()
article_text

import nltk
from nltk.tokenize import word_tokenize

# Download the 'punkt' and 'punkt_tab' resources
nltk.download('punkt')
nltk.download('punkt_tab')

clean_text = " ".join(word_tokenize(article_text))  # Tokenizes and keeps meaningful punctuation

import nltk
# Download the 'punkt_tab' resource
nltk.download('punkt_tab')
# Now you can use sent_tokenize
sentence_list = nltk.sent_tokenize(article_text)

## run this cell once to download stopwords
# import nltk
# nltk.download('stopwords')

"""## Word Frequencies"""

import nltk
# Download the 'stopwords' resource
nltk.download('stopwords')

# Now you can access the stopwords
stopwords = [word for word in nltk.corpus.stopwords.words('english') if word not in ['not', 'but', 'while']]

# Rest of your code remains the same
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf_vectorizer = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf_vectorizer.fit_transform(sentence_list)

# Calculate sentence scores
sentence_scores = {sentence: tfidf_matrix[idx].sum() for idx, sentence in enumerate(sentence_list)}

import nltk
from nltk.tokenize import word_tokenize
# Download the 'punkt_tab' resource
nltk.download('punkt_tab')
# Now you can use sent_tokenize
sentence_list = nltk.sent_tokenize(article_text)

## run this cell once to download stopwords
# import nltk
# nltk.download('stopwords')


import nltk
# Download the 'stopwords' resource
nltk.download('stopwords')

# Now you can access the stopwords
# Instead of 'stop', use 'stopwords' to access the list of stop words
print(stopwords)

import nltk
from nltk.tokenize import word_tokenize
from collections import defaultdict

# ... (your existing code) ...

# Calculate word frequencies
word_frequencies = defaultdict(int)
for sentence in sentence_list:
    for word in word_tokenize(sentence):
        if word not in stopwords:  # Exclude stop words
            word_frequencies[word] += 1

# Normalize word frequencies (optional, but often helpful)
max_frequency = max(word_frequencies.values())

"""## Calculate Sentence Scores"""

sentence_scores = {}

for sentence in sentence_list:
    for word in nltk.word_tokenize(sentence):
        if word in word_frequencies and len(sentence.split(' ')) < 30:
            if sentence not in sentence_scores:
                sentence_scores[sentence] = word_frequencies[word]
            else:
                sentence_scores[sentence] += word_frequencies[word]

word_frequencies

sentence_scores

from sentence_transformers import SentenceTransformer, util
model = SentenceTransformer('all-MiniLM-L6-v2')

# Get embeddings for all sentences
sentence_embeddings = model.encode(sentence_list)

# Remove similar sentences
final_sentences = []
used_indices = set()

for idx, sentence in enumerate(sentence_list):
    if idx not in used_indices:
        final_sentences.append(sentence)
        similarities = util.pytorch_cos_sim(sentence_embeddings[idx], sentence_embeddings)
        for sim_idx, sim_score in enumerate(similarities[0]):
            if sim_score > 0.8:  # Similarity threshold
                used_indices.add(sim_idx)

for sentence in sentence_scores:
    sentence_scores[sentence] /= len(sentence.split(' '))

"""## Text Summarization"""

# ... previous code ...

# Initialize summary as an empty list before the loop
summary = []

unique_summary = []
for sent in summary:  # Now, 'summary' is defined
    if all(sent not in s for s in unique_summary):
        unique_summary.append(sent)
summary = unique_summary

# ... rest of your code ...

# get top 5 sentences
import heapq
num_sentences = max(1, len(sentence_list) // 3)  # At least 1 sentence or 1/3 of the total
summary = heapq.nlargest(num_sentences, sentence_scores, key=sentence_scores.get)

print(" ".join(summary))

"""Legal ke liye train krna hai
to find risk
"""