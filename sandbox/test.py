from urllib.parse import urlparse

url = 'https://example.com/images/pic.jpg'
parsed = urlparse(url)

print(parsed)
# ➤ ParseResult(
#     scheme='https',
#     netloc='example.com',
#     path='/images/pic.jpg',
#     params='',
#     query='',
#     fragment=''
# )
