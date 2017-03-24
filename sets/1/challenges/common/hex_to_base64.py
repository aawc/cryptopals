import base64


def HexToBase64(hex_input):
  hex_decoded = hex_input.decode("hex")
  base64_encoded = base64.b64encode(hex_decoded)
  return base64_encoded

def main():
  assert "3q2+7w==" == HexToBase64("deadbeef"), HexToBase64("deadbeef")
  assert "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t" == (
    HexToBase64(
      "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f697"
      "36f6e6f7573206d757368726f6f6d"))

if __name__ == "__main__":
  main()
