# Development record

This record separates work observed in the student's walkthrough from changes prepared with AI assistance. Keep it accurate and add further entries only after completing the actions yourself.

| Date | Change or decision | Why it was made | How it was checked |
|---|---|---|---|
| 24 Nov 2026 | Student installed the project dependencies in a local Python virtual environment and launched the Streamlit application. | To verify that the supplied project can run locally. | The terminal screenshot shows dependency installation and the Streamlit local URL. |
| 24 Nov 2026 | Student completed the five-scenario demonstration using the Partial explanation condition. | To inspect the end-to-end interaction and results screen. | Screenshots show the five-scenario run and the results dashboard. The dashboard recorded 5 responses, 100% decision accuracy, 40% AI acceptance and mean confidence 4.0/5 for that demonstration only. |
| 24 Nov 2026 | Student ran the original automated test suite. | To check core explanation and scoring functions. | The terminal screenshot showed 5 tests passed. |
| 24 Nov 2026 | AI-assisted revision prepared: explanation condition is locked after the first response, and the interface displays the selected condition. | To prevent responses from different conditions being mixed in one session, improving consistency of the demonstration. | Revised code includes the disabled selector after the first response. Student must run the revised app and verify this behaviour locally. |
| 24 Nov 2026 | AI-assisted revision prepared: added separate acceptance metrics for correct and incorrect recommendations and descriptive summary helper. | Overall acceptance alone cannot show whether a user is accepting incorrect advice. | Added automated tests for the summary calculations. Student must inspect the metric definitions and run the tests locally. |
| 24 Nov 2026 | AI-assisted revision prepared: expanded automated tests from 5 to 10. | To cover all three explanation outputs, invalid condition handling, both correct and incorrect decisions, and summary calculations. | In the prepared project environment, `pytest -q` reported 10 passed. Student must repeat this check in their own environment. |

## Design decisions and reflection prompts

- **Why compare no, full and partial explanations?** They operationalise three levels of explanatory information for the research question. They do not imply that one condition is automatically superior.
- **Why record acceptance separately from confidence?** Acceptance is a behavioural response. Confidence is the user's self-reported certainty about their own decision. Neither is a complete direct measure of trust.
- **Why include correct and incorrect recommendations?** This allows the prototype to distinguish acceptance of correct advice from acceptance of incorrect advice. The latter is a behavioural indicator of possible overreliance.
- **Why keep the condition constant within a run?** Mixing conditions in one five-scenario session would make the summary difficult to interpret. The revised interface locks the condition after the first submitted response.
- **Why reveal correctness only through the scoring/results data?** The user should make a judgement before seeing the correctness label, otherwise the task would disclose the answer.
- **What are the limitations of fixed, simulated scenarios?** They are predictable and repeatable, but do not represent live model behaviour, a validated task set or a real participant study.

## Student completion required

Before submission, the student should:
1. Review the revised source code and be able to explain the state flow, condition lock, scoring and summary metrics.
2. Run `pytest -q` locally and retain the actual output.
3. Launch the app and verify that the condition selector becomes locked after the first response.
4. Complete one run for each of the three conditions if time permits, saving genuine screenshots for each results screen.
5. Add a short personal reflection describing any issue encountered and how it was resolved.
6. Ensure the AI-use declaration matches the actual assistance received and the University's requirements.
