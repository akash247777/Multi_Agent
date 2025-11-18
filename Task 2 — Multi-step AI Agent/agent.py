import os
import requests
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure APIs
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
gemini_model = genai.GenerativeModel('gemini-pro')

SERPAPI_KEY = os.getenv("SERPAPI_KEY")

# --- Step 1: Web Info Gathering ---
def search_web(topic):
    url = "https://serpapi.com/search"
    params = {
        "q": topic,
        "api_key": SERPAPI_KEY,
        "num": 3,
        "engine": "google"
    }
    try:
        response = requests.get(url, params=params, timeout=10)
        results = response.json()
        snippets = [result.get('snippet', '') for result in results.get('organic_results', [])[:3]]
        return " ".join(snippets)
    except Exception as e:
        print(f"[⚠️] Search failed: {e}. Using fallback text.")
        return """
        AI can support teachers by automating grading, personalizing learning, identifying at-risk students, suggesting lesson resources, and analyzing class trends.
        Studies show teachers save 5–10 hours per week on grading with AI tools.
        Intelligent tutoring systems provide 24/7 student support.
        Early warning systems flag students struggling with concepts.
        AI recommends aligned resources based on curriculum and student level.
        Analytics help teachers adjust instruction in real time.
        """

# --- Step 2: Key Point Extraction ---
def extract_key_points(text, topic):
    prompt = f"From the following text, extract exactly 5 key points about {topic}. Each point must be concise (under 15 words), actionable, and evidence-based. Use bullet points. Ignore fluff and opinions.\n\nText: {text}"
    response = gemini_model.generate_content(prompt)
    return response.text.strip()

# --- Step 3: Summary Generation ---
def generate_summary(key_points, topic):
    prompt = f"Write a 150-word professional summary about {topic} using only the following key points: {key_points}. Tone: informative, calm, suitable for educators or school administrators. Do not exceed 150 words."
    response = gemini_model.generate_content(prompt)
    return response.text.strip()

# --- Step 4: Email Formatting ---
def format_email(summary, topic):
    prompt = f"Format the following summary as a professional email draft. Include:\n- To: School Principal\n- Subject: Clear, benefit-driven\n- Body: The summary text, properly formatted with line breaks.\nDo not add signatures or greetings like 'Dear...'. Just output To:, Subject:, Body:.\n\nSummary: {summary}"
    response = gemini_model.generate_content(prompt)
    return response.text.strip()

# --- MAIN AGENT ---
def main(topic):
    print(f"🤖 Running AI Agent for: '{topic}'\n")

    # Step 1: Gather info
    print("🔍 Step 1: Gathering web info...")
    web_text = search_web(topic)

    # Step 2: Extract key points
    print("📌 Step 2: Extracting key points...")
    key_points = extract_key_points(web_text, topic)
    print(key_points + "\n")

    # Step 3: Generate summary
    print("📝 Step 3: Generating 150-word summary...")
    summary = generate_summary(key_points, topic)
    print(summary + "\n")

    # Step 4: Format email
    print("📧 Step 4: Formatting email draft...")
    email = format_email(summary, topic)
    print(email)

if __name__ == "__main__":
    import sys
    topic = sys.argv[1] if len(sys.argv) > 1 else "How AI can support teachers"
    main(topic)