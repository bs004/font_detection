1. How to run code?

sudo docker-compose up
Post request at Postman :
{“url”: image url} at port 5000

2. Data creation script had been included in 2 files Data_prepration and data_utils, 
   contains data for Hello world detection using yolo with image files for training a image classsifier.

3. Data used for training has been included in font_data

4. Training script has been included in 2 files train and train_utils, 
   I've used a pretrained EfficientNetB0 to classsify detected Hello World.

5. Model Architecture can be seen in train_utils and corresponding model file is label_classifier.hdf5 .

6. Summary of Findings:
	Using Yolo to directly identify texts is not fruitful as Anchors play an important role in identifying the font.
	So I've used pytesseract to identify a group of 2 tokens and classify them, 
	which is working well but certrainly better results can be achieved with experimental design.
	I've added sample outputs from my models in image and json format both.

7. We can add more classes easily by adding more labels in Font dictionary and
   increasing the nodes of last layer of our model. 
