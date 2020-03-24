import pickle

def savepkl(data,filename):
    output = open(filename + '.pkl', 'wb')

    # Pickle dictionary using protocol 0.
    pickle.dump(data, output)
    
    
    
def conll2spacy(data):
    sentList = []
    temp = []
    startloc = 0
    endloc = 0
    entity = []

    for word in data:
        if word == "":# new sent
            sent = " ".join(temp)
            e = {'entities':entity }
            finalSent = (sent,e)
            sentList.append(finalSent)
            temp = []
            entity = []
            startloc = 0
            endloc = 0

        else: # old sent
            w = word.split(" ")
            wordlen = len(w[0])
            if w[1] == 'O': # if normal increase both loc
                startloc += wordlen
                endloc += wordlen
            else:# if not normal then start and end diff
                endloc += wordlen
                tup = (startloc,endloc,w[1])
                entity.append(tup)
                startloc += wordlen
            temp.append(w[0])
            # including space
            startloc += 1
            endloc += 1
    return sentList



