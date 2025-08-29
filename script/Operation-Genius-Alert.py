import subprocess
import sys

# list of required packages
packages = [
    "python-dotenv",          
    "tf-keras",              
    "faiss-cpu",
    "sentence-transformers",
    "transformers",
    "tensorflow",
    "pymupdf4llm",
    "openai",
    "langchain-community",
    "pypdf",
    "langchain-huggingface"
]

# install each one if missing
for pkg in packages:
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", pkg])
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {pkg}: {e}")

from openai import OpenAI
from dotenv import load_dotenv
import pymupdf4llm
import faiss
from sentence_transformers import SentenceTransformer
import os

# Load environment variables

load_dotenv(override=True)
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

# Return tasks based on student feedback
def get_tasks(text: str) -> str:
    """
    Finds a task for a student based on student's feedback on the help they need for specific topics
    """


    system_prompt = """
    You are a Data Science tutor with a Doctorate in Data Science. You analyze students' grades, students feedback, and find short tasks to improve their learning. 
    Your job is to create clear, actionable 7-day study plans for students who are struggling in a subject. 
    Each plan should include:
    - Daily micro-tasks (small, manageable steps)
    - Spaced review of previously covered material
    - Clear instructions for practice problems or study activities
    - Motivational and encouraging language to help the student stay engaged
    Keep the plan practical, concise, and easy for a student to follow. 
    """
    prompt = f"""student's prompt is {text}    
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
]
    )

    output = completion.choices[0].message.content.strip()
    print(output)
    return output

# Example Usage
response = get_tasks('I need help with Bayes Theorem')
print(response)


data = "."

# Generate tags for data
def get_tags(text: str) -> str:
    """
    Finds tags for the requested topic in data science
    """


    system_prompt = f"""
    Can you come up with a list of tags to quickly search material for the 7 day study plan for software engineers. 
    These are the topics covered in the Data Science course:{data}
    Don't use hashtag in the beginning of the words. Don't use hashtags from social media.
    """
    prompt = f"""student's prompt is {text}    
    """

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt}
]
    )

    output = completion.choices[0].message.content.strip()
    
    #print (output)
    return output

get_tags("AB Testing")
updated_tags = get_tags('AB Testing')
print(updated_tags)


updated_tags = updated_tags.replace("\n","")

# Load PDFs
from pathlib import Path

ROOT = Path().resolve().parent
slides = ROOT / "data"

# Embeddings + Vectorstore
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

documents = []

for pdf in slides.glob("*.pdf"):
    pdf_pages = PyPDFLoader(pdf).load_and_split()
    documents.extend(pdf_pages)


documents



embedder = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
db = FAISS.from_documents(documents, embedder)


retriever = db.as_retriever(search_kw={"k":5})


results = retriever.invoke("Bayes Theorem")


first_result = results[0]

first_result.model_dump()

# Generate student study feedback from instructors

import csv
import random

# Topics to base feedback on
topics = [
    "Python Basics", "NumPy", "Pandas", "Data Visualization",
    "Statistics", "Machine Learning", "SQL", "AB Testing",
    "Data Cleaning", "Regression Analysis"
]
# Sample feedback messages (adjusted to include topics dynamically)
positive_feedback = [
    "Great job on your assignments! You’ve shown strong progress in understanding {}.",
    "Excellent effort in applying {} concepts to real problems!",
    "Your coding practices in {} are clean and efficient. Keep up the great work!",
    "You’ve demonstrated strong analytical thinking when working with {} datasets.",
    "Fantastic progress in {}. You’re ready to tackle more advanced challenges!"
]
negative_feedback = [
    "Your submissions on {} are missing key sections, and you need to review the basics.",
    "You struggled with {} exercises. Try to work on time management and practice more.",
    "Your understanding of {} concepts is weak. Please revisit the lecture notes.",
    "The quality of your code in {} lacks proper structure and documentation.",
    "You need to participate more actively in {} activities to strengthen your understanding."
]
neutral_feedback = [
    "You are doing fine in {}, but try focusing more on practicing exercises.",
    "Your {} concepts are clear, but revising them regularly will help retain the knowledge.",
    "You’re making steady progress in {}, but solving more real-world case studies will help.",
    "Consider setting aside 30 minutes daily to review {} alongside new topics.",
    "Good work so far in {}, but consistency in practicing challenges is key."
]
# Feedback types
feedback_types = ["Positive", "Negative", "Neutral"]
# Generate feedback for 15 students
students = [f"Student_{i}" for i in range(1, 16)]
feedback_data = []
for student in students:
    topic = random.choice(topics)
    feedback_type = random.choice(feedback_types)
    if feedback_type == "Positive":
        feedback = random.choice(positive_feedback).format(topic)
    elif feedback_type == "Negative":
        feedback = random.choice(negative_feedback).format(topic)
    else:
        feedback = random.choice(neutral_feedback).format(topic)
    feedback_data.append({
        "Student": student,
        "Feedback_Type": feedback_type,
        "Topic": topic,
        "Feedback": feedback
    })
# Save to CSV
filename = "student_feedback.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["Student", "Feedback_Type", "Topic", "Feedback"])
    writer.writeheader()
    writer.writerows(feedback_data)
print(f"CSV file '{filename}' has been created successfully!")

