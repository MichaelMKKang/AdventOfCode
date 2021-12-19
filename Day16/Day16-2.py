# now appending literals to list of values (in case we compare type4 to typenot_four)
# also passing the whole stirng along with just the start index along
# also getting rid of parse literal function and using bitwise logic (2x binary value shifts it one digit to the left)
# also using mapping for the operator evaluation

import math

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

op = [sum, math.prod, min, max,
      lambda ls: ls[0], # literal
      lambda ls: 1 if ls[0] > ls[1] else 0,
      lambda ls: 1 if ls[0] < ls[1] else 0,
      lambda ls: 1 if ls[0] == ls[1] else 0]

def orch(start):
    typeid = int(bits[start+3:start+6],2)
    print('TYPEID: ',typeid)
    start += 6
    if typeid == 4:
        vals = [0]
        while 1:
            vals[0] = vals[0]*(2**4) + int(bits[start+1:start+5],2)
            start += 5
            if bits[start-5] == '0':
                break
    else:
        vals = []
        if bits[start] == '0':
            sub_length = start + 16 + int(bits[start+1:start+16],2)
            start += 16
            print('sub_length:',sub_length)
            while start < sub_length:
                start,val = orch(start)
                vals.append(val)
                print('        literal is: ',val)
            print('end length')
        else:
            num_packets = int(bits[start+1:start+12],2)
            start += 12
            print('here is the num_packets: ',num_packets)
            for i in range(num_packets):
                start,val = orch(start)
                vals.append(val)
                print('        literal is: ',val)
            print('end count')         
    return start,op[typeid](vals)

test = 'E0525D9802FA00B80021B13E2D4260004321DC648D729DD67B2412009966D76C0159ED274F6921402E9FD4AC1B0F652CD339D7B82240083C9A54E819802B369DC0082CF90CF9280081727DAF41E6A5C1B9B8E41A4F31A4EF67E2009834015986F9ABE41E7D6080213931CB004270DE5DD4C010E00D50401B8A708E3F80021F0BE0A43D9E460007E62ACEE7F9FB4491BC2260090A573A876B1BC4D679BA7A642401434937C911CD984910490CCFC27CC7EE686009CFC57EC0149CEFE4D135A0C200C0F401298BCF265377F79C279F540279ACCE5A820CB044B62299291C0198025401AA00021D1822BC5C100763A4698FB350E6184C00A9820200FAF00244998F67D59998F67D5A93ECB0D6E0164D709A47F5AEB6612D1B1AC788846008780252555097F51F263A1CA00C4D0946B92669EE47315060081206C96208B0B2610E7B389737F3E2006D66C1A1D4ABEC3E1003A3B0805D337C2F4FA5CD83CE7DA67A304E9BEEF32DCEF08A400020B1967FC2660084BC77BAC3F847B004E6CA26CA140095003900BAA3002140087003D40080022E8C00870039400E1002D400F10038C00D100218038F400B6100229500226699FEB9F9B098021A00800021507627C321006E24C5784B160C014A0054A64E64BB5459DE821803324093AEB3254600B4BF75C50D0046562F72B1793004667B6E78EFC0139FD534733409232D7742E402850803F1FA3143D00042226C4A8B800084C528FD1527E98D5EB45C6003FE7F7FCBA000A1E600FC5A8311F08010983F0BA0890021F1B61CC4620140EC010100762DC4C8720008641E89F0866259AF460C015D00564F71ED2935993A539C0F9AA6B0786008D80233514594F43CDD31F585005A25C3430047401194EA649E87E0CA801D320D2971C95CAA380393AF131F94F9E0499A775460'
bits = hex_to_bits(test)
start,output = orch(0)
print('end: ',output)