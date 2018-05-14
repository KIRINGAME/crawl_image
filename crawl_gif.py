
import os
import requests
from lxml import html

headers = {
    # 'Host': 'www.****.com',
    # 'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    # 'Accept-Encoding': 'gzip, deflate, sdch, br',
    # 'Connection': 'keep-alive',
    # 'Pragma': 'no-cache',
    # 'Cache-Control': 'no-cache',
    # 'Upgrade-Insecure-Requests': '1',
    # 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    # 'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) '
    #               'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
}

#存储文件
def save(page, fpath):
    if os.path.exists(fpath):
        print('exist '+ fpath)
        return
    with open(fpath, 'wb') as f:
        print('output:', fpath)
        f.write(page)

#存储图片
def save_image(image_url, path):
    try:
        resp = requests.get(image_url)
        page = resp.content
        filename = image_url.split('/')[-1]
        fpath = os.path.join(path, filename)
        save(page, fpath)
    except BaseException:
        print("error:"+image_url)


#获取图片文件路径
def getimage_url_info(url, info):
    path = "download/" + info
    if not os.path.exists(path):
        os.makedirs(path)
    resp = requests.get(url, headers=headers)
    page = resp.content
    root = html.fromstring(page)
    image_urls = root.xpath("//img[contains(@src,'.gif')]/@src")

    for image_url in image_urls:
        save_image(image_url, path)

#根据论坛分页爬每页的图片
def crawl_image(url_pre, page_num, url):

    resp = requests.get(url, headers=headers)

    page = resp.content
    root = html.fromstring(page)

    # _all_urls_node1 = root.xpath("//td/h3/a[contains(@href,'htm_data')]")
    _all_urls_node = root.xpath("//a[contains(text(),'gif')]")
    _all_urls_node2 = root.xpath("//a[contains(text(),'GIF')]")
    _all_urls_node3 = root.xpath("//a[contains(text(),'动图')]")
    _all_urls_node.extend(_all_urls_node2)
    _all_urls_node.extend(_all_urls_node3)

    for i in _all_urls_node:
        url_list = i.xpath('@href')
        info_list = i.xpath('text()')
        url = ""
        info = ""
        if len(url_list) != 0 :
            url = url_list[0]
        else:
            continue
        if len(info_list) != 0:
            info = info_list[0]
        else:
            continue
        getimage_url_info(url_pre + url, info)


#爬100页分页
if __name__ == '__main__':
    url_pre = 'http://****.com/'
    num_min = 1
    num_max = 100

    url_list_pre = url_pre+'thread0806.php?fid=7&search=&page='

    for i in range(num_min, num_max):
        url = url_list_pre + str(i)
        crawl_image(url_pre, "page_"+str(i), url)

