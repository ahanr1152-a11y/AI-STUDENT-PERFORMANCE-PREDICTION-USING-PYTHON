#AI Student Performance Predictor
#Beginner Machine Learning Project
from sklearn.tree import DecisionTreeClassifier
#1.TRAINING DATA
#Each student has:[Study Hours,Attendance %,Previous Marks,Assignments Completed]
X = [
    [1,50,35,3],
    [2,60,40,4],
    [2,65,45,5],
    [3,70,50,6],
    [3,75,55,6],
    [4,78,60,7],
    [4,80,65,7],
    [5,85,70,8],
    [5,88,75,8],
    [6,90,80,9],
    [7,92,85,9],
    [8,95,90,10]
]
#RESULT:
#0 = NEED IMPROVEMENTS
#1 = PASS

y=[
    0,
    0,
    0,
    0,
    1,
    1,
    1,
    1,
    1,
    1,
    1,
    1
]

#CREATING MACHINE LEARNING MODEL
model = DecisionTreeClassifier(random_state=42)

#TRAIN THE MODEL
model.fit(X,y)

#TAKE STUDENT INFORMATION

print("="*50)
print("    AI STUDENT PERFORMANCE PREDICTOR")
print("="*50)
print("\nEnter the students's information:\n")

study_hours=float(input("Study hours per day: "))
attendance=float(input("Attendance percentage: "))
previous_marks=float(input("Previous exam marks: "))
assignments=int(input("Assignments completed: "))

#CREATE INPUT FOR THE MODEL

student_data=[
    [study_hours,attendance,previous_marks,assignments]
]

#MAKE PREDICTIONS

prediction=model.predict(student_data)

#7.DISPLAY RESULT

print("\n"+"="*50)
print("      RESULT")
print("=" * 50)
if prediction[0] == 1:
    print("\nPrediction: PASS")
    print("\nSuggestions:")
    print("- Keep maintaining your attendance.")
    print("- Continue your current study routine.")
    print("- Keep completing assignments on time.")

else:

    print("\nPrediction: NEED IMPROVEMENTS")
    print("\nSuggestions:")
    if study_hours < 3:
        print("- Try to increase your daily study hours.")
    if attendance < 75:
        print("-    Try to improve your attendance.")
    if previous_marks < 50:
        print("- Focus on improving your academic performance.")
    if assignments < 6:
        print("- Try to complete more assignments.")

print("\n"+"="*50)
print("Prediction completed using Machine Learning.")
print("="*50)