import os
import gensim as gs
def trainWordEmbeddGensim():
    if "model.bin" in os.curdir("."):
        return
    else:
        model = Word2Vec(sentences, size=100, windows=5, min_count=25,\
                         workers=8)
        model.save("model.bin")
        return model
def loadModel(text):
    wordEmbeddings=gensim.models.KeyedVectors.load_word2vec_format("model.bin",\
                                                                    binary=True)
    ct=0
    for i in wordVectors.vocab:
        ct+=1
        if ct>=5:
            break
        print(i)
        print(wordVectors[i])
    for i in text:
