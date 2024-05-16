def sort_sentence(sentence):
    return ' '.join(sorted(sentence.split()))

sentence = "this is an example sentence"
sorted_sentence = sort_sentence(sentence)
print("Sorted Sentence:", sorted_sentence)

# Explanation:
# 1. The `sort_sentence` function takes a sentence as input.
# 2. Inside the function, `sentence.split()` splits the sentence into words, which are then sorted using the `sorted()` function.
# 3. The sorted words are joined back into a sentence using `' '.join(sorted(sentence.split()))`.
# 4. Finally, the sorted sentence is returned.
# 5. The input sentence is provided, and the sorted sentence is printed.