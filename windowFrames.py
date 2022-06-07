import sys
import argparse
import os 
import cv2

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







''' Function to get a window of 50 frames before and after the frame of '''
def getWindow(dirname):

    # find the video number to be processed 
    if os.path.exists(dirname):

      # get the video number
      vid_num = dirname[-2:]
      print(vid_num)

      # find the corresponding segmentation
      video_segmentation_folder = dirname + '/Labels'
      os.chdir(dirname + '/Labels')
      print(os.getcwd())

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
                wf_path = '/Volumes/WD_Drive/MSc_Project/CATARACTS_WF_2020/Videos/train' + vid_num + '.mp4'

                os.chdir(wf_path)
                print(os.getcwd())




    # find the frame number of the segmentation in the video 
    return 

