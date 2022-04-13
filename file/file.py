import os, requests

#Open file
#with open('file01.txt','r') as f:
#    print(f.read())
#    print(f.readline())
#    chunk_size=100
#    rf_chunk=f.read(chunk_size)
#    print(rf_chunk,end='&')

#Copy file
with open('file02.txt','r') as rf:
    with open('file03.txt','w') as wf:
        chunk_size=100
        rf_chunk=rf.read(chunk_size)
        while len(rf_chunk)>0:
            wf.write(rf_chunk)
            rf_chunk=rf.read(chunk_size)

#Copy Image file
r=requests.get('https://cdn.discuss.com.hk/t/0fe0cb/f/800x0/https://newsstatic.rthk.hk/images/mfile_1643671_1_L_20220412193658.jpg')
with open('test.jpg','wb') as f2:
    f2.write(r.content)

#Delete file
if os.path.exists('file03.txt'):
    os.remove('file03.txt')
else:
    print("File doesn't exist")
