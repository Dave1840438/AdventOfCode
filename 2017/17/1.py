input = open('input').readline().strip()

step = 354

currIndex = 0

buff = [0]



for i in range(1, 2018):
    currIndex = (currIndex + step) % len(buff)
    #print len(buff)
    buff.insert(currIndex+1, i)
    #print buff, currIndex
    currIndex +=1
    



print buff
print buff[buff.index(2017)+1]
