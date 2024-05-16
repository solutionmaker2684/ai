from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Initialize Porter Stemmer
porter_stemmer = PorterStemmer()

# Input sentence
sentence = """
It wasn't quite yet time to panic. There was still time to salvage the situation.
At least that is what she was telling himself. The reality was that it was time
to panic and there wasn't time to salvage the situation, but he continued to delude
himself into believing there was.
"""

# Tokenize the sentence into words
words = word_tokenize(sentence)

# Stem each word and print original word along with its stemmed form
for word in words:
    print(word, " : ", porter_stemmer.stem(word))


#Theory
# Stemming is the process of reducing words to their root or base form, which may not always be a real word. It's commonly used in natural language processing to normalize words and reduce them to a common base form.
# For example, the words "running", "ran", and "runs" would all be stemmed to "run".

# nltk.stem is a module within NLTK (Natural Language Toolkit) that provides implementations of various stemming algorithms.
# Stemming algorithms aim to identify and remove affixes (suffixes, prefixes, infixes) from words to obtain their root or base form.
# Common stemmers in NLTK include the Porter Stemmer (PorterStemmer), Lancaster Stemmer (LancasterStemmer), and Snowball Stemmer (SnowballStemmer).

# nltk.tokenize is another module within NLTK that provides functions for tokenizing text, which involves splitting text into individual words or sentences.
# Tokenization is a fundamental task in natural language processing and is often a pre-processing step before tasks such as stemming, part-of-speech tagging, or sentiment analysis.
# Common tokenizers in NLTK include word tokenization (word_tokenize()) and sentence tokenization (sent_tokenize()).