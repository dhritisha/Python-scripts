with open(r'''C:\Users\desengup\Desktop\py4e\words.txt''') as fh:
    newDict={}
    for line in fh:
        words=line.split()
        for word in words:
            newDict[word]=newDict.get(word,0) + 1
tmp=[]
for k,v in newDict.items():
    tmp.append((v,k))

tmp=sorted(tmp,reverse=True)

for tup in range(5):
    print(tmp[tup][1])
