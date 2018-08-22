
# coding: utf-8

# In[7]:


#Converter várias frames em um vídeo
import os
import cv2


dir_path = r'C:\Users\username\Desktop\dir_images'

os.chdir(dir_path)

images = []



for f in os.listdir():
    if(f.endswith('jpg')):
        images.append(f)

image_path = os.path.join(dir_path, images[0])
frame = cv2.imread(image_path)
cv2.imshow('video',frame)
height, width, channels = frame.shape

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('video.avi', fourcc, 14.0, (width, height))

for image in images:
    image_path = os.path.join(dir_path, image)
    frame = cv2.imread(image_path)
    
    out.write(frame)
    
    cv2.imshow('video', frame)
    
    if(cv2.waitKey(1) & 0xFF) == ord('q'):
        break

out.release()
cv2.destroyAllWindows()

