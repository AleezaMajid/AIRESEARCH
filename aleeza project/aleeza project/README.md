# Domain-Based Intelligent Voice AI Interviewer

🎤 AI Interview Summary Generator (Gemini API)

A Python-based AI tool that analyzes a technical interview transcript and generates a structured interview summary using the Google Gemini API.

This project demonstrates how Large Language Models (LLMs) can automatically evaluate interview responses and produce structured insights such as:

Candidate domain

Projects mentioned

Strengths

Weaknesses

Final performance score

Overall summary

The system uses prompt engineering + JSON schema validation to ensure consistent and machine-readable results.

---

📂 Project Structure
interview-summary-generator/
│
├── generate_summary.py              # Main Python script to generate the summary
├── summary_prompt.txt               # System prompt used by the AI model
├── summary_schema.json              # JSON schema defining the output format
├── interview_summary_result.json    # Example generated output
├── requirements.txt                 # Project dependencies
├── .env                             # Stores Gemini API key (not pushed to GitHub)
├── .gitignore                       # Prevents sensitive files from being committed
└── README.md                        # Project documentation

---

⚙️ Technologies Used

Python

Google Gemini API

Prompt Engineering

JSON Structured Output

Environment Variables (.env)

Python Libraries:

google-generativeai
python-dotenv

---

🚀 How the System Works

A technical interview transcript is provided as input.

A system prompt (summary_prompt.txt) instructs the AI how to analyze the transcript.

A JSON schema (summary_schema.json) defines the required structure of the output.

The prompt and transcript are sent to the Gemini model.

The model generates a structured JSON response.

The result is saved as interview_summary_result.json.

This approach ensures the output is structured, consistent, and easy to parse programmatically.

---

🧠 Prompt Engineering

The AI behavior is defined in:

summary_prompt.txt

This file instructs the AI to:

Identify the candidate's technical domain

Extract projects mentioned

Analyze strengths and weaknesses

Assign a performance score (1–10)

Generate a short professional summary

Keeping the prompt separate from the code allows the AI logic to be updated without modifying the Python script.

---

📑 Output Schema

The expected output format is defined in:

summary_schema.json
{
  "domain": "string",
  "projects_mentioned": ["string"],
  "strengths": ["string"],
  "weaknesses": ["string"],
  "final_score": "number (1-10)",
  "summary_text": "string"
}

This schema ensures that the AI response is consistent and structured so it can be easily used in applications such as dashboards, hiring systems, or analytics pipelines.

---

📦 Installation

Clone the repository:

git clone https://github.com/AleezaMajid/AIRESEARCH.git
cd interview-summary-generator

Create a virtual environment:

python -m venv venv

Activate the environment:

Windows
venv\Scripts\activate
Mac/Linux
source venv/bin/activate

Install dependencies:

pip install -r requirements.txt

---

🔑 Environment Variables

Create a .env file in the root directory:

GEMINI_API_KEY=your_gemini_api_key_here

You can get your API key from:

https://ai.google.dev/

The project securely loads the API key using python-dotenv.

---

▶️ Running the Project

Run the script:

python generate_summary.py

Console output will look like this:

--- Interview Summary Generator ---
Calling Gemini API...

--- Generated Summary ---
{
  "domain": "Web Development",
  "projects_mentioned": [
    "high-traffic e-commerce sites",
    "Real-time Analytics Dashboard"
  ],
  "strengths": [
    "Strong understanding of JavaScript fundamentals",
    "Clear explanation of React Virtual DOM"
  ],
  "weaknesses": [],
  "final_score": 9.0,
  "summary_text": "The candidate demonstrated strong web development knowledge and clearly explained advanced concepts."
}

The result is also saved in:

interview_summary_result.json

---

📊 Example Output
{
  "domain": "Web Development",
  "projects_mentioned": [
    "high-traffic e-commerce sites",
    "Real-time Analytics Dashboard"
  ],
  "strengths": [
    "Strong understanding of JavaScript fundamentals",
    "Clear explanation of React Virtual DOM",
    "Knowledge of performance optimization techniques"
  ],
  "weaknesses": [],
  "final_score": 9.0,
  "summary_text": "The candidate demonstrated a strong grasp of both core and advanced web development concepts."
}

--- 

🔒 Security Best Practices

Sensitive files are excluded from Git using .gitignore.

Ignored files include:

.env
venv/
__pycache__/

This prevents API keys and local environments from being uploaded to GitHub.

---

🎯 Use Cases

AI-powered technical interview analysis

Automated candidate evaluation

HR screening automation

AI interview assistants

LLM prompt engineering demos

---

🚀 Possible Future Improvements

Support real interview audio → speech-to-text transcripts

Build a web dashboard for HR teams

Add multiple interview domains (AI, Data Science, Backend, etc.)

Integrate with ATS or recruitment platforms

---

👨‍💻 Author

Developed as part of an AI research project exploring LLM-powered interview systems using Gemini API.
