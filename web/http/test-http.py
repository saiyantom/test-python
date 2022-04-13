import requests

#download image
#r=requests.get('https://cdn.hk01.com/di/media/images/dw/20220413/590801733542744064624875.jpeg/B7IcTmY7Zn1MoFQlteiFn8QViF_yNW4eOUB9AzlAfQM?v=w1440r16_9')

#with open('test.jpeg','wb') as f:
#    f.write(r.content)

#HTTP Request get/post
#payload={'pages':10,'count':40}
#r=requests.get('http://httpbin.org/get',params=payload)
#print(r.url)

#payload={'username':'peter','password':'pass'}
#r=requests.post('http://httpbin.org/post',data=payload)
#print(r.json()['headers']['User-Agent'])

#Authentication
#r=requests.get('http://httpbin.org/basic-auth/peter/pass',auth=('peter','pass'))
#print(r.text)

#Delay with timout
#r=requests.get('http://httpbin.org/delay/6',timeout=3)
#r=requests.get('http://httpbin.org/delay/5')
#print(r.text)

#Redirect
payload={'url':'http://tasper.hk'}
r=requests.get('http://httpbin.org/redirect-to',params=payload)
print(r.text)