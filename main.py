from src.photo_injector import photo_injector
from src.video_injector import video_injector

import os

def check_media_type(extension) :
    photo_extension = ["jpg", "png"]
    video_extension = ["mp4", "avi"]
    
    if extension in photo_extension :
        return 1
    elif extension in video_extension :
        return 2
    else :
        return 0

if __name__ == "__main__" : 
    script_directory = os.path.abspath(os.path.dirname(__file__))
    
    result_directory = script_directory + "/result"
    os.makedirs(result_directory, exist_ok=True)
    
    media_directory = script_directory + "/media"
    media_files = os.listdir(media_directory)
    
    photo = photo_injector(result_directory, media_directory)
    video = video_injector(result_directory, media_directory)
    
    photo_list = list()
    video_list = list()
    
    for file_name in media_files : 
        if file_name.split('_')[0] != "KakaoTalk" :
            continue
        extension = file_name.split('.')[1]
        media_type = check_media_type(extension)
        
        if media_type != 0 :
            if media_type == 1 :
                photo_list.append(file_name)
            elif media_type == 2 :
                video_list.append(file_name)
    
    photo.inject_metadata(photo_list)
    video.inject_metadata(video_list)