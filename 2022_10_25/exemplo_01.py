#pip install feedparser

import feedparser

url = 'http://rss.uol.com.br/feed/tecnologia.xml'
#url = 'https://g1.globo.com/rss/g1/tecnologia/'

noticias = feedparser.parse(url)

print(noticias.keys())