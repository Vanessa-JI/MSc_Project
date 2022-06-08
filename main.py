import windowFrames

# specify video to create optical flows for 
video = 'Video01'

# dirname for now is the directory of the video e.g. 'Video01', but will change in the future to CaDISv2 and loop through this 
dirname = '/Users/vanessaigodifo/Library/CloudStorage/OneDrive-UniversityCollegeLondon/MSc_Project/Dataset/CaDISv2/' + video 
windowFrames.generateFlows(dirname)