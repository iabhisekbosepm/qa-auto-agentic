# QA-Auto: Automated QA Agent Framework

## Overview
QA-Auto is an automated QA testing framework powered by LLMs and browser automation. It reads BDD-style feature files, executes all scenarios, and generates Cucumber-style HTML reports.

---

## 1. Python Environment Setup

### Create a Virtual Environment
```bash
python3 -m venv venv
```

### Activate the Virtual Environment
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
- On Windows:
  ```bash
  .\venv\Scripts\activate
  ```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 2. Project Structure
- `test.py` — Main entry point to run the agent and execute all BDD scenarios.
- `to-do.md` — Your BDD (Gherkin) feature file with all test scenarios.
- `Result/` — Stores conversation logs, generated BDD feature files, and HTML reports.
- `features/` — Used by Behave for HTML report generation.
- `run_full_test.sh` — Script to run the full workflow (agent, BDD formatter, HTML report).

---

## 3. How to Run the Project

### (A) Run the Full Automated Workflow
This will:
- Run the agent on all scenarios in `to-do.md`
- Format results as a BDD `.feature` file
- Generate a Cucumber-style HTML report

```bash
./run_full_test.sh
```
- The final report will be at `Result/report.html` (open in your browser)

### (B) Manual Steps (if needed)
1. Run the agent:
   ```bash
   python test.py
   ```
2. Format the conversation log to BDD:
   ```bash
   python Result/bdd_formatter.py
   ```
3. Copy the generated `.feature` file to `features/`:
   ```bash
   cp Result/bdd_result_*.feature features/
   ```
4. Generate the HTML report:
   ```bash
   behave -f behave_html_formatter:HTMLFormatter -o Result/report.html
   ```

---

## 4. Customizing Your Tests
- Edit `to-do.md` to add or modify BDD scenarios.
- Sensitive data (like credentials) is managed via placeholders in `test.py`.
- The agent will attempt all scenarios and report pass/fail for each.

---

## 5. Troubleshooting
- **Behave not found?** Make sure your virtual environment is activated and run `pip install behave behave-html-formatter`.
- **Chromium/browser not closing?** Use `pkill -f chromium` or update the agent to close the browser after each scenario.
- **Agent not running all scenarios?** Ensure your `to-do.md` is in valid Gherkin format and the meta-instruction in `test.py` is present.

---

## 6. Contributing
- Fork the repo, create a branch, and submit a PR.
- Please keep code and documentation clear and maintainable.

---

## 7. License
MIT 