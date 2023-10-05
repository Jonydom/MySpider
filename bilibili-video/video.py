import re
import json
import requests
import subprocess
from pprint import pprint

cookie = """i-wanna-go-back=-1; buvid4=96796CFA-5393-664B-B1A3-8582EE7E579126286-022061412-1a0soFqTHEM5amqdyPQhzg%3D%3D; buvid_fp_plain=undefined; DedeUserID=471601657; DedeUserID__ckMd5=b178cdd4790f5a1d; CURRENT_BLACKGAP=0; LIVE_BUVID=AUTO4916682636265781; rpdid=|(J|)RY~J)m)0J'uYYmku~Ym|; fingerprint=70a6b4c95ddadd9573e94601db8a112a; buvid_fp=52f2638964d8c774754193d4ccb047d8; CURRENT_PID=c3c99910-d202-11ed-bb7c-f55dae439595; header_theme_version=CLOSE; FEED_LIVE_VERSION=V_TOPSWITCH_FLEX; buvid3=0ECD8400-F782-5E07-0383-87F6FBF92B4724321infoc; b_nut=1687320024; _uuid=8A8C8442-CC14-E1DE-398B-F35F103122DAC27499infoc; b_ut=5; nostalgia_conf=-1; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTY1OTQyMjMsImlhdCI6MTY5NjMzNDk2MywicGx0IjotMX0.HWL_H6Vt0aONNos8XG5Yhmpe2MMdxcOQKjted962YrU; bili_ticket_expires=1696594163; SESSDATA=5496807a%2C1711887036%2C98db9%2Aa2CjABPF8S0C3GV22w4Dfd3RWzVmPeE-N_tDYHAkEriQXTStuLbY3FJH8tyrkK_XJUUPUSVmMxNVJKZUd6VE9QQ3F4M3RPNkduNTVFUmlyYUJ2aWNfdkMzVmdwbGFMOTdoaUdZNkR0RlMwTk50dzl2LTA0dDE2RjZvazlveFlvR2tTWmQyQmNwcHd3IIEC; bili_jct=b07ee55c60e9d1d8bc354f408612344c; Hm_lvt_8dabccb80a103a16cdfecde99700b220=1696337302; home_feed_column=4; browser_resolution=1280-643; is-2022-channel=1; sid=5nr1mddl; share_source_origin=WEIXIN; CURRENT_FNVAL=4048; bsource=search_google; CURRENT_QUALITY=80; PVID=9; bp_video_offset_471601657=848975211766218825; b_lsid=101E437C8_18AFFC90AEF"""


headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
    "Referer": "https://www.bilibili.com/"
}

def get_response(url):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response
    except:
        print(url + "请求失败")
        return None

def get_video_info(html_url):
    response = get_response(html_url)
    title = re.findall(r'<title data-vue-meta="true">(.*?)_哔哩哔哩_bilibili</title>', response.text)[0]
    html_data = re.findall(r'<script>window.__playinfo__=(.*?)</script>', response.text)[0]
    print(html_data)
    # 将字符串转换成字典
    json_data = json.loads(html_data)
    # 修改视频清晰度
    # json_data['data']['quality'] = json_data['data']['accept_quality'][0]
    # print(json_data['data']['accept_quality'][0])
    # json字典根据键值对取值
    # pprint(json_data['data']['dash']['video'][0])
    # pprint(json_data['data']['dash']['video'][1])
    # pprint(json_data['data']['dash']['video'][2])
    audio_url = json_data['data']['dash']['audio'][0]['baseUrl']
    video_url = json_data['data']['dash']['video'][0]['baseUrl']
    video_info = [title, audio_url, video_url]
    return video_info

def save(title, audio_url, video_url):
    # 保存视频、音频 图片 都是二进制数据
    audio_url_content = get_response(audio_url).content
    video_url_content = get_response(video_url).content
    with open(title+".mp3", "wb") as f:
        f.write(audio_url_content)
    with open(title+".mp4", "wb") as f_1:
        f_1.write(video_url_content)
    print(title+"视频内容保存完成")


def merge_video_audio(video_name):
    print("视频合成开始：", video_name)
    cmd = f"ffmpeg -i {video_name}.mp4 -i {video_name}.mp3 -vcodec copy -acodec copy {video_name}_output.mp4"
    subprocess.run(cmd, shell=True)
    print("视频合成结束：", video_name)


html_url = "https://www.bilibili.com/video/BV1AN411J7Jz"
video_info = get_video_info(html_url)
pprint(video_info)
# save(video_info[0], video_info[1], video_info[2])
# merge_video_audio(video_info[0])
