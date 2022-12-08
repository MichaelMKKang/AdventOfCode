with open('Day16 input.txt') as f:
    lines = f.readlines()
lines = [x.strip() for x in lines]
line = lines[0]

hex_dict = {
    '0' : '0000',
    '1' : '0001',
    '2' : '0010',
    '3' : '0011',
    '4' : '0100',
    '5' : '0101',
    '6' : '0110',
    '7' : '0111',
    '8' : '1000',
    '9' : '1001',
    'A' : '1010',
    'B' : '1011',
    'C' : '1100',
    'D' : '1101',
    'E' : '1110',
    'F' : '1111'
}

def hex_to_bits(line):
    bits = ''
    for l in line:
        bits += hex_dict[l]
    return bits

# Get the literal,where remainder starts, and remainder of the packet
def get_literal_from_packet(packets):
    version = int(packets[:3],2)
    typeid = int(packets[3:6],2)
    packets = packets[6:]
    literal = ''
    for i in range(0,len(packets),5):
        num = packets[i:i+5]
        literal+=num[1:]
        if num[0] == '0':
            break
    return int(literal,2),i+5+6,packets[i+5:]

def orch(bits):
    version = int(bits[:3],2)
    typeid = int(bits[3:6],2)
    print('')
    print('VERSION: ',version,', typeid: ',typeid)
    if typeid == 4:
        # returned bits is not really used
        literal,start,bits = get_literal_from_packet(bits)
        return version,literal,start,bits
    else:
        lengthtype = int(bits[6])
        print('lengthtype is: ',lengthtype)
        if lengthtype == 0:
            start = 0
            sub_length = int(bits[7:22],2)
            bits = bits[22:]
            print('sub_length:',sub_length)
            while start < sub_length:
                subversion,literal,substart,bits = orch(bits)
                #print('literal is',literal,'remainder is: ',bits)
                version += subversion
                start += substart
                if '1' not in bits:
                    return version,literal,start,bits
            return version,literal,start,bits
        else:
            packet_count = 0
            num_packets = int(bits[7:18],2)
            print('here is the num_packets: ',num_packets)
            bits = bits[18:]
            while packet_count < num_packets:
                subversion,literal,start,bits = orch(bits)
                print('        literal is: ',literal)
                version += subversion
                packet_count += 1
            return version,literal,start,bits
bits = hex_to_bits(line)
version,literal,start,bits = orch(bits)
print(version)