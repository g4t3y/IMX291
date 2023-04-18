# a workshop in IP conversion
#
# https://www.youtube.com/watch?v=icldNo6reNY

# IP to HEX converter for this repo
# define the variable - DNS server IP for eample
ipa = '192.168.1.1'

print (ipa)

parts = ipa.split('.')
print()
#print(parts[0])

for part in parts:
    print(part)

print()
print('Dec Hex Binary Oct')
for part in parts:
    print ( format(int(part), '03d'), \
            format(int(part), '02X'), \
            format(int(part), '08b'), \
            format(int(part), '03o'), )

print()
print('This appears to be the format the camera expects: 3,2,1,0 instead of 0,1,2,3...')
hexNumber=  format(int(parts[3]), '02X') \
          + format(int(parts[2]), '02X') \
          + format(int(parts[1]), '02X') \
          + format(int(parts[0]), '02X')
print('IP Address in HEX base 16')
print( '0x'+hexNumber )

print()
print()
print('IP Address in HEX2 using a for loop')
hex2='0x'
for part in parts:
    hex2 += format(int(part),'02X')
print (hex2)

print()
print()
print('IP Address in Decimal')
print (int(hex2, base=16))

print()
print()
print('IP Address in Binary')
binaryNumber= \
            format(int(parts[0]),   '08b') \
            + format(int(parts[1]), '08b') \
            + format(int(parts[2]), '08b') \
            + format(int(parts[3]), '08b')

print('0b'+binaryNumber);

print()
print()
bin2='0b'
for part in parts:
    bin2 += format(int(part),'08b')

print('IP Address in binary using a for loop')
print(bin2);

print()
print()
print('IP Address in Octal base 8')
print( 'Oo'+format(int('0x'+hexNumber, base=16), '02o'))
