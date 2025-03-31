def sentence_operations():
    # Input sentences
    sentence1 = input("Enter sentence 1: ")
    sentence2 = input("Enter sentence 2: ")

    # Convert to sets of unique words
    set1 = set(sentence1.lower().split())
    set2 = set(sentence2.lower().split())

    print("Unique words in Sentence 1:", set1)
    print("Unique words in Sentence 2:", set2)

    # Find common words
    common_words = set1.intersection(set2)
    print("Common words:", common_words)

    # Find unique words in both sentences
    unique_words_each = set1.symmetric_difference(set2)
    print("Words unique to each sentence:", unique_words_each)

sentence_operations()
