"""### Converting video to frames"""

import os
import glob

def mkdir_ifnotexists(dir):
    if os.path.exists(dir):
        return
    os.makedirs(dir)

videos = ['Video01', 'Video02', 'Video03', 'Video04', 'Video05', 
        'Video06', 'Video07', 'Video08', 'Video09', 'Video10', 
        'Video11', 'Video12', 'Video13', 'Video14', 'Video15', 
        'Video16', 'Video17', 'Video18', 'Video19', 'Video20',
        'Video21', 'Video22', 'Video23', 'Video24']

for filename in glob.glob('Video02/Images/*.png'):
    img = cv2.imread(filename)

    vid_file='/Volumes/WD_Drive/MSc_Project/Windows/Video01/000090.mp4'
    frame_pth='/Volumes/WD_Drive/MSc_Project/Windows_To_Frames/Video01/000090'
    mkdir_ifnotexists(frame_pth)
    cmd = "ffmpeg -i %s -start_number 0 -vsync 0 %s/frame_%%06d.png" % (
                vid_file,
                frame_pth,
            )
    os.system(cmd)

