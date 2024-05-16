import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def remove_stopwords(text):
    nltk.download('stopwords')

    nltk.download('punkt')
    
    word_tokens = word_tokenize(text)
    
    stop_words = set(stopwords.words('english'))
    
    filtered_words = [word for word in word_tokens if word.lower() not in stop_words]
    
    return filtered_words

passage = """It wasn't quite yet time to panic. There was
still time to salvage the situation. At least that is what
she was telling himself. The reality was that it was time
to panic and there wasn't time to salvage the situation,
but he continued to delude himself into believing there was."""

removed_stopwords = remove_stopwords(passage)

print("Original Tokens:")
print(word_tokenize(passage))
print("\nTokens after removing stopwords:")
print(removed_stopwords)


#Theory
# Stopwords are commonly used words in a language that are often removed from text data during natural language processing tasks because they typically do not carry significant meaning or contribute much to the understanding of the text. Examples of stopwords in English include "the", "is", "at", "which", etc.

# NLTK (Natural Language Toolkit) is a leading platform for building Python programs to work with human language data. It provides easy-to-use interfaces to over 50 corpora and lexical resources such as WordNet, along with a suite of text processing libraries for classification, tokenization, stemming, tagging, parsing, and semantic reasoning.

# nltk.corpus is a module within NLTK that provides access to various corpora and lexical resources, including stopwords, word lists, and annotated text collections. In this context, nltk.corpus.stopwords is specifically used to access stopwords in different languages.

# nltk.tokenize is another module within NLTK that provides functions for tokenizing text, which involves splitting text into individual words or sentences. It includes different tokenizers for various purposes, such as word tokenization (word_tokenize()) and sentence tokenization (sent_tokenize()).