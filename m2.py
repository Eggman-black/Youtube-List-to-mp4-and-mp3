# -*- coding: utf-8 -*-
import os
import subprocess
import platform
#os.system('pip install pytube')
#os.system('pip install moviepy')
from pytube import *
from moviepy.editor import* 
quality = ['1080p', '720p', '480p', '360p', '240p', '144p']
def progress(stream, chunk, remaining):
    contentSize = stream.filesize
    size = contentSize - remaining
    print('\r' + '[Download progress]:[%s%s]%.2f%%;' % (
    '█' * int(size*20/contentSize), ' '*(20-int(size*20/contentSize)), float(size/contentSize*100)), end='')

name = input('playlistname:')

cnt = 1
while True:
    where = input('playlist\'s url:')
    if(where == 'none'):
        break
    url = where
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
    try:
        os.mkdir('.\\'+name+'\\video_done')
    except:
        print('', end='')
    
    path_video = os.listdir('.\\'+name+'\\music')
    fileobj = {}
    
    for i in path_video:
        
        if(i[-1] == '4'):
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
        
        if(i[-1] == '4'):
            print(i)
            oldname = '.\\'+name+'\\music\\'+i
            newname = '.\\'+name+'\\music\\'+i[:-1]+'3'
            print(oldname+'>>>'+newname)
            #try:
            os.rename(oldname, newname)
            #except:
            #    print('wrong')
    
