import imageio
import matplotlib.pyplot as plt
import numpy as np
import glob 
import cv2

# visualising the first frame of Video01
filename = 'CaDISv2/Video01/Labels/Video1_frame000090.png'
label = imageio.imread(filename)

# visualising the first frame of the images 
filename = 'CaDISv2/Video01/Images/Video1_frame000090.png'
im = imageio.imread(filename)

print(np.amin(label), np.amax(label))

# print(im.shape)
plt.imshow(label, vmin=np.amin(label), vmax=np.amax(label), cmap='gray')
plt.show()

# #finding out how many frames are in this video 
# counter = 0
# for filename in glob.glob('Video01/Labels/*.png'):
#     counter += 1

# print('counter is', counter) #177 frames 

# # writing a video using frames from Video01
# img_array = []
# for filename in glob.glob('Video02/Images/*.png'):
#     img = cv2.imread(filename)
#     # img = cv2.cvtColor(img, cv2.COLOR_GRAY2RGB)
#     height, width, layers = img.shape
#     size = (width, height)
#     # size = (height, width, layers)
#     # print(layers)
#     img_array.append(img)

# filename = 'Full Videos/Images/mp4/Video02.mp4'
# out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc(*'XVID'), 15, size, isColor=True)
# # out = cv2.VideoWriter('RGB_Video01_Labels.mp4', cv2.VideoWriter_fourcc(*'XVID'), 15, size, isColor=True)

# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()


# masking an image and seeing this video
# with np.printoptions(threshold=np.inf):
#     print(im)

# # thresholding so only surgical tape (1) shows 
# label[label != 1] = 0
# l, w = label.shape
# label = np.reshape(label, (l, w, 1))
# label = np.repeat(label, 3, axis=2)
# maskedIm = label * im

# plt.imshow(maskedIm)
# plt.show()

# with np.printoptions(threshold=np.inf):
    # print(bool_idx)
