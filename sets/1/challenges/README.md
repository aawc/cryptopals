# 01: Convert hex to base64
## Source
https://cryptopals.com/sets/1/challenges/1
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


# 02: Fixed XOR
## Source
https://cryptopals.com/sets/1/challenges/2
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
