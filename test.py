'''
base_url = ''的引号里填地址见readme.md的描述
'User-Agent': ''的引号里填User-Agent见readme.md的描述
'cookie':''的引号里填cookie见readme.md的描述
'clazz_course_id': ''的引号里填clazz_course_id见readme.md的描述
'res_id': ''的引号里填res_id见readme.md的描述
'watch_to': ''的引号里填duration的数据见readme.md的描述
'duration': ''的引号里填duration见readme.md的描述
'current_watch_to': ''的引号里填current_watch_to见readme.md的描述
此时watch_to的数据应该是等于duration的数据
保存并运行即可
'''
import requests
base_url = ''
headers = {
    'User-Agent': '',
    'cookie':''
}
bodys = {
    'clazz_course_id': '',
    'res_id': '',
    'watch_to': '',
    'duration': '',
    'current_watch_to': ''
}
r = requests.post(base_url,data = bodys, headers=headers)
print(r.text)
    

    