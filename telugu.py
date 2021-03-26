import stanza

nlp = stanza.Pipeline(lang='te')

with open("telugu-corpus/Telugu_500_sentences.txt", 'r', encoding="utf8") as f:
    sentences = f.readlines()

count = 1

for sentence in sentences:
    doc = nlp(sentence)
    with open("telugu-corpus/telugu_pos.txt", "a", encoding="utf8") as text_file:
        print(*[f'word: {word.text}\tupos: {word.upos}\txpos: {word.xpos}\tfeats: {word.feats if word.feats else "_"}' for sent in doc.sentences for word in sent.words], sep='\n', file=text_file)
        print("----------------------------------------------------------------------------", file=text_file)
    print("Completed", count/5, "%")
    count += 1
