'''
    Read results and return them
'''
def read_results(result):

    arq = open(result, "r")
    vector = []

    for line in arq:
        line = line.replace("\n","").split(" ")
        res = []
        for i in range(len(line)):
            if line[i] != '':
                res.append(line[i])
        vector.append(res)
    arq.close
    return vector

def read_results_vpr(result):

    arq = open(result, "r")
    vector = []

    count = 0
    for line in arq:
        if count == 0:
            dim = int(line)
        else:
            line = line.replace("\n","").split(" ")
            res = []
            for i in range(len(line)):
                if line[i] != '':
                    res.append(line[i])
            vector.append(res)
        count += 1
    arq.close
    return dim, vector