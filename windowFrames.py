import sys
import argparse
import os 
import cv2

def extractImages(pathIn, pathOut):
    count = 0
    vidcap = cv2.VideoCapture(pathIn)
    success,image = vidcap.read()
    success = True
    while success:
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        cv2.imwrite( pathOut + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
        count = count + 1

if __name__=="__main__":
    a = argparse.ArgumentParser()
    a.add_argument("train01.mp4", help="path to video")
    a.add_argument("TESTtrain01.mp4", help="path to images")
    args = a.parse_args()
    print(args)
    extractImages(args.pathIn, args.pathOut)



def getWindow(wf_file, save_path, frame_num):

  count = 0 

  # open the workflow video file
  vidcap = cv2.VideoCapture(wf_file)

  # access the image array 
  success, image = vidcap.read()
  # success = True

  # if video successfully read
  while success:
    # fps is 30 fps
    print(vidcap.get(cv2.CAP_PROP_FPS))


      # vidcap.set(cv2.CAP_PROP_POS_MSEC,(count*1000))    # added this line 
      # success,image = vidcap.read()
      # print ('Read a new frame: ', success)
      # cv2.imwrite(save_path + "\\frame%d.jpg" % count, image)     # save frame as JPEG file
      # count = count + 1
  

  return 



''' Function to get a window of 50 frames before and after the frame of '''
def generateFlows(dirname):

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
              save_path = '/Volumes/WD_Drive/MSc_Project/Windows/Video' + vid_num + '/'

              # generate video for the window of frames centered on segmentation
              getWindow(wf_file, save_path, frame_num)
  return 

