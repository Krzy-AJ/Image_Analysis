
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt 

#%%
class Open_Image:
        def __init__(self, image_path, qx_low, qx_high, num_qx_pixels,
                qy_low, qy_high, num_qy_pixels):
                 
                self.qx = np.linspace(qx_low, qx_high, num=num_qx_pixels) # how should I incorporate this?
                self.qy = np.linspace(qy_low, qy_high, num=num_qy_pixels) # how should I incorporate this?
        
                self.img = Image.open(image_path)
                plt.imshow(self.img)
        
        def img_rotate(self, rotate_angle):

                self.img_rotate = self.img.rotate(rotate_angle)
                plt.imshow(self.img_rotate)
        
        def img_resize(self ):
                self.img_resized = plt.imshow(self.img, 
                        extent=[self.qx[0], self.qx[-1], self.qy[0], self.qy[-1]])


 
test = Open_Image("example_image.tif", 0, 4032, 4032, 0, 3024, 3024)
#%%