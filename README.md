# E-Commerce Review Analyzer

A small **Streamlit** app for summarizing **Amazon- or Flipkart-style** product reviews. Paste one or many reviews, click **Analyze**, and get structured Markdown: **positive themes**, **negative themes**, **overall sentiment**, and **key insights**. The app uses **LangChain** with **Groq** (`llama-3.3-70b-versatile`).

**Repository:** [github.com/Abhisyanth/Product-analyzer](https://github.com/Abhisyanth/Product-analyzer)

## Features

- Large text area for pasted reviews  
- **Analyze** — single LLM call with a fixed report layout  
- **Clear** — empties the text area and removes the last saved report (uses Streamlit `session_state` + `on_click` so the widget state stays valid)  
- **Download report (.md)** — after a successful analysis, download the last report as `review-analysis.md`  
- **API key** — read from `.env`; value is **trimmed** so accidental spaces/newlines don’t break the key  
- **Errors** — missing key / empty paste / API failures surface in the UI (`st.error` / `st.warning`) instead of crashing the page  

## Prerequisites

- **Python 3.10+** (recommended)  
- A **Groq API key** from [Groq Console](https://console.groq.com) (limits depend on Groq’s current free tier)

## Setup

1. **Clone the repository**

   ```bash
   git clone https://github.com/Abhisyanth/Product-analyzer.git
   cd Product-analyzer
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

   In the project root, create `.env`:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

   Do **not** commit `.env`. It is listed in `.gitignore`.

## Run the app

```bash
python -m streamlit run app.py
```

Open the URL shown in the terminal (usually `http://localhost:8501`), paste reviews, then click **Analyze**. Use **Download report (.md)** to save the latest summary.

## Project layout

| File | Purpose |
|------|--------|
| `app.py` | Streamlit UI + LangChain / Groq call |
| `requirements.txt` | Python dependencies |
| `.env` | Your secret key (local only) |
| `.gitignore` | Keeps `.env`, `.venv`, etc. out of git |

## Tech stack

| Piece | Role |
|--------|------|
| Streamlit | Web UI |
| LangChain | `SystemMessage` / `HumanMessage` + `invoke` |
| langchain-groq | `ChatGroq` → Groq-hosted Llama |
| python-dotenv | Load `GROQ_API_KEY` from `.env` |

## Limitations

- The report is only as good as the **text you paste**; it does not verify facts or fetch live listings.  
- Long inputs use more tokens; stay within your Groq quota.  
- Do not paste passwords, payment data, or other sensitive information.

