import stanza

nlp = stanza.Pipeline(lang='te')

with open("Telugu_500_sentences.txt", 'r', encoding="utf8") as f:
    sentences = f.readlines()

with open("telugu_transliterated.txt", 'r', encoding="utf8") as f:
    roman_sentences = f.readlines()

sentence_len = len(sentences)

transliteration = {}

for i in range(0, sentence_len):
    words = sentences[i].split()
    roman_words = roman_sentences[i].split()

    word_len = len(words)

    for j in range(0, word_len):
        transliteration[words[j]] = roman_words[j]

count = 1

for k in range(0, sentence_len):
    doc = nlp(sentences[k])
    for sent in doc.sentences:
        for word in sent.words:
            if word.upos == "VERB":
                if word.text in transliteration:
                    if "inchu" in transliteration[word.text] or "inc" in transliteration[word.text]:
                        with open("inchu_infix.txt", "a", encoding="utf8") as text_file:
                            print(sentences[k], file=text_file)
                            print(roman_sentences[k], file=text_file)
                            print("----------------------------------------------------------------------------", file=text_file)

    print("Completed", (count*100)/952, "%")
    count += 1
