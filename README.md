# Multi-Agent Blog Generator with CrewAI

An AI-powered **multi-agent blog generation system** built using **CrewAI, FastAPI, and LLMs**.  
The system uses multiple specialized AI agents that collaborate to research, write, and refine blog content automatically.

Users simply provide a **topic**, and the system generates a **well-structured blog post** through coordinated agent workflows.

---

# Features

- Multi-agent AI system using **CrewAI**
- Automatic **blog generation from a topic**
- Agents collaborate to produce structured content
- **FastAPI backend** for API communication
- **Streaming responses** for real-time blog generation
- Simple **frontend UI** for interaction

---

# How It Works

The system uses multiple AI agents, each responsible for a specific task.

### Agent Workflow

1. **Research Agent**
   - Collects relevant information about the topic.

2. **Writer Agent**
   - Converts research into a structured blog draft.

3. **Editor Agent**
   - Improves readability, clarity, and structure.

4. **Final Output**
   - A complete blog post delivered to the user.

These agents collaborate using **CrewAI's orchestration system**.

---

# Project Architecture

```
User
  |
  v
Frontend UI
  |
  v
FastAPI Backend
  |
  v
CrewAI Agent System
  |        |        |
Research  Writer   Editor
 Agent     Agent     Agent
  |
  v
Generated Blog Output
```

---

# Project Structure

```
Multi-Agent-Blog-Generator-With-CrewAI

backend/
│
├── main.py                # FastAPI application
├── crew.py                # CrewAI agent orchestration
├── agents.py              # Agent definitions
├── tasks.py               # Task definitions
│
frontend/
│
├── index.html             # User interface
├── style.css              # Styling
├── script.js              # API communication
│
requirements.txt           # Python dependencies
README.md
```

---

# Tech Stack

### AI & Agents
- CrewAI
- Large Language Models (LLMs)

### Backend
- FastAPI
- Python

### Frontend
- HTML
- CSS
- JavaScript

### AI Workflow
- Multi-agent collaboration
- Task orchestration

---

# Installation

Clone the repository

```bash
git clone https://github.com/your-username/Multi-Agent-Blog-Generator-With-CrewAI.git
cd Multi-Agent-Blog-Generator-With-CrewAI
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Setup

Create a `.env` file and add your API key.

Example:

```
GROQ_API_KEY=your_api_key_here
```

---

# Run the Backend

Start the FastAPI server.

```bash
uvicorn backend.main:app --reload
```

The backend will run at:

```
http://127.0.0.1:8000
```

---

# Run the Frontend

Open the `index.html` file in your browser or serve it using a local server.

Example using Python:

```bash
python -m http.server
```

---

# Example Usage

1. Enter a **blog topic** in the UI.
2. The request is sent to the **FastAPI backend**.
3. The **CrewAI agent system** generates the blog.
4. The blog content streams back to the frontend.

Example input:

```
Future of Artificial Intelligence
```

Example output:

```
A complete structured blog including:
- Introduction
- Key concepts
- Real-world applications
- Future trends
```

---

# Future Improvements

- Add **SEO optimization agent**
- Add **fact-checking agent**
- Add **image generation for blogs**
- Support **multiple LLM providers**
- Deploy as a **public SaaS tool**

---

# Author

**Ritik Gautam**

GitHub  
https://github.com/HritikGautam

---

# Support

If you like this project, consider giving it a **star on GitHub**.
