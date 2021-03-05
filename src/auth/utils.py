import random
import string
 
 
def generate_token() -> str:
  token = ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(200))
  return token