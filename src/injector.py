from datetime import datetime

class injector() :
    def __init__(self, result_directory, media_directory) :
        self.result_directory = result_directory
        self.media_directory = media_directory
    
    def get_photo_creation_time(self, file_name) : 
        file_name_YYYYMMDD = file_name.split('_')[1]
        file_name_hhmmss = file_name.split('_')[2][:5]
        
        creation_time = datetime.strptime(file_name_YYYYMMDD + file_name_hhmmss, "%Y%m%d%H%M%S").strftime("%Y:%m:%d %H:%M:%S") #YYYY:MM:DD HH:MM:SS
        return creation_time
    
    def get_video_creation_time(self, file_name) :
        file_name_YYYYMMDD = file_name.split('_')[1]
        file_name_hhmmss = file_name.split('_')[2][:5]
        file_name_sss = file_name.split('_')[2][5:7]
        
        creation_time = datetime.strptime(file_name_YYYYMMDD + file_name_hhmmss + '.' + file_name_sss, "%Y%m%d%H%M%S.%f").isoformat() #ISO 8601
        return creation_time
    
    def inject_metadata(self, file_list) :
        pass