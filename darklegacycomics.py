import os, requests, bs4
url='http://www.darklegacycomics.com/newest'
os.makedirs('darklegacycomics', exist_ok=True)
while not url.endswith('/1'):
    print('Downloading page %s ...'%url)
    res=requests.get(url)
    res.raise_for_status()
    
    soup=bs4.BeautifulSoup(res.text)
    comicElem=soup.select('img.comic-image')
    if comicElem==[]:
        print('Could not find comic image.')
    else:
        comicUrl=comicElem[0].get('src')
        comicUrl2='http://www.darklegacycomics.com/'+comicUrl
        print('Downloading image %s ...'%(comicUrl))
        res = requests.get(comicUrl2)
        res.raise_for_status()
        imageFile=open(os.path.join('darklegacycomics',os.path.basename(comicUrl)),'wb')
        for chunk in res.iter_content(100000):
            imageFile.write(chunk)
        imageFile.close()
    prevLink=soup.select('a[title="Previous"]')[0]
    url= 'http://www.darklegacycomics.com/'+prevLink.get('href')
print('Done.')
    
