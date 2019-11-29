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
            self.__postingList = self.VBEncode(self.__gaps)
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
            if self.type =="V":
                byteStream += self.VBEncodeNumber(number)
            elif self.type =="LP":
                byteStream += self.LPEncodingNumber(number)
            elif type == "GV":
                pass
        return byteStream
    ###############

    def LPEncodingNumber(self,n):
        bytesList = bytearray()
        binaryNum = bin(n).replace("0b", "")
        byteLength = ''
        if len(binaryNum) < 7:
            byteLength = '00'  # 1
            zeros = '0' * (6 - len(binaryNum))  # CALCULATE ZEROS
            byteLength += zeros
            byteLength += binaryNum
            bytesList.append(int(byteLength, 2))
            return bytesList
        elif len(binaryNum) < 15:
            byteLength = '01'  # 2
            zeros = '0' * (14 - len(binaryNum))  # CALCULATE ZEROS
            byteLength += zeros
            byteLength += binaryNum
            bytesList = self.bitsToBytes(byteLength)
            return bytesList
        elif len(binaryNum) < 23:
            byteLength = '10'  # 3
            zeros = '0' * (22 - len(binaryNum))  # CALCULATE ZEROS
            byteLength += zeros
            byteLength += binaryNum
            bytesList = self.bitsToBytes(byteLength)
            return bytesList
        elif len(binaryNum) < 31:
            byteLength = '11'  # 4
            zeros = '0' * (30 - len(binaryNum))  # CALCULATE ZEROS
            byteLength += zeros
            byteLength += zeros
            byteLength += binaryNum
            bytesList = self.bitsToBytes(byteLength)
            return bytesList
    ###############

    def bitsToBytes(self,bits):
        bytes = bytearray()
        count = len(bits) / 8
        temp = bits
        currByte = ''
        while count > 0:
            currByte = temp[:8]
            bytes.append(int(currByte, 2))
            temp = temp[8:]
            count -= 1
        return bytes

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
print("length of number in bits is smaller than 7")
print(LPEncoding(1))
print(LPEncoding(7))
print(LPEncoding(8))
print(LPEncoding(14))
print(LPEncoding(15))
print(LPEncoding(22))
print(LPEncoding(23))
'''
postListLP = PostingList(testList,"LP")
print("length of number in bits is smaller than 15")

print(postListLP.GetList())
#print(LPEncoding(100))
#print(LPEncoding(122))




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