import json
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure Gemini API
API_KEY = os.getenv("GEMINI_API_KEY")
if not API_KEY or API_KEY == "your_gemini_api_key_here":
    print("ERROR: GEMINI_API_KEY not found or not set in .env file.")
    print("Please update the .env file with your actual API key.")
    exit(1)

genai.configure(api_key=API_KEY)

#Mock transcript for demonstration
mock_transcript = """
Interviewer: Please introduce yourself.
Candidate: I'm Alex, a software engineer with 3 years of experience in Web Development. I've worked on high-traffic e-commerce sites using React and Node.js.
Interviewer: (Easy) What is the difference between let and const in JavaScript?
Candidate: 'let' is for variables that can be reassigned, while 'const' is for constants that cannot.
Interviewer: (Medium) How does the virtual DOM work in React?
Candidate: It's a lightweight copy of the real DOM. React updates the virtual DOM first, then compares it with the real DOM to apply only the necessary changes.
Interviewer: (Medium) Can you describe a project where you used these technologies?
Candidate: I built a 'Real-time Analytics Dashboard' that processed live user data and displayed it using D3.js.
Interviewer: (Hard) What are some ways to optimize the performance of a large-scale web application?
Candidate: We can use code splitting, lazy loading, and caching strategies like Service Workers. I also use memoization in React.
"""

def get_system_prompt():
    with open("summary_prompt.txt", "r") as f:
        return f.read()

def generate_summary(transcript):
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    prompt = f"{get_system_prompt()}\n\nTranscript:\n{transcript}"
    
    print("Calling Gemini API...")
    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            response_mime_type="application/json",
        ),
    )
    
    try:
        # The API returns a string that we need to parse as JSON
        summary_json = json.loads(response.text)
        return summary_json
    except json.JSONDecodeError:
        print("Error parsing JSON from Gemini response.")
        return response.text

if __name__ == "__main__":
    print("--- Interview Summary Generator ---")
    
    # Run the generator
    result = generate_summary(mock_transcript)
    
    print("\n--- Generated Summary ---")
    print(json.dumps(result, indent=2))
    
    # Save to a file
    output_file = "interview_summary_result.json"
    with open(output_file, "w") as f:
        json.dump(result, f, indent=2)
    
    print(f"\nSummary successfully saved to '{output_file}'.")
