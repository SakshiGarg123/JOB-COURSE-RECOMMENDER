import gensim
infile = r"newfile.log"

with open(infile) as f:
    f = f.readlines()
final_document=[]

for line in f:
    index_opening_brace=line.find('[')
    #print(index_opening_brace)
    l=[]
    for pos, char in enumerate(line) :
        if (char == "'"):
         l.append(pos)
    #print(l)
    document=[]
    for i in range(0,len(l)):
        if(i%2==0):
            document.append(line[l[i]+1:l[i+1]])
    print(document)
    final_document.append(document)
model = gensim.models.Word2Vec(
        final_document,
        size=150,
        window=10,
        min_count=1,
        workers=10)
model.train(final_document, total_examples=len(final_document), epochs=100)
w1="Team Leading"
print(model.wv.most_similar(positive=w1))
