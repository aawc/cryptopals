<!-- TOC depthFrom:1 depthTo:1 orderedList:true -->

1. [Convert hex to base64](#convert-hex-to-base64)
2. [Fixed XOR](#fixed-xor)
3. [Single-byte XOR cipher](#single-byte-xor-cipher)
4. [Detect single-character XOR](#detect-single-character-xor)
5. [Repeating-key XOR](#repeating-key-xor)
6. [Break repeating-key XOR](#break-repeating-key-xor)

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
One of the 60-character strings in [this file](sets/1/challenges/4.txt) has been encrypted by single-character XOR. Find it.

(Your code from #3 should help.)

## Solution
See: [s1c4.py](https://github.com/aawc/cryptopals/blob/master/sets/1/challenges/s1c4.py)

# Repeating-key XOR
## Source
[https://cryptopals.com/sets/1/challenges/5](https://cryptopals.com/sets/1/challenges/5)
## Description

## Solution
See: [s1c5.py](https://github.com/aawc/cryptopals/blob/master/sets/1/challenges/s1c5.py)

# Break repeating-key XOR

## Source
[https://cryptopals.com/sets/1/challenges/6](https://cryptopals.com/sets/1/challenges/6)

## Description
### It is officially on, now.
This challenge isn't conceptually hard, but it involves actual error-prone
coding. The other challenges in this set are there to bring you up to speed.
This one is there to qualify you. If you can do this one, you're probably just
fine up to Set 6.

There's a file [here](sets/1/challenges/6.txt). It's been base64'd after being
encrypted with repeating-key XOR.

Decrypt it.

#### Here's how

Let KEYSIZE be the guessed length of the key; try values from 2 to (say) 40.
Write a function to compute the edit distance/Hamming distance between two
strings. The Hamming distance is just the number of differing bits. The distance
between:
```
this is a test
```
and
```
wokka wokka!!!
```
is 37. Make sure your code agrees before you proceed.

##### Step 1
For each KEYSIZE, take the first KEYSIZE worth of bytes, and the second KEYSIZE
worth of bytes, and find the edit distance between them. Normalize this result
by dividing by KEYSIZE.

The KEYSIZE with the smallest normalized edit distance is probably the key. You
could proceed perhaps with the smallest 2-3 KEYSIZE values. Or take 4 KEYSIZE
blocks instead of 2 and average the distances.

##### Step 2
Now that you probably know the KEYSIZE: break the ciphertext into blocks of
KEYSIZE length.

##### Step 3
Now transpose the blocks: make a block that is the first byte of every block,
and a block that is the second byte of every block, and so on.
Solve each block as if it was single-character XOR. You already have code to do
this.

For each block, the single-byte XOR key that produces the best looking histogram
is the repeating-key XOR key byte for that block. Put them together and you have
the key.

This code is going to turn out to be surprisingly useful later on. Breaking
repeating-key XOR ("Vigenere") statistically is obviously an academic exercise,
a "Crypto 101" thing. But more people "know how" to break it than can actually
break it, and a similar technique breaks something much more important.

##### No, that's not a mistake.
```
We get more tech support questions for this challenge than any of the other
ones. We promise, there aren't any blatant errors in this text. In particular:
the "wokka wokka!!!" edit distance really is 37.
```
