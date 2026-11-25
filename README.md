# TrustCheck

TrustCheck is an interactive Streamlit prototype exploring whether explanation format can help people distinguish correct from incorrect simulated AI recommendations.

## Run locally
1. Use Python 3.10 or later.
2. Create a virtual environment: `python -m venv .venv`
3. Activate it (macOS/Linux): `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Launch: `streamlit run app.py`
6. Open the local URL printed in the terminal (usually `http://localhost:8501`).

## Interaction
- Select one explanation condition before the first response.
- The condition is locked after the first response to prevent mixing conditions in a single run.
- Complete the five fixed scenarios.
- For each scenario, accept or reject the recommendation, rate confidence from 1–5, and optionally enter a reason.
- At the end, inspect the descriptive metrics and optionally download the session CSV.
- Reset the session to run another condition.

## Measures and interpretation
The prototype reports decision accuracy, overall AI acceptance, mean confidence, acceptance of incorrect recommendations and acceptance of correct recommendations. Acceptance of incorrect recommendations is a behavioural indicator of possible overreliance, not a complete measure of trust. Confidence is self-reported confidence in the user's decision, not a direct trust scale.

## Scope and limitations
All recommendations and explanations are scripted. There is no live model, retrieval, external API, database, account, persistent memory or external action. The five scenarios are illustrative and are not a validated research instrument. A single demonstration run cannot establish comparative effects or causal claims. A controlled, appropriately approved participant study would be needed for that.

## Tests
Run `pytest -q`. Record the actual output from your own environment. The tests cover condition handling, explanation variants, scoring cases and descriptive summary calculations.

## Development and AI assistance
Review the code and maintain `DEVELOPMENT_RECORD.md` with your actual changes and checks. Disclose AI assistance accurately in line with University requirements. Do not claim work or testing you did not perform.
