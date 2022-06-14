"""### Converting video to frames"""

import os

def mkdir_ifnotexists(dir):
    if os.path.exists(dir):
        return
    os.makedirs(dir)

vid_file='/Volumes/WD_Drive/MSc_Project/Windows/Video01/000090.mp4'
frame_pth='/Volumes/WD_Drive/MSc_Project/Windows_To_Frames/Video01/000090'
mkdir_ifnotexists(frame_pth)
cmd = "ffmpeg -i %s -start_number 0 -vsync 0 %s/frame_%%06d.png" % (
            vid_file,
            frame_pth,
        )
os.system(cmd)

