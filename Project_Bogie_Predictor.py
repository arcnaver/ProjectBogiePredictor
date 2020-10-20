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



# Prompt the user for model and image selection
def promptUser():
	#prompts
	print("Welcome to Project Bogie.")
	print("The Predictor program will need a model, .h5 or hdf5, and an image, .jpg or .png, to test.")
	print("\n")
	

	modelFound = False

	imageFound = False

	# Valid path and file check 
	while not modelFound:
		modelDir = input("Please insert the filepath of the predictive model: ")
		modelExt = os.path.splitext(modelDir)
		print("Model extension: " + modelExt[0])
		print("Model extension: " + modelExt[1])

		if modelExt[1] == '.h5' or modelExt[1] == '.hdf5':
			print("Yay")
			modelFound = True
		else:
			print("Boo")
		
		#if (not os.path.isfile(modelDir)) or (modelExt[1] != '.hdf5' or modelExt[1] != '.h5'):
		#	print(modelDir, 'Filepath does not point to a compatible model file of extention .h5 or .hdf5')
			
		#else:
		#	print("Thank You")
		#	modelFound = True
		

	

	# make sure the path exists
	#assert os.path.exists(modelDir), "No model found at, " + str(modelDir)


	#image = input("Please insert the directory location of the image file you want to test: ")

	return 0;

promptUser()

