class PostingList:
    type = ""
    __gaps =[]
    __postingList = []
    def __init__(self, DocIDs, type):
        '''
        Given sorted list of DocIDs, creates a
        compressed posting list according to the
        compression type.
        The compressed posting list should be stored as
        byte array
        '''
        self.type = type
        self.DocIDs = DocIDs
        #calculateGaps
        self.__gaps = self.calculateGaps(DocIDs)
        print(self.__gaps)
        if type == "V": # Varint
                self.__postingList = self.VBEncode(self.__gaps)

        elif type == "LP": # Length precoded
            pass
        elif type == "GV": # Group varint
            pass
    ###############
    def calculateGaps(self,IDs):
        '''
        :param IDs: a list of posting IDs
        :return: the array of the gaps between the IDs
        '''
        gaps = [IDs[0]]
        index = 1
        while index < len(IDs):
            gaps.append(IDs[index]-IDs[index-1])
            index+=1
        return gaps
    ###############
    def VBEncodeNumber(self,n):
        bytesList = bytearray()
        bitsArray = []
        binaryNum = bin(n).replace("0b", "")
        #
        curr = binaryNum[-7:]
        curr = curr[::-1]
        zeros = '0' * (7 - len(curr))  # CALCULATE ZEROS
        curr += zeros  # ADD ZEROS
        curr += '1'
        curr = curr[::-1]
        binaryNum = binaryNum[: - 7]
        if len(binaryNum) == 0:
            bytesList.append(int(curr, 2))
            return bytesList
        bitsArray.append(curr)

        while True:
            if len(binaryNum) <= 7:
                zeros = '0' * (8 - len(binaryNum))  # CALCULATE ZEROS
                binaryNum = binaryNum[::-1]  # INVERT
                binaryNum += zeros  # ADD ZEROS
                binaryNum = binaryNum[::-1]  # INVERT

                bitsArray.append(binaryNum)  # ADD TO ARRAY
                break
            curr = binaryNum[-7:]
            curr = curr[::-1]
            curr += '0'
            curr = curr[::-1]
            bitsArray.append(curr)
            binaryNum = binaryNum[: - 7]
        bitsArray.reverse()

        for byte in bitsArray:
            bytesList.append(int(byte, 2))
        return bytesList
    ###############


    def VBEncode(self,numbers):
        byteStream = bytearray()
        #print(numbers)
        for number in numbers:
            byteStream += self.VBEncodeNumber(number)
        return byteStream
    ###############

    def GetList(self):
        '''
        Returns a byte-array containing the
        compressed string
        '''
        return self.__postingList


testList = [7,12,23,1033,2354634,2354636]

postListV = PostingList(testList,"V")

print(postListV.GetList())



################




#a = bin(33).replace("0b","")
#print(a)



##print('\n\n\n\n######################################################################################################')

'''
a = bin(824).replace("0b","")
print("original a : {}".format(a))
end = a[-7:]
print("end pre inversion : {}".format(end))
end = end[::-1]
print("end post inversion : {}".format(end))
end +='1'
print("adding 1 to end : {}".format(end))
newEnd = end[::-1]
print("newEnd : {}".format(newEnd))
a = a[:len(a)-7]
print("a after slicing : {}".format(a))
a = a[::-1]
print("a post inversion : {}".format(a))
a += '0'*5
print("a post zeros : {}".format(a))
a = a[::-1]
print("a inverted   : {}".format(a))

'''


'''
    def VBEncodeNumber(self,n):
        bytesList = bytearray() #initialize byte array
        temp = n
        count = 0
        while True:
            bytesList.append(temp%128)
            if temp < 128:
                break
            temp = temp/128
            count +=1
        bytesList[count]+=128 # add the c bit to the last element of the byte array
        return bytesList

'''