# API REST JSONPlaceHolder
import json, requests, random

urls = { 
         'comments': 'http://jsonplaceholder.typicode.com/comments',
         'posts'   : 'http://jsonplaceholder.typicode.com/posts',
         'albums'  : 'http://jsonplaceholder.typicode.com/albums',
         'photos'  : 'http://jsonplaceholder.typicode.com/photos',
         'todos'   : 'http://jsonplaceholder.typicode.com/todos',
         'users'   : 'http://jsonplaceholder.typicode.com/users'
       }


response = requests.get(urls['todos'])
data     = json.loads(response.content)

data_len = len(data)

id_post  = random.randint(0, data_len-1)

print(f'\n{data_len}\n')
print(data[id_post])