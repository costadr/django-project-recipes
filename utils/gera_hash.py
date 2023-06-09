import string as s
from random import SystemRandom as sr

print(''.join(sr().choices(s.ascii_letters + s.punctuation, k=64)))
