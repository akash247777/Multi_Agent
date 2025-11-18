import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

def generate_content(prompt):
    """Generic function to generate content using Gemini"""
    response = model.generate_content(prompt)
    return response.text.strip()

def generate_blog_outline(topic):
    prompt = f"Create a blog outline about {topic} with 5-7 bullet points covering main sections. Each bullet should represent a key section of the blog post. Focus on structure and logical flow."
    return generate_content(prompt)

def generate_linkedin_post(topic):
    prompt = f"Write a professional LinkedIn post about {topic}. Keep it engaging and informative, suitable for professionals. Include a compelling opening, 2-3 key insights, and a thought-provoking closing question. Limit to 2500 characters."
    return generate_content(prompt)

def generate_social_captions(topic):
    prompt = f"Generate 5 short social media captions about {topic}. Each caption should be under 280 characters, engaging, and suitable for different platforms (Instagram, Twitter, Facebook). Include varied styles: question, statement, quote-style, statistic, and call-to-action."
    return generate_content(prompt)

def generate_hashtags(topic):
    prompt = f"Provide 15-20 relevant hashtags for content about {topic}. Include a mix of popular, niche, and branded hashtags. Format as a comma-separated list."
    return generate_content(prompt)

def main(topic):
    print(f"Generating content for: {topic}\n")
    
    outline = generate_blog_outline(topic)
    print("Blog Outline:")
    print(outline)
    print("\n" + "="*50 + "\n")
    
    linkedin = generate_linkedin_post(topic)
    print("LinkedIn Post:")
    print(linkedin)
    print("\n" + "="*50 + "\n")
    
    captions = generate_social_captions(topic)
    print("Social Media Captions:")
    print(captions)
    print("\n" + "="*50 + "\n")
    
    hashtags = generate_hashtags(topic)
    print("Hashtags:")
    print(hashtags)

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        topic = " ".join(sys.argv[1:])
        main(topic)
    else:
        print("Usage: python content_workflow.py 'Your Topic Here'")