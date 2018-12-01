#!/usr/bin/env python3
import re
import math
'''
Revature is building a new API! This API contains functions for validating data, 
solving problems, and encoding data. 

The API consists of 10 functions that you must implement.

Guidelines:
1) Edit the file to match your first name and last name with the format shown.

2) Provide tests in the main method for all functions, We should be able to run
this script and see the outputs in an organized manner.

3) You can leverage the operating system if needed, however, do not use any non
legacy command that solves the problem by just calling the command.

4) We believe in self commenting code, however, provide comments to your solutions
and be organized.

5) Leverage resources online if needed, but remember, be able to back your solutions
up since you can be asked.

6) Plagiarism is a serious issue, avoid it at all costs.

7) Don't import external libraries which are not python native

8) Don't change the parameters or returns, follow the directions.

9) Assignment is optional, but totally recommend to achieve before Monday for practice.

Happy Scripting!

© 2018 Revature. All rights reserved.
'''

'''
Use the main function for testing purposes and to show me results for all functions.
'''
def main():
	print(reverse('Hello World'))
	print(acronym('Big   Friendly -- =  Gaint'))
	print(acronym('Complementry metal-oxide semiconductors'))
	print(whichTriangle(1, 2, 3))
	print(whichTriangle(1, 1, 1))
	print(whichTriangle(2, 2, 3))
	print(whichTriangle(1, 2, 2))
	print(whichTriangle(1, 2, 1))
	print(str(scrabble("Hello")))
	print(str(scrabble("quick")))
	print(str(scrabble("qzk")))
	print(str(scrabble("aeiou")))
	print('armstrong(153) = ', str(armstrong(153)))
	print('armstrong(154) = ', str(armstrong(154)))
	print('primeFactors(27) = ', str(primeFactors(27)))
	print('primeFactors(25) = ', str(primeFactors(25)))
	print('primeFactors(26) = ', str(primeFactors(26)))
	print('primeFactors(101) = ', str(primeFactors(101)))
	print('primeFactors(60) = ', str(primeFactors(60)))
	print('primeFactors(8) = ', str(primeFactors(8)))
	print('primeFactors(8) = ', str(primeFactors(8)))
	print('pangram("hello") = ', str(pangram('hello')))
	print('pangram("The quick brown fox jumped over the lazy dog.") = ', str(pangram('The quick brown fox jumps over the lazy dog.')))
	

'''
1. Reverse a String. Example: reverse("example"); -> "elpmaxe"

Rules:
- Do NOT use built-in tools
- Reverse it your own way

param: str
return: str
'''
def reverse(string):
	slist = list(string)
	i = 0
	j = len(string) - 1
	while(i < j):
		tmp = slist[i]
		slist[i] = slist[j]
		slist[j] = tmp
		i += 1
		j -= 1
	return ''.join(slist)

	#all done in one line
	#return string[::-1]
'''
2. Convert a phrase to its acronym. Techies love their TLA (Three Letter
Acronyms)! Help generate some jargon by writing a program that converts a
long name like Portable Network Graphics to its acronym (PNG).

param: str
return: str
'''
def acronym(phrase):
	split = re.split('[^a-zA-Z0-9]', phrase)
	output = ""
	for s in split:
		s = s.strip()
		if len(s) > 0:
			output += s[0]
	return output.upper()
'''
3. Determine if a triangle is equilateral, isosceles, or scalene. An
equilateral triangle has all three sides the same length. An isosceles
triangle has at least two sides the same length. (It is sometimes specified
as having exactly two sides the same length, but for the purposes of this
exercise we'll say at least two.) A scalene triangle has all sides of
different lengths.

param: float, float, float
return: str -> 'equilateral', 'isoceles', 'scalene'
'''
def whichTriangle(sideOne, sideTwo, sideThree):
	if sideOne == sideTwo or sideOne == sideThree or sideTwo == sideThree:
		if sideOne == sideTwo and sideOne == sideThree:  
			return 'equilateral'
		return 'isoceles'
	return 'scalene'

'''
4. Given a word, compute the scrabble score for that word.

--Letter Values-- Letter Value A, E, I, O, U, L, N, R, S, T = 1; D, G = 2; B,
C, M, P = 3; F, H, V, W, Y = 4; K = 5; J, X = 8; Q, Z = 10; Examples
"cabbage" should be scored as worth 14 points:

3 points for C, 1 point for A, twice 3 points for B, twice 2 points for G, 1
point for E And to total:

3 + 2*1 + 2*3 + 2 + 1 = 3 + 2 + 6 + 3 = 5 + 9 = 14

param: str
return: int
'''
def scrabble(word):
	alpha = '1AEIOULNRST 2DG 3BCMP 4FHVWY 5K 8JX 0QZ'
	alphaMap = {}
	value = 0	
	for c in alpha:
		if c == '0':
			value = 10
		elif c >= '1' and c <= '9':
			value = int(c)
		else:
			alphaMap[c] = value
	score = 0
	for c in word.upper():
		score += alphaMap[c]
	return score

'''
5. An Armstrong number is a number that is the sum of its own digits each
raised to the power of the number of digits.

For example:

9 is an Armstrong number, because 9 = 9^1 = 9 10 is not an Armstrong number,
because 10 != 1^2 + 0^2 = 2 153 is an Armstrong number, because: 153 = 1^3 +
5^3 + 3^3 = 1 + 125 + 27 = 153 154 is not an Armstrong number, because: 154
!= 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190 Write some code to determine whether
a number is an Armstrong number.

param: int
return: bool
'''
def armstrong(number):
	sum = 0
	strNum = str(number)
	length = len(strNum)
	for n in strNum:
		sum += int(n) ** length
	return number == sum
		
'''
6. Compute the prime factors of a given natural number.

A prime number is only evenly divisible by itself and 1.
 
Note that 1 is not a prime number.

param: int
return: list
'''
def primeFactors(number):
	factors = []
	while(number % 2 == 0):
		factors.append(2)
		number = number // 2
	
	i = 3
	while i <= math.sqrt(number):
		while number % i == 0:
			factors.append(i)
			number = number // i
		i += 2
	if number > 2:
		factors.append(number)
	return factors	


'''
7. Determine if a sentence is a pangram. A pangram (Greek: παν γράμμα, pan
gramma, "every letter") is a sentence using every letter of the alphabet at
least once. The best known English pangram is:

The quick brown fox jumps over the lazy dog.
 
The alphabet used consists of ASCII letters a to z, inclusive, and is case
insensitive. Input will not contain non-ASCII symbols.
 
param: str
return: bool
'''
def pangram(sentence):
	alphaSet = set()
	sentence = re.sub('[^a-z]', '', sentence.lower())
	for c in sentence:
		alphaSet.add(c)
	return len(alphaSet) == 26
	
'''
8. Sort list of integers.
f([2,4,5,1,3,1]) = [1,1,2,3,4,5]

Rules:
- Do NOT sort it with .sort() or sorted(list) or any built-in tools.
- Sort it your own way

param: list
return: list
'''
def sort(numbers):
	print("sort not defined")
	
'''
9. Create an implementation of the rotational cipher, also sometimes called
the Caesar cipher.

The Caesar cipher is a simple shift cipher that relies on transposing all the
letters in the alphabet using an integer key between 0 and 26. Using a key of
0 or 26 will always yield the same output due to modular arithmetic. The
letter is shifted for as many values as the value of the key.

The general notation for rotational ciphers is ROT + <key>. The most commonly
used rotational cipher is ROT13.

A ROT13 on the Latin alphabet would be as follows:

Plain: abcdefghijklmnopqrstuvwxyz Cipher: nopqrstuvwxyzabcdefghijklm It is
stronger than the Atbash cipher because it has 27 possible keys, and 25
usable keys.

Ciphertext is written out in the same formatting as the input including
spaces and punctuation.

Examples: ROT5 omg gives trl ROT0 c gives c ROT26 Cool gives Cool ROT13 The
quick brown fox jumps over the lazy dog. gives Gur dhvpx oebja sbk whzcf bire
gur ynml qbt. ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. gives The
quick brown fox jumps over the lazy dog.

param: int, str
return: str
'''
def rotate(key, string):
	print("rotate not implemented")
'''	
10. Take 10 numbers as input from the user and store all the even numbers in a file called even.txt and
the odd numbers in a file called odd.txt.

param: none, from the keyboard
return: nothing
'''
def evenAndOdds():
	print("evenAndOdds not implemented")

if __name__ == "__main__":
    main()
