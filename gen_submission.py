"""
Description: Generate a Kaggle submission file from VW predictions
Author: Triskelion <info@mlwave.com>
Kaggle contest description, rules and data: 
http://www.kaggle.com/c/decoding-the-human-brain/
Code description:
http://mlwave.com/predict-visual-stimuli-from-human-brain-activity/
"""

loc_preds = "face.preds.txt"
loc_submission = "kaggle.face.submission.csv"

def generate_submission(loc_preds, loc_submission, header="Id,Prediction", binary=True):
	with open(loc_submission, "wb") as outfile:
		if len(header) > 0:
			outfile.write(header+"\n")
			
		for e, line in enumerate( open(loc_preds) ):
			row = line.strip().split(" ")
			if binary:
				if float(row[0]) == 1:
					pred = "1"
				else:
					pred = "0"
			outfile.write(row[1]+","+pred+"\n")

if __name__ == '__main__':
	generate_submission(loc_preds, loc_submission)