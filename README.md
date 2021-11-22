# hex_decimal_converters
Functions for converting values from hexadecimal to decimal and back.

```py
def hex_to_decimal(hex_in):
  global hex_dict
  decimal_out = 0

  list_hex_in = list(hex_in)
  list_hex_in.reverse()

  base = 1
  for i in list_hex_in:
    for k, v in hex_dict.items():
      if v is i:
        decimal_out += k * base
    break
      elif k == 15:
        decimal_out += int(i) * base
    base *= 16
    
  return decimal_out
```


```py
def decimal_to_hex(quotient):
  hex_dict = {
    10: "A",
    11: "B",
    12: "C",
    13: "D",
    14: "E",
    15: "F",
  }

  remainders = []
  while quotient >= 0.1:
    remainder = int(quotient % 16)
    remainders.append(remainder)
    quotient /= 16

  remainders.reverse()

  hex_out = ""
  for char in remainders:
        hex_out += hex_dict[char] if char in hex_dict else str(char)

  hex_out = hex_out[1:]  # trims leading 0
  return hex_out
```
