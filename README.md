# E-Commerce Review Analyzer

A small **Streamlit** app for summarizing **Amazon- or Flipkart-style** product reviews. Paste one or many reviews, click **Analyze**, and get structured output: **positive themes**, **negative themes**, **overall sentiment**, and **key insights**. The app uses **LangChain** with **Groq** (`llama-3.3-70b-versatile`).

## Features

- Paste review text in a large text area  
- **Analyze** runs a single LLM call with a fixed Markdown report format  
- **Clear** resets the text area  
- API key loaded from a local `.env` file (not committed to git)

## Prerequisites

- **Python 3.10+** (recommended)  
- A **Groq API key** from [Groq Console](https://console.groq.com) (free tier subject to Groq’s current limits)

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/YOUR_REPO.git
   cd YOUR_REPO
   ```

2. **Create and activate a virtual environment**

   **Windows (PowerShell)**

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   **macOS / Linux**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**

   In the project root, create a file named `.env`:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Never commit `.env`. It is listed in `.gitignore`.

## Run the app

```bash
streamlit run app.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`), paste reviews, then click **Analyze**.

## Tech stack

| Piece        | Role                                      |
|-------------|--------------------------------------------|
| Streamlit   | Web UI                                     |
| LangChain   | Messages + `invoke` on the chat model      |
| langchain-groq | `ChatGroq` → Groq-hosted Llama          |
| python-dotenv | Load `GROQ_API_KEY` from `.env`        |

## Limitations

- Output is a **summary of the text you pasted**; it does not verify facts or fetch live product data.  
- Very long pastes use more tokens; stay within Groq’s limits for your account.

## License

Specify your license here (for example MIT), or remove this section if the repo is private and you prefer not to state one.
