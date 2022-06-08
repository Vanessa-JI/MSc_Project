import windowFrames

# specify video to create optical flows for 
video = 'Video02'

videos = ['Video01', 'Video02', 'Video03', 'Video04', 'Video05', 
        'Video06', 'Video07', 'Video08', 'Video09', 'Video10', 
        'Video11', 'Video12', 'Video13', 'Video14', 'Video15', 
        'Video16', 'Video17', 'Video18', 'Video19', 'Video20',
        'Video21', 'Video22', 'Video23', 'Video24']

for vid in videos:

    # size of window - this is how many frames before and after we'll capture
    # will change this at some point to be in terms of frames instead of time 
    windowSize = 250 # time in milliseconds 

    # dirname for now is the directory of the video e.g. 'Video01', but will change in the future to CaDISv2 and loop through this 
    dirname = '/Users/vanessaigodifo/Library/CloudStorage/OneDrive-UniversityCollegeLondon/MSc_Project/Dataset/CaDISv2/' + vid 
    windowFrames.generateFlows(dirname, windowSize)