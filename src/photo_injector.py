from src.injector import injector

from PIL import Image
import piexif

class photo_injector(injector) :
    def __init__(self, result_directory, media_directory) :
        super().__init__(result_directory, media_directory)
    
    def inject_metadata(self, file_list):
        for photo_name in file_list :
            try : 
                result_photo = Image.open(self.media_directory + "/" + photo_name)
                creation_time = self.get_photo_creation_time(photo_name).encode("utf-8")
                
                exif_data = result_photo.info.get("exif")
                if exif_data :
                    return
                else :
                    exif_dictionary = {"0th": {}, "Exif": {}, "GPS": {}, "1st": {}, "thumbnail": None}
                    exif_dictionary["Exif"][piexif.ExifIFD.DateTimeOriginal] = creation_time
                    exif_dictionary["Exif"][piexif.ExifIFD.DateTimeDigitized] = creation_time
                
                    exif_bytes = piexif.dump(exif_dictionary)
                    result_photo.save(self.result_directory + "/" + photo_name, exif=exif_bytes)
                    
                    print(photo_name + " is Finished")
                
            except Exception as e:
                print("Error : ", e)