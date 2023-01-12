# https://developers.google.com/youtube/v3/docs
import requests
from urllib import parse

API_TOKEN = 'YOUR_API_KEY'
strTOKEN  = f'&key={API_TOKEN}' if API_TOKEN else ''

strURL    = 'YOUR_CHANNEL_ORIGIN'

# Decompondo a URL
strURLAnalisada = parse.urlparse(strURL)
print('\n'+'-'*100)
print('URL Decomposta')
print(strURLAnalisada)

# Montando Dicionário com resultado da URL analisada  
tuplaHeaders = ('scheme','netloc','path','params','query','fragment')
dictParametros = dict(zip(tuplaHeaders, strURLAnalisada))
print('\n'+'-'*100)
print('Dicionário com resultado da URL analisada')
print(dictParametros)

# Montando URL de requisição - Playlists do Canal
print('\n'+'-'*100)
print('URL de Requisição')
strURLReqChannel   = f'https://youtube.googleapis.com/youtube/v3/playlists?part=snippet'
strChannelID       = dictParametros['path'].replace('/channel/','')
strURLReqChannel  += f'&channelId={strChannelID}{strTOKEN}'
print(strURLReqChannel)


# Requisição de metadados do canal
resposta = requests.get(strURLReqChannel).json()


# Montando URL de requisição - URLs Playlists do Canal
print('\n'+'-'*100)
print('Resultado da Requisição - URLs Playlist do Canal')
lstCanais = list()
strURLReqPlaylist = 'https://youtube.googleapis.com/youtube/v3/playlistItems?part=snippet'
for i in resposta['items']:
   strURLPlaylist  = strURLReqPlaylist
   strURLPlaylist += f'&playlistId={i["id"]}{strTOKEN}'
   lstCanais.append(strURLPlaylist)
print(lstCanais)

# Obter link dos vídeos de cada canal