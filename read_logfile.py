import gensim
from resumeparser import parse_resume

infile = r"example.log"

with open(infile) as f:
    f = f.readlines()

final_document=[]
job_name=[]
job_url=[]
for index,line in enumerate(f):
    l=[]
    single = False
    double = False
    for pos, char in enumerate(line) :
        if(single and char == "'"):
            l.append(pos)
            single = False
        elif(double and char == '"'):
            l.append(pos)
            double = False
        elif(not single and not double):
            if(char=="'"):
                single = True
                l.append(pos)
            if(char=='"'):
                double = True
                l.append(pos)
    document=[]
    job_url.append(line[l[0]+1:l[1]].strip())
    job_name.append(line[l[2]+1:l[3]].strip())
    for i in range(4,len(l),1):
        if(i%2==0):
            document.append(line[l[i]+1:l[i+1]].strip())
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
skills = []
dictionary = list(model.wv.vocab)
for item in w1:
    if item in dictionary:
        skills.append(item)
print("")
print("")
print("important skills (that are used for job suggestion)")
print(skills)

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
    print("JOB NAME: ")
    print(job_name[ans[i][1]])
    print("JOB_URL: ")
    print(job_url[ans[i][1]])
    print ("REQUIRED SKILLS: ")
    print(final_document[ans[i][1]])
    print( "")
    print( "")
    print( "")