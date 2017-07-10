<!-- TOC depthFrom:1 depthTo:1 orderedList:true -->

1. [Convert hex to base64](#convert-hex-to-base64)
2. [Fixed XOR](#fixed-xor)
3. [Single-byte XOR cipher](#single-byte-xor-cipher)
4. [Detect single-character XOR](#detect-single-character-xor)

<!-- /TOC -->

# Convert hex to base64
## Source
[https://cryptopals.com/sets/1/challenges/1](https://cryptopals.com/sets/1/challenges/1)

## Example
### Input
```
49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d
```
### Output
```
SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t
```
## Tip
Always operate on raw bytes, never on encoded strings.
Only use hex and base64 for pretty-printing.
## Solution
See: [s1c1.py](https://github.com/aawc/cryptopals/blob/master/sets/1/challenges/s1c1.py)


# Fixed XOR
## Source
[https://cryptopals.com/sets/1/challenges/2](https://cryptopals.com/sets/1/challenges/2)

## Description
Write a function that takes two equal-length buffers and produces their XOR combination.
## Example
If your function works properly, then when you feed it the example input strings, ```input_1``` and ```input_2```, after hex decoding and when XOR'd against each other, it produces the example output.
### Input
```
input_1:
1c0111001f010100061a024b53535009181c

input_2:
686974207468652062756c6c277320657965
```
### Output
```
746865206b696420646f6e277420706c6179
```
## Solution
See: [s1c2.py](https://github.com/aawc/cryptopals/blob/master/sets/1/challenges/s1c2.py)


# Single-byte XOR cipher
## Source
[https://cryptopals.com/sets/1/challenges/3](https://cryptopals.com/sets/1/challenges/3)
## Description
The hex encoded string:
```
1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736
```

has been XOR'd against a single character. Find the key, decrypt the message.
You can do this by hand. But don't: write code to do it for you.

How? Devise some method for "scoring" a piece of English plaintext.
Character frequency is a good metric.
Evaluate each output and choose the one with the best score.
## Achievement Unlocked
You now have our permission to make "ETAOIN SHRDLU" jokes on Twitter.
## Solution
See: [s1c3.py](https://github.com/aawc/cryptopals/blob/master/sets/1/challenges/s1c3.py)

# Detect single-character XOR
## Source
[https://cryptopals.com/sets/1/challenges/4](https://cryptopals.com/sets/1/challenges/4)
## Description
One of the 60-character strings in [this file](sets/1/challenges/4.txt) has been encrypted by single-character XOR.
Find it.
(Your code from #3 should help.)
