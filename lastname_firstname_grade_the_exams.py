import pandas as pd 
import numpy as np


######## INITIAL ################
filename = input("enter a filename: ")
# filename = 'class1'
answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
answer_key = answer_key.split(',')


############## CREATE FUNCTIONS ####################
def check_name(name): #Check ID of student, It must include 9 characters, fisrt one is N and the rest are integers.
	flag = 0
	try:
		for i in range(1, len(name)):
			int(name[i])
		flag = 1 
	except:
		flag= 0

	if len(name) != 9:
		return False
	elif name[0] != 'N':
		return False
	elif flag == 0:
		return False
	else:
		return True

def compute_score(x):  # compute student's score by correct answers, incorect answers and even skip answers
	score = 0
	right = 0
	none = 0
	wrong = 0
	for i in range(1,len(x)):
		if answer_key[i-1] in x[i]:
			right +=1
		elif x[i] in ' \n':
			none += 1
		elif answer_key[i-1] not in x[i]:
			wrong +=1
	score = right*4 + wrong* -1 
	# print('wrong:' ,wrong)
	# print('none', none)
	# print('right', right)
	# print("total:", right+none+wrong)
	return score

#### GET INTO THE CODE #########
try:
	score_line = []
	store =[]

	with open(f"{filename}.txt","r") as f:     #read file 
		print(f"Successfully opened {filename}.txt")
		print("*** ANALYZING ***")


		lines= f.readlines()
		invalid = 0

		for line in lines:
			x = line.split(',')
			name = x[0]

			########### DETECT INVALUE ID  ##################
			if len(x) != 26 or check_name(name) == False :
				print("Invalid line of data: does not contain exactly 26 values:")
				print(x)
				invalid +=1
			else:
				############ CREATE A LIST OF SCORE IN A CLASS AND ITEM OF CLASS_GRADES FILES ##################
				score = compute_score(x)
				score_line.append(score)  #list of score
				item = f'{name},{score}\n'
				store.append(item)
		#CREATE CLASS_GRADE FILES
		with open(f'Grades/{filename}_grades.txt','w') as file1:
			for line in store:
				file1.write(line)
		########## REPORT THE RESULT BASE ON SCORE_LINE ARRAY
		if invalid == 0 :
			print("No errors found!")
		print("**** REPORT ****")
		print("Total valid lines of data:", len(lines) - invalid)
		print("Total invalid lines of data:", invalid)
		mean_v = np.mean(score_line)
		max_v = np.max(score_line)
		min_v = np.min(score_line)
		range_v = max_v - min_v
		median_v = np.median(score_line)

		print('Mean score:', mean_v)
		print('Highest score:', max_v)
		print('Lowest score:', min_v)
		print('Range of score:', range_v )
		print('Median score:', median_v)
except:
	print("Sorry, I can't find this filename")
