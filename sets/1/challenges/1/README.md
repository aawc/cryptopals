# Convert hex to base64

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
