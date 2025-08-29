# Operation-Genius-Alert project

“Operation Genius Alert” - AI-powered Student Study Planner 

✅Provide a brief description of the project
Operation Genius Alert is a tool designed to help students generate personalized study plans and capture feedback for continuous improvement. The system stores student prompts, generated study plans, related tags, retrieved documents, and user feedback in a structured format for future analysis.

✅ Features
Generate personalized study plans based on student prompts.
Save feedback for continuous improvement.
Store tags for easy categorization of topics.
Keep a record of retrieved documents for context tracking.
Feedback is stored in a CSV file for simplicity and portability.

✅Dataset
Educational materials from the Data Science course at The Knowledge House (pdf files). 

✅Problem Statement
Students receive grade feedback but often don’t know how to act on it effectively. They struggle to create a structured study plan, prioritize topics, and incorporate spaced review into their daily study routine. Without guidance, students may waste time or fail to address weak areas in their understanding.

✅Why AI is needed:
AI can analyze recent grade feedback and automatically identify weak areas in a student’s understanding.
AI can personalize a 7-day study plan, breaking it into micro-tasks and scheduling spaced reviews.
AI can link tasks directly to relevant course resources (slides, syllabus sections, readings).

✅Installation instructions
# 1. Clone the repo
git clone https://github.com/Dbell14/Operation-Genius-Alert.git

# 2. Launch Python script
Python script python scripts/Operation-Genius-Alert.py

✅Future Work
In the future, we would like to add options like: 
App grading student’s mini assignments and adjusting the program automatically;
App giving a “GENIUS ALERT” notification when student’s results improve;
Implement feedback loop integration to refine the initial prompt and improve the quality of generated 7-day plans;
Enable dynamic tag generation through an automated call to the tagging system;
Perform a search against the vector database using the generated tags to retrieve the most relevant context;
Extract and compile information from the retrieved results to enhance the final response provided to the user.

✅Acknowledgements / References 
We express gratitude to our TKH instructors Anil Seoparson and Maurice Colon for assisting us with this project. Other resources used: 
Evidence of the Spacing Effect and Influences on Learning – A neuroscience-based study showing how spaced learning significantly strengthens memory compared to cramming. PMC
How Spaced Repetition, Review, and Microlearning Boost Knowledge Retention – Explains how combining spaced repetition with microlearning enhances memory and learner success. LearnDash
PlanGlow: Personalized Study Planning with an Explainable and Controllable LLM-Driven System – Describes an AI-based system that generates personalized study plans with transparency and user control. arXiv 
Recent report on Generative AI in ITS (2024) – discusses LLM integration, adaptive pathways, and ethical considerations. https://arxiv.org/pdf/2410.10650  
CTAT+TutorShop (2025 paper) – research platform supporting ITS experimentation and rapid prototyping. https://arxiv.org/pdf/2502.10395 