# Generate some random content
import string
import random as r

for counter in range(1, 256):
    content = ''.join(r.choices(string.ascii_letters + string.digits, k=100))
    with open(f'./sn/SN-{counter}', mode='w', encoding="utf-8") as f:
        f.write(content)
