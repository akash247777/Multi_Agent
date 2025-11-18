# AI Content Automation Suite  
**By: Akash S G**

---

## 🔍 Overview

This submission delivers a fully automated, multi-task AI content workflow designed to transform a single topic into professionally formatted, platform-optimized content across blogs, social media, and email outreach — all with minimal human input.

The solution includes three modular, production-ready systems:

1. **Task 1: Mini AI Content Workflow** — Turns a topic into a blog outline, LinkedIn post, 5 social captions, and hashtags.  
2. **Task 2: Multi-step AI Agent** — Gathers real-time web data, extracts insights, writes a 150-word summary, and formats it as a ready-to-send email.  
3. **Task 3: Prompt Engineering Toolkit** — Provides reusable, high-precision templates for rewriting, carousel conversion, and cross-platform repurposing.

All workflows use **Google Gemini API** for generative AI and **SerpAPI** for real-time web search (where needed), ensuring ethical, scalable, and culturally aware outputs — especially optimized for contexts like *Education in India*.

---

## 🛠 Tools & Libraries Used

| Component | Tool/Library |
|---------|--------------|
| AI Generation | Google Gemini Pro (via `google-generativeai`) |
| Web Search | SerpAPI (Google Search Results) |
| Environment Management | `python-dotenv` |
| Scripting | Python 3.10+ |
| Diagramming | draw.io (exported as PNG) |
| Dependencies | `requests`, `dotenv` |

*No OpenAI or proprietary models used — fully Google ecosystem compliant.*

---

## 📁 How to Navigate This Submission

All files are organized under a single root folder:

```
AI_Content_Automation_Suite/
├── Task1_Content_Workflow/ # Blog + Social + Hashtags generator
│ ├── workflow_diagram.png
│ ├── workflow_explanation.txt
│ ├── prompts_used.txt
│ ├── example_output.txt
│ └── code/
│ ├── content_workflow.py
│ ├── requirements.txt
│ └── README.md
│
├── Task2_AI_Agent/ # Web-research → Email draft agent
│ ├── agent_flowchart.png
│ ├── agent_logic.txt
│ ├── prompts_used.txt
│ ├── example_run.txt
│ └── code/
│ ├── agent.py
│ ├── requirements.txt
│ └── README.md
│
├── Task3_Prompt_Engineering/ # Rewriting, carousels, repurposing
│ ├── prompt_templates.txt
│ ├── explanations.txt
│ └── example_outputs.txt
│
└── README.md # ← You're here!
```


> ✅ All `.txt` files are plain text for easy viewing.  
> ✅ All code is executable with minimal setup.

---

## ▶️ Setup Instructions

1. **Clone or download** this entire folder.
2. Install dependencies for each task:

```
bash
# For Task 1
cd Task1_Content_Workflow/code
pip install -r requirements.txt

# For Task 2
cd ../Task2_AI_Agent/code
pip install -r requirements.txt


3. Get API Keys:
 * Google Gemini API Key
 * SerpAPI Key (required only for Task 2)
4. Create .env files in each code/ folder:

```
# In Task1_Content_Workflow/code/.env
GOOGLE_API_KEY=your_gemini_key_here

# In Task2_AI_Agent/code/.env
GOOGLE_API_KEY=your_gemini_key_here
SERPAPI_KEY=your_serpapi_key_here
```

5. Run any workflow:

```
# Task 1
python content_workflow.py "Future of Learning in India"

# Task 2
python agent.py "How AI can support teachers"

# Task 3 — Use prompts directly in any Gemini interface
```

# 💡 Why This Works

This suite doesn’t just generate content — it structures it.
Each workflow is engineered for ** consistency, clarity, and real-world usability ** — whether you’re a teacher drafting an email to a principal, an EdTech marketer creating social posts, or a content team scaling output across platforms.

All outputs are human-readable, platform-optimized, and audit-ready — no fluff, no hallucinations.

Built for impact. Delivered in code.
