from functools import reduce
import operator
def hex_to_binary( hex_code ):
  bin_code = bin( int(hex_code,base=16))[2:]
  padding = (4-len(bin_code)%4)%4 
  leadingZero = len(hex_code)*4 - (len(bin_code) + padding)
  padding += leadingZero
  return '0'*padding + bin_code

input = open('input16.txt', 'r').read()

inputBinary = hex_to_binary(input)

class Packet:
    def __init__(self):
        self.headerSize =0
        self.version = 0
        self.type = 0
        self.subPacketCount = 0
        self.subPacketSize = 0
        self.isCommand = 0
        self.literal = []
        self.subpacket = []

    def PacketSize(self):
        retVal = 0 if len(self.subpacket) == 0 else  sum([A.PacketSize() for A in self.subpacket])
        retVal += self.headerSize + len(self.literal)*5
        return retVal

    def TraverseVersionSum(self):
        retVal = 0 if  len(self.subpacket) == 0 else sum([A.TraverseVersionSum() for A in self.subpacket])
        retVal += self.version 
        return retVal

def decodeHeader(input):
    retVal = Packet()
    retVal.version = int(input[0:3], 2)
    retVal.type = int(input[3:6], 2)
    retVal.headerSize = 6
    if retVal.type != 4:
        retVal.isCommand = 1
    sizeByteLength = 0
    if retVal.isCommand == 1:
        if(int(input[6],2) == 0):
          sizeByteLength = 15 
          retVal.subPacketSize = int(input[7:7+sizeByteLength],2)
        else:
          sizeByteLength =  11
          retVal.subPacketCount = int(input[7:7+sizeByteLength],2)

        retVal.headerSize += sizeByteLength + 1
    print("input:",input)
    print("New packet:")
    print("version:",input[0:3])
    print("type:",input[3:6])
    if retVal.isCommand == 1:
        print("flag:",input[6])
        print("length:",input[7:7+sizeByteLength])

    return retVal


def decodeLiteral(input,packet):
    flag = 1
    offset = 0

    while flag == 1:
        flag = int(input[0+offset*5],2)     
        print("payload:",input[0+offset*5:5+offset*5])
        packet.literal.append(input[1+offset*5:5+offset*5])
        offset +=1
   
  
def calcPacketLength(usedBits):
    diff = usedBits % 4
    return usedBits + (4-diff)

def printPacketInfo():
    print("Packet:")



def process(inputBinary):
    if(len(inputBinary) < 11):
       print("end arivved:",inputBinary)
       return None
    packet = decodeHeader(inputBinary)
    if packet.isCommand == 0:
       print("decode literal packet")
       decodeLiteral(inputBinary[packet.headerSize:],packet)
    else:
       if packet.subPacketCount == 0:            
            subinputBinary = inputBinary[packet.headerSize:]
            subpackentLength =0
            while subpackentLength < packet.subPacketSize :                
                subpacket = process(subinputBinary)
                if(subpacket == None):
                   break
                subpackentLength += subpacket.PacketSize()
                subinputBinary= subinputBinary[subpacket.PacketSize():]               
                packet.subpacket.append(subpacket)
       else:
            subinputBinary = inputBinary[packet.headerSize:]          
            for i in range(packet.subPacketCount):
                print("do sub:",i)
                subpacket = process(subinputBinary)
                if(subpacket == None):
                   break      
                packet.subpacket.append(subpacket)
                subinputBinary= subinputBinary[subpacket.PacketSize():]
    print("<--")
    return packet
packets = []
versionSumAll = 0
while(len(inputBinary) > 0):

    packet = process(inputBinary)    
    if(packet != None):
        packets.append(packet)
        newlength = calcPacketLength(packet.PacketSize())
   
        inputBinary = inputBinary[newlength:]
        versionSum =  packet.TraverseVersionSum()
 
        versionSumAll += versionSum
    else:
        break
print ("Version SumAll:" ,versionSumAll)

OPERATORS = {
        0: sum,
        1: lambda x: reduce(operator.mul, x, 1),
        2: min,
        3: max,
        4: lambda x: int(''.join(x),2),
        5: lambda x: int(x[0] > x[1]),
        6: lambda x: int(x[0] < x[1]),
        7: lambda x: int(x[0] == x[1])        
    }

def TraversePacket(packet):   
    subValList = []
    subVal = 0
    for subpack in packet.subpacket:
        subValList.append(TraversePacket(subpack))
    if packet.type == 4:
      subVal = OPERATORS[packet.type](packet.literal)
    else:
      subVal = OPERATORS[packet.type](subValList)   
    return subVal

for packet in packets:
    print("--> new packet")
    print("Value:",TraversePacket(packet))