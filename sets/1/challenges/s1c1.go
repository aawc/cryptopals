package main

import (
    "encoding/base64"
		"encoding/hex"
    "fmt"
		"log"
)

func main() {
	const input = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d";
	fmt.Printf("input, as hex: %s\n", input)

	decoded, err := hex.DecodeString(input)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("input, decoded: %s\n", decoded)

	encoded := base64.StdEncoding.EncodeToString([]byte(decoded))
	fmt.Printf("encoded: %s\n", encoded)
}
