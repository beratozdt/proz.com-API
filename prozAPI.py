import requests
import re
result=[]
url="https://www.proz.com/language-jobs"
for i in range(100):
    if i >=1:
        url=url+"?page="+str(i)
    response=requests.api.get(url=url)
    a=response.text
    dumb=re.findall('%s(.*)%s' % ("https://www.proz.com/translation-jobs/", "target"), a)

    if dumb==[]:
        break
    for i in range(len(dumb)):
        result.append("https://www.proz.com/translation-jobs/"+dumb[i])
        if "value._source.job_id" in dumb[i]:
            result = result[:-1]
for i in range(len(result)):
     print(result[i])


