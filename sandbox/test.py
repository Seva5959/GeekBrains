import re

name = re.search(r"/([^.]+)", "https://wikipedia.org").group(1)
print(name)  # wikipedia
