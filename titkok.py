
import requests
import json
import re
 
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'cache-control': 'max-age=0',
 # This seems to be very important
    'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Mobile Safari/537.36',
}
 
 
def download(url):
    """
 Download TikTok video without watermark
    """
 # Get interface parameters
    html = requests.get(url=url, headers=headers)
    title = re.findall('itemId: "(.*?)",', html.text)[0]
    dytk = re.findall('dytk: "(.*?)" }', html.text)[0]
 
 # Splicing interface
    url_item = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + title + '&dytk=' + dytk
 
 # Get TikTok video link without watermark
    html_item = requests.get(url=url_item, headers=headers)
 # String to dictionary
    content = json.loads(html_item.text)
 
 # Video interface
    url_video = content['item_list'][0]['video']['play_addr']['url_list'][1]
    response = requests.get(url_video, headers=headers, allow_redirects=True)
 
 # Get the redirected link, this is also the download link of the video without watermark, but it is useless this time
    redirect = response.url
    print(redirect)
 
 # The video is binary and requires this kind of download method
    video = requests.get(url_video, headers=headers).content
    video_name = "douyin.mp4"
    with open(video_name, 'wb') as f:
        f.write(video)
        f.flush()
 Print("Download complete")
 
 
if __name__ == '__main__':
 # Douyin link
    url = 'https://v.douyin.com/XJj85H/'
    download(url)
