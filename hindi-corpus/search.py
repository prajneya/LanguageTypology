import stanza

words_to_search = ["वाना", "वाया", "वाई"]

with open("dev_hi.txt", 'r', encoding="utf8") as f:
    sentences = f.readlines()

sentence_len = len(sentences)

count = 1

for k in range(0, sentence_len):
    doc = sentences[k].split()
    for word in doc:
        for search_word in words_to_search:
            if search_word in word:
                with open("search_words.txt", "a", encoding="utf8") as text_file:
                    print(sentences[k], file=text_file)
                    print("----------------------------------------------------------------------------", file=text_file)

    print("Completed", (count*100)/520, "%")
    count += 1
