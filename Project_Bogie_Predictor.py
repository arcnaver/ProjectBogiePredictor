##################################################################################
# Author:   Adam Tipton
# Title:    Project Bogie Predictor
# Version:  1
#
# Company:  Brigham Young University - Idaho
# Course:   CSE 499 Senior Project
# Semester: Fall 2020
# 
# Description:
#   Project Bogie is a Convolutional Neural Network written in the Python language. 
#   This CNN will train a model from a dataset the ability to identify military 
#   aircraft/jets. 
#   
#   Once trained, the program will create save the model for use in an application
#   that allows a user to input an image to test if it contains a military aircraft.
#   
#   Project Bogie uses TensorFlow as a backend and Keras as a driving force for training
#   and predicting.
#
#   The Predictor program will take the model created by the Project Bogie Trainer.
#   The model will then be loaded into the predictor program. The user well then point
#   to an image, or set of images, for the model to predict an outcome. Possible outcomes
#   will be does the image contain a modern military aircraft or something else. 
#
# Sources:
#   Much inspiration and reusable code base is taken from the following tutorial -
#   URL: https://machinelearningmastery.com/how-to-develop-a-convolutional-neural-network-to-classify-photos-of-dogs-and-cats/
###################################################################################   
###################################################################################

# These imports are import for image loading and processing
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.models import load_model

# These imports are important for file handling
import os
from os import listdir


# Welcome the user
def welcome():
	#prompts
	print("Welcome to Project Bogie.")
	print("The Predictor program will need a model, .h5 or hdf5, and an image, .jpg or .png, to test.")
	print("\n")

# Prompt the user for model
def promptUserModel():
	
	
	#model
	modelFound = False
	modelDir = ''
	
	# Valid model path and file check 
	while not modelFound:
		modelDir = input("Please insert the filepath of the predictive model: ")
		modelExt = os.path.splitext(modelDir)
		
		# check if model[0] is valid dir
		if not os.path.exists(modelDir):
			print("\nFilepath error: " + modelDir + " not found.\n")
		# check if model[1] is a valid extension
		elif (modelExt[1] == '.h5') or (modelExt[1] == '.hdf5'):
			modelFound = True
			print("Model found.\n")
		else:			
			print("\nError: .h5 or .hdf5 model not found.")
			print("Please select a compatible model (<model name>.h5, <model name>.hdf5) \n")
	
			

	return modelDir;

# Prompt the user for an image 
def promptUserImage():
		
	#image
	imageFound = False
	imageDir = ''
	
				
	# Valid image path and file check	
	while not imageFound:
		imageDir = input("Please insert the directory location of the image file you want to test: ")
		imageExt = os.path.splitext(imageDir)
		
		# check if model[0] is valid dir
		if not os.path.exists(imageDir):
			print("\nFilepath error: " + imageDir + " not found.\n")
		# check if model[1] is a valid extension
		elif (imageExt[1] == '.jpg') or (imageExt[1] == '.jpeg') or (imageExt[1] == '.png'):
			imageFound = True
			print("Image found.\n")
		else:			
			print("\nError: .jpg/.jpeg or .png image not found.")
			print("Please select a compatible image type (<image name>.jpg/.jpeg, <image name>.png) \n")
		

	return imageDir;

# Get things rolling
welcome()
model = promptUserModel()
image = promptUserImage()

print(model)
print(image)