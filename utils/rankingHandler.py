def readRankingDouble():
    file1 = open('rankingTables/rankingDouble.txt', 'r')
    rank = {}
    Lines = file1.readlines()
    for line in Lines:
        line = line.split()
        rank[line[0]] = 0
        rank[line[1]] = 0
    i = 0
    rank4 =[[]]
    for line in Lines:
        line = line.split()
        if i>0:
            rank3 = rank2

        if(line[2]>line[3]):
            rank[line[0]] = rank[line[0]] + 1
        elif(line[2]<line[3]):
            rank[line[1]] = rank[line[1]] + 1

        rank2 = sorted(rank.items(), key=lambda x: x[1], reverse=True)

        if i>0:
            len2 = len(rank2)
            j=0
            while len2>0:
                if rank3[len2-1][0]!=rank2[len2-1][0]:
                    rank2[len2-1] = rank2[len2-1] + (line[4],)
                len2 -=1
            while j<4:
                if len(rank2[j]) != 3:
                    k=rank2[j][0]
                    h = 0
                    while h < 4:
                        if rank3[h][0] == k and len(rank3[h]) > 2:
                            rank2[j]= rank2[j] +(rank3[h][2],)
                        h+=1
                j += 1
        i+=1
        if len(rank2[0])<3:
            rank2[0] = rank2[0] +(line[4],)
    return rank2

def readRankingSingle():
    rank2 = [('aaa', 20, '10.20.1999'), ('bbb', 18, '10.20.1999'), ('ccc', 15, '10.20.1999'), ('ddd', 12, '10.20.1999'), ('eee', 8, '10.20.1999'), ('fff', 7, '10.20.1999')]
    return rank2