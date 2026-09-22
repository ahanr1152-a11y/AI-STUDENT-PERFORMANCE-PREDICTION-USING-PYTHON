# AI-STUDENT-PERFORMANCE-PREDICTION-USING-PYTHON
# 🤖 AI Student Performance Predictor

A beginner-friendly Machine Learning project built with Python and Scikit-learn that predicts whether a student is likely to **Pass** or **Need Improvement** based on basic academic factors.

# 📌 About The Project

The AI Student Performance Predictor is my first Machine Learning project as I begin my journey toward becoming an AI/ML Engineer.

The project uses a **Decision Tree Classifier** to learn patterns from student performance data.

The model considers four features:

- Study hours per day
- Attendance percentage
- Previous exam marks
- Assignments completed

Based on these inputs, the trained model predicts:

- `1` → Pass
- `0` → Need Improvement

# 🎯 Project Objective

The main objective of this project is to understand the fundamentals of supervised Machine Learning by building a simple prediction system from scratch.

Instead of using an AI API, this project uses a Machine Learning algorithm that learns patterns from training examples.

# 🧠 Machine Learning Concept

This project uses **Supervised Learning**.

In supervised learning, we provide the model with:

- Input data
- Correct answers/labels

The model learns the relationship between them and uses that knowledge to make predictions on new data.

# 🌳 Algorithm Used

## Decision Tree Classifier

A Decision Tree makes predictions by creating a sequence of decisions based on the input features.

For example:

```text
                 Attendance >= 75%?
                    /          \
                  NO            YES
                  ↓              ↓
          NEED IMPROVEMENT    Marks >= 50?
                              /         \
                            NO           YES
                            ↓             ↓
                    NEED IMPROVEMENT    PASS
The actual tree is created automatically by the Machine Learning algorithm from the training data.
📊 Features Used
Feature
Description
Study Hours
Number of hours studied per day
Attendance
Student attendance percentage
Previous Marks
Marks obtained in a previous exam
Assignments
Number of completed assignments
🗂️ Project Structure
AI-Student-Performance-Predictor/
│
├── AIStudentPerformance.py
└── README.md
🛠️ Technologies Used
Python
Scikit-learn
Machine Learning
Decision Tree Classification
⚙️ Installation
1. Install Python
Make sure Python is installed on your computer.
You can check it using:
python --version
2. Install Scikit-learn
Open the VS Code terminal and run:
pip install scikit-learn
▶️ How To Run
Open the project folder in VS Code.
Run:
python AIStudentPerformance.py
The program will ask for:
Study hours per day:
Attendance percentage:
Previous exam marks:
Assignments completed:
Enter the required information.
💻 Example
Input:
Study hours per day: 6
Attendance percentage: 90
Previous exam marks: 76
Assignments completed: 8
The model may produce:
==========================================
              RESULT
==========================================

Prediction: PASS ✅
For a student with weaker academic indicators, the result may be:
Prediction: NEED IMPROVEMENT ⚠️
🔍 How The Model Works
The project contains two important types of data.
X - Input Features
X contains the information about students.
Example:
X = [
    [1, 50, 35, 3],
    [2, 60, 40, 4],
    [3, 75, 55, 6],
    [5, 85, 70, 8]
]
Each row represents one student.
The four values represent:
Study Hours
Attendance
Previous Marks
Assignments
y - Target Labels
y contains the correct result for each student.
y = [
    0,
    0,
    1,
    1
]
Where:
0 = Need Improvement
1 = Pass
🧠 Training The Model
The Decision Tree model is created using:
model = DecisionTreeClassifier(random_state=42)
The model is trained using:
model.fit(X, y)
The fit() function allows the Machine Learning algorithm to learn patterns from the training data.
🔮 Making A Prediction
After training, new student information is provided to the model.
Example:
student_data = [
    [6, 90, 76, 8]
]
The model makes a prediction using:
prediction = model.predict(student_data)
The prediction is then displayed to the user.
📚 What I Learned
While building this project, I learned:
Basics of supervised Machine Learning
Features and labels
Training data
Decision Tree Classification
model.fit()
model.predict()
How Machine Learning learns patterns from examples
How to use Scikit-learn with Python
How to debug basic Machine Learning errors
⚠️ Project Limitation
This is a beginner educational project.
The current dataset is small and manually created, so the predictions should not be considered scientifically reliable or suitable for making real academic decisions.
The main purpose of this project is to understand the fundamentals of Machine Learning.
🚀 Future Improvements
I plan to improve this project by adding:
[ ] A larger real-world dataset
[ ] CSV-based data storage
[ ] Pandas for data processing
[ ] Train/test split
[ ] Model accuracy evaluation
[ ] Confusion matrix
[ ] Data visualization
[ ] Multiple ML algorithms
[ ] Tkinter GUI
[ ] Better student performance insights
[ ] Model comparison
🎓 My AI/ML Learning Journey
This project is one of the first steps in my journey toward becoming an AI/ML Engineer.
My planned learning path is:
Python
   ↓
NumPy
   ↓
Pandas
   ↓
Data Visualization
   ↓
Machine Learning
   ↓
Deep Learning
   ↓
NLP
   ↓
Generative AI
   ↓
LLMs
   ↓
AI Engineering
👨‍💻 Author
Ahan Raj
B.Tech CSE (AIML) Student
Currently learning Python, Machine Learning and AI Engineering.
⭐ Acknowledgement
This project was created as a hands-on learning project to understand the fundamentals of Machine Learning and Decision Tree Classification.
If you find this project useful, consider giving the repository a ⭐.