#!/usr/bin/env python3

import binascii

def main() -> None :
	with open("data.txt") as f:
		data : str = f.read()
	
	decoded : bytes = binascii.unhexlify(data)
	decoded : str = decoded.decode('utf-8', 'ignore')
 
	result : str = ''
	for ch in decoded:
		if ch == '\x7f':  # ascii DEL
			result = result[:-1]
		else:
			result += ch

	print(result)

if __name__ == '__main__':
	main()