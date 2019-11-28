class Dictionary:

    __dictionaryStr = ""
    __table = []# MAYBE NOT GLOBALLY???
    type = ""
    k = 0

    #blk (index , lengths)
    #fc  [(index, (lentgh,prefix length),  ...., .....),(index, (lentgh,prefix length),  ...., .....)]
    def __init__(self, TermList, type):
        """Given sorted list of terms, creates a data
        structure which holds a compressed dictionary
        TermList is the sorted list of terms
        Type is one of the following tupples: ("STR"),
        ("BLK", k), ("FC", k) where k is the size of
        the block"""
        if type == "STR":
            self.TermList = TermList
            self.type = type
            counter = 0
            for term in TermList:
                self.__dictionaryStr += term
                self.__table.append(counter)
                counter+=len(term)
            print(self.__table)
        else:
            self.__table = []
            self.type ,self.k = type
            add = len(TermList)%self.k
            self.TermList = TermList
            for i in range(add):
                self.TermList.append(None)
            print(self.TermList)

            if self.type == "BLK":
                for i in range(0,len(TermList),self.k):
                    if self.TermList[i] == None:
                        break
                    block = [self.termLocation(self.TermList[i])]
                    count = 0
                    while count < self.k:
                        if self.TermList[i+count] == None:
                            break
                        block.append(len(self.TermList[i+count]))
                        count+=1
                    self.__table.append(tuple(block))

                print(self.__table)
                #TO String
            elif self.type == "FC":
                for i in range(0, len(TermList), self.k):
                    if self.TermList[i] == None:
                        break
                    block = [self.termLocation(self.TermList[i]),(len(self.TermList[i]),0)]
                    count = 1
                    self.__dictionaryStr += self.TermList[i]
                    while count < self.k  :
                        currWord = self.TermList[i+count - 1]
                        nextWord = self.TermList[i+count]
                        #print("iteration :  {}\ncurrWord : {}\nnextWord : {}  ".format(count,currWord,nextWord))
                        if currWord == None:
                            break
                        prefix = self.calcPrefix(currWord, nextWord)# CALCULATE PREFIX
                        self.__dictionaryStr += nextWord[len(prefix):]
                        block.append((len(nextWord), len(prefix)))
                        count += 1
                    self.__table.append(tuple(block))
                print(self.__dictionaryStr)
                print(self.__table)


    #########################################
    def calcPrefix(self, curr, next):
        prefix = ""
        for i in range(len(curr)):
            if i < len(next):
                if curr[i] == next[i]:
                    prefix += curr[i]
                else:
                    return prefix
        return prefix
    #########################################
    def GetString(self):
        """Returns the dictionary's string"""
        return self.__dictionaryStr
    def GetInfo(self, term):
        #print("in getInfo")
        #print(term)
        """ Returns relevant data about term.
        For "STR" it returns the location of the term
        in the string
        For "BLK" it returns a tuple containing the
        location of the container block and the lengths
        of its terms
        For "FC" it returns a tuple containing the
        location of the container block and pairs
        containing the lengths and prefixes sizes of
        its terms"""
        location = self.termLocation(term)
        if self.type == "STR":
            return location
        else:
            for tup in self.__table:
                index =1
                currLocation = tup[0]
                while index <= self.k:
                    if location == currLocation :
                        return tup
                    if self.type == "BLK":
                        currLocation += tup[index]#pointer to next term in the block
                    elif self.type == "FC":
                        currLocation += tup[index][0]  # pointer to next term in the block
                    index += 1

    #############################

    def termLocation(self,term):
        location = 0
        for word in self.TermList:
            if word == term:
                break
            location += len(word)
        return location

     ############################




strArray=["ba", "banana", "car", "cat", "dog", "doggy", "dump", "far", "formula", "in", "input", "int"]
'''
print(1)
dic1 = Dictionary(strArray,"STR")
print(dic1.GetString())
print(dic1.GetInfo("banana"))
print(2)
dic2 = Dictionary(strArray,("BLK",2))
print(3)
dic3 = Dictionary(strArray,("BLK",3))
'''
'''

'''

print(4)
dic4 = Dictionary(strArray,("BLK",4))
print(dic4.GetInfo("car"))
print(dic4.GetInfo("dog"))
print(dic4.GetInfo("int"))


'''
print(5)
dic5= Dictionary(strArray,("BLK",5))
print(dic4.GetInfo("car"))
print(dic4.GetInfo("doggy"))
print(dic4.GetInfo("int"))

print(6)
dic6 = Dictionary(strArray,("BLK",6))
print(dic4.GetInfo("car"))
print(dic4.GetInfo("dump"))
print(dic4.GetInfo("int"))
print(7)
dic7 = Dictionary(strArray,("BLK",7))
print(dic4.GetInfo("car"))
print(dic4.GetInfo("far"))
print(dic4.GetInfo("int"))
print(8)
dic8 = Dictionary(strArray,("BLK",8))
print(dic4.GetInfo("car"))
print(dic4.GetInfo("formula"))
print(dic4.GetInfo("int"))

'''
dicFC4 = Dictionary(strArray,("FC",4))
print(dicFC4.GetString() == "bananacartdoggyumpfarformulainputt")

print(dicFC4.GetInfo("car"))
print(dicFC4.GetInfo("dog"))
print(dicFC4.GetInfo("int"))

print("FC2")
dicFC2 = Dictionary(strArray,("FC",2))
print(dicFC2.GetInfo("car"))
print(dicFC2.GetInfo("dog"))
print(dicFC2.GetInfo("int"))

print("FC3")
dicFC3 = Dictionary(strArray,("FC",3))
print(dicFC3.GetInfo("car"))
print(dicFC3.GetInfo("dog"))
print(dicFC3.GetInfo("int"))




