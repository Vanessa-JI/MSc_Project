# MSc_Project


Link to Google Drive with code, training, and test data: https://drive.google.com/drive/folders/1lz57aAy-NrJ1o2gCgjKTFMWwha4vudfM?usp=sharing

Link to Colab Notebook: https://colab.research.google.com/drive/1T6F1oniBV9wLTyMftNzaKHhfIgwp4hP4?usp=sharing

- To change from Farneback to FlowNet optical flow data, change *other_inputs_paths* variable in train.py (MSc_Project/image-segmentation-keras/keras_segmentation/train.py) to FB_Flows or FN_Flows on lines 227 and 236. Do the same for *corr_flo* variable on line 145 in predict.py (MSc_Project/image-segmentation-keras/keras_segmentation/predict.py). 
- If weighted loss function is not to be used, change *weighted* variable in train.py to False (line 112).
- Specify the type of augmentation to be applied in data_loader.py (MSc_Project/image-segmentation-keras/keras_segmentation/data_utils/data_loader.py) on line 
