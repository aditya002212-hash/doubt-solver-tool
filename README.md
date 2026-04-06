 # Doubt Solver with Memory & Follow-up

An AI-powered personalized doubt solver built in Python that simulates a real study mentor by combining memory, structured responses, and follow-up interaction.


🧠 Overview


This project is designed to go beyond a basic chatbot.


Instead of just answering one question, it:

remembers student profile
stores past doubts
provides structured explanations
supports intelligent follow-ups


The goal was to understand how AI system design + prompt engineering + memory can improve real-world usefulness.


✨ Features

📌 1. Profile Memory
Stores student details (class, target exam, weak subject)
Uses this context to personalize responses

💬 2. Doubt Solving
Structured answers like a Kota mentor
Includes:
key points
step-by-step solution
exam tips
summary
common mistakes

🔁 3. Follow-up System

After solving a doubt, user can:

get another example
convert explanation into Hinglish
generate revision notes
get a practice question
ask custom follow-ups

🗂️ 4. History Tracking
Saves all previous doubts and responses
Enables learning continuity

🏗️ System Design (How it works)
User Input
   ↓
Profile Memory (JSON)
   ↓
Prompt Builder (System Prompt + Context)
   ↓
LLM Response
   ↓
Follow-up Engine
   ↓
History Storage (JSON)

Key Components:
Memory Layer → Profile + History
Prompt Layer → Structured system prompt
Interaction Layer → Follow-up system
Storage Layer → JSON-based persistence

🧪 Tech Stack
Python
JSON (for memory storage)
Generative AI API
CLI-based interface

📚 What I Learned

This project was a major step in understanding real AI product building:

🔹 1. System Design Thinking

How to connect:

memory
prompt logic
user flow
response pipeline
🔹 2. Importance of Memory

Without memory → generic chatbot
With memory → personalized assistant

🔹 3. Follow-up Design

Real value comes from:

Not just answering, but continuing the learning process

🔹 4. Power of System Prompts

A well-designed prompt can:

improve structure
improve clarity
improve teaching quality
improve relevance
🔹 5. Product vs Script

This project made me realize:

AI is not just about API calls — it's about designing the full experience.
