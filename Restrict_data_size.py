from PIL import Image
import os

img_path = "satisfact_data/cats"

for file in os.listdir(img_path): 
    if file.split('.')[-1]=='jpg': 
        img = Image.open(os.path.join(img_path,file)) 
        img.close()
        size = list(img.size) 
        if size[0] > 224 and size[1] > 224: 
            pass 
        if size[0]*size[1] < 105000: 
            pass 
        else: 
            os.remove(os.path.join(img_path,file)) 
            print(file)



