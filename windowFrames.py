import sys
import argparse
import os 
import cv2
import matplotlib.pyplot as plt
import numpy as np


# def extractImages(pathIn, pathOut):
#     count = 0
#     vidcap = cv2.VideoCapture(pathIn)
#     success,image = vidcap.read()
#     success = True
#     while success:
#         vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
#         success,image = vidcap.read()
#         print ('Read a new frame: ', success)
#         cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
#         count = count + 1

# if __name__=="__main__":
#     a = argparse.ArgumentParser()
#     a.add_argument("train01.mp4", help="path to video")
#     a.add_argument("TESTtrain01.mp4", help="path to images")
#     args = a.parse_args()
#     print(args)
#     extractImages(args.pathIn, args.pathOut)



''' Function to generate a video from the frames extracted in the window centered on the segmentation image'''
def genVideo(video_arr, save_path, frame_rate, frame_num): 

  if not os.path.exists(save_path):
    os.mkdir(save_path)

  out = cv2.VideoWriter(save_path, cv2.VideoWriter_fourcc(*'XVID'), frame_rate, (video_arr.shape[1], video_arr.shape[0]), isColor=True)

  for i in range(len(video_arr)):
      out.write(video_arr[i])
  out.release()

  return 











''' Function to get the frames extracted from the window centered on the segmentation'''
def getWindow(wf_file, save_path, frame_num, windowSize):

  count = 0 

  # open the workflow video file
  vidcap = cv2.VideoCapture(wf_file)

  # get frame rate 
  frame_rate = vidcap.get(cv2.CAP_PROP_FPS)

  # find the time stamp (in ms) in the video footage to be extracted
  time_stamp = 1000 * int(frame_num) / frame_rate

  # find the time stamp (in ms) of n frames before the frame with segmentation
  # will do this when I change window to be in terms of frames

  # define the window to extract frames from
  windowStart, windowEnd = time_stamp - windowSize, time_stamp + windowSize

  time = windowStart
  video_arr = []

  while time < windowEnd:

    # go to the frame at the point of interest 
    vidcap.set(cv2.CAP_PROP_POS_MSEC, time)

    # read the image array for the frame at this point
    success, image = vidcap.read()

    if success:
      
      # add this image to the array 
      video_arr.append(image)
      # np.append(video_arr, image)

      # this will capture a window of 20 frames for a window size of 250 ms
      time += 25

  video_arr = np.array(video_arr)
  shapetest = video_arr.shape

  # make the array of frames in the window into a video 
  genVideo(video_arr, save_path, frame_rate, frame_num)

  # my_test = len(video_arr)
  # plt.imshow(video_arr[10], vmin=np.amin(video_arr[1]), vmax=np.amax(video_arr[10]), cmap='brg')

  return 













''' Function to get a window of 50 frames before and after the frame of '''
def generateFlows(dirname, windowSize):

  # find the video number to be processed 
  if os.path.exists(dirname):

    # get the video number
    vid_num = dirname[-2:]

    # find the corresponding segmentation
    video_segmentation_folder = dirname + '/Labels'
    os.chdir(dirname + '/Labels')

    # loop through all the segmentations in this directory
    for filename in os.listdir(video_segmentation_folder):

      # ignoring hidden files
      if not filename.startswith('.'):
          segmentation = os.path.join(video_segmentation_folder, filename)

          # checking if it is a file
          if os.path.isfile(segmentation):
              
              # find the frame number 
              frame_num = os.path.splitext(filename)[0][-6:]

              # find the corresponding video in the workflow folder 
              wf_file = '/Volumes/WD_Drive/MSc_Project/CATARACTS_WF_2020/Videos/train' + vid_num + '.mp4'
              
              # define save path for window centered on segmentation 
              save_path = '/Volumes/WD_Drive/MSc_Project/Windows/Video' + vid_num 

              # generate video for the window of frames centered on segmentation
              getWindow(wf_file, save_path, frame_num, windowSize)
  return 

