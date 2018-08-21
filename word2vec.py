import gzip
import gensim
documents=[["man","king","king"],["woman","queen","pretty"]]
model = gensim.models.Word2Vec(
        documents,
        size=150,
        window=10,
        min_count=1,
        workers=10)
model.train(documents, total_examples=len(documents), epochs=100)
w1="man"
print(model.wv.most_similar(positive=w1))

