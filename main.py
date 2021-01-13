# -*- coding: utf-8 -*-
import os
import subprocess
import platform
#os.system('pip install pytube')
#os.system('pip install moviepy')
from pytube import *
from moviepy.editor import* 
def progress(stream, chunk, remaining):
    contentSize = stream.filesize
    size = contentSize - remaining
    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

name = input('playlistname:')
where = input('playlist\'s url:')
cnt = 1

pl = Playlist(where)

quality = ['1080p', '720p', '480p', '360p', '240p', '144p']
for s in pl:
    print(cnt,'/',len(pl), ' url:'  , s)
    url = s
    yt = YouTube(url, on_progress_callback=progress)
    audio = yt.streams.filter(type = 'audio').first()
    audio.download('.\\'+name+'\\music')
    for q in quality:
        try:
            v = yt.streams.filter(type="video", resolution=q).first()
            v.download('.\\'+name+'\\video')
            print('quality is '+q)
            break
        except:
            continue
    print(cnt, 'done')
    cnt+=1

try:
    os.mkdir('.\\'+name+'\\video_done')
except:
    print('', end='')
path_video = os.listdir('.\\'+name+'\\video')
fileobj = {}
print(path_video)

for i in path_video:
    print(i)
    temp_video = '.\\'+name+'\\video\\'+i
    temp_audio = '.\\'+name+'\\music\\'+i
    temp_output = '.\\'+name+'\\video_done\\'+i
    
    cmd = f'C:\\ffmpeg-N-100606-ga0acc44106-win64-gpl-shared-vulkan\\bin\\ffmpeg -i \"{temp_video}\" -i \"{temp_audio}\" -map 0:v -map 1:a -c copy -y \"{temp_output}\"'
    status = subprocess.call(cmd, shell=True)
    if status == 0:
        # 視訊檔重新命名
        print('視訊和聲音合併完成')
    #except:
    else:
        print('視訊和聲音合併失敗')

path_aduio = os.listdir('.\\'+name+'\\music')
for i in path_aduio:
    print(i)
    oldname = '.\\'+name+'\\music\\'+i
    newname = '.\\'+name+'\\music\\'+i[:-4]+'.mp3'
    print(oldname+'>>>'+newname)
    os.rename(oldname, newname)
    

