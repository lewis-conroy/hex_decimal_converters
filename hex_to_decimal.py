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
