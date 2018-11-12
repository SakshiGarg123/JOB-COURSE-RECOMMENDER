import gensim
from resumeparser import parse_resume
#from past import autotranslate
print ("her")
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
    # print(document)
    final_document.append(document)
model = gensim.models.Word2Vec(
        final_document,
        size=1500,
        window=10,
        min_count=1,
        workers=10,sg=1)
model.train(final_document, total_examples=len(final_document), epochs=100)
ans=[]
w1 = parse_resume()
# w1=['Bangalore','Finance']
skills = []
dictionary = list(model.wv.vocab)
for item in w1:
    if item in dictionary:
        skills.append(item)
print ("")
print( skills)

i=0
for document in final_document:
    if(len(document)!=0):
        ans.append([model.n_similarity(document, skills),i])
        # print document,final_document[i]
    i=i+1
#print(ans)
ans=sorted(ans)
# print("newline")
print ("")
print( "")
print (""  )
print ("similarity: ", ans[-1:-5:-1])

print("")
for i in range(-1,-5,-1):
    print (final_document[ans[i][1]])
    print( "")