from src.injector import injector

from mutagen.mp4 import MP4
import shutil

class video_injector(injector) :
    def __init__(self, result_directory, media_directory) :
        super().__init__(result_directory, media_directory)
    
    def inject_metadata(self, file_list):
        for video_name in file_list :
            try :
                shutil.copy2(self.media_directory + "/" + video_name, self.result_directory + "/" + video_name)
                
                video = MP4(self.result_directory + "/" + video_name)
                video["©day"] = self.get_video_creation_time(video_name)
                video.save()
                
                print(video_name + " is Finished")
                
            except Exception as e:
                print("Error : ", e)