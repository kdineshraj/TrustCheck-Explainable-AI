# TrustCheck: Exploring the Effect of AI Explanations on Trust and Overreliance

**Module:** Intelligent Interactive Systems  
**Status:** Draft to be completed after running and evaluating the prototype.

## 1. Problem, context and scope
AI-assisted systems present recommendations that users may accept without independently checking the evidence. An explanation can make a recommendation easier to understand, but it is not proof that the recommendation is correct. TrustCheck examines whether explanation format changes a user's decision to accept or reject an AI recommendation, especially when it is wrong.

The prototype compares no explanation, full explanation and partial explanation. It presents a mixture of correct and incorrect simulated recommendations. Users accept or reject each recommendation and rate confidence. The system records the response and scores whether the decision was appropriate for the known scenario.

The scope is deliberately limited to a low-risk simulated task. TrustCheck does not make real-world recommendations, connect to external services or claim to measure stable personal trust.

## 2. Design reasoning
The recommendation and explanation are displayed separately so users can distinguish the AI's answer from its supporting information. The three conditions make explanation format the main visible difference. Both correct and incorrect recommendations are necessary: accepting every recommendation may produce high acceptance but poor discrimination, while rejecting every recommendation is also not a good decision strategy.

Accept/reject choice, confidence and accuracy are recorded separately. Confidence is not equivalent to correctness: a user may be highly confident and still make an incorrect decision. An optional comment gives limited qualitative context. Fixed scenario evidence makes scoring transparent and repeatable. The interface labels all recommendations as simulated.

## 3. Relationship to lecture concepts
Week 1's systems perspective motivates treating the project as an interaction among a person, interface, recommendation component and task evidence, rather than as a model-only problem.

Week 3 Lecture 9, *Prompting as Interaction: Specifying and Checking a Model Call*, motivates making task and output conditions explicit. The prototype controls recommendation content and explanation format rather than relying on unconstrained generation.

Week 4 Lecture 10, *Context Engineering and Memory*, explains that context is selected, ordered and budgeted. TrustCheck keeps scenario evidence fixed and visible. Persistent user memory is excluded from scope.

Week 4 Lecture 11, *Retrieval, Grounding and Provenance*, explains that grounding makes claims checkable but does not guarantee truth, freshness or actual use of a passage. TrustCheck therefore treats explanations as information to inspect, not proof.

Week 4 Lecture 12, *Tools, Connectors and the Boundary*, distinguishes a proposed action from application execution and reporting. TrustCheck does not execute external actions; it records a local decision and offers a CSV export.

## 4. Developed interaction
The user selects one explanation condition, reads a scenario and recommendation, inspects any explanation, then accepts or rejects the recommendation and rates confidence. After five scenarios, the app displays decision accuracy, AI acceptance rate, mean confidence, a response table and a CSV export.

**Add genuine screenshots after running:** condition selector, scenario screen, and results screen. Explain what each screenshot demonstrates.

## 5. Architecture and technical reasoning
The interface is implemented in Streamlit. Python scenario and scoring functions are separated into `trustcheck/study.py`; `app.py` manages the interface and session state. pandas creates the results table and CSV export. Scenario records hold context, recommendation, known correctness and full/partial explanation text. The scoring function checks whether the user's accept/reject decision matches known correctness.

A database, accounts, live model API and persistent memory are excluded to reduce complexity and avoid unnecessary personal-data collection. All simulated content is labelled.

## 6. Evaluation and limitations
First perform functional checks: complete all scenarios, verify that the selected explanation condition is displayed, check that responses are recorded once, confirm correct/incorrect scoring, and test CSV export. Run `pytest -q` and report the actual output.

A small usability check could ask volunteers to complete one assigned condition and comment on clarity and usefulness. Follow module ethics and consent guidance before recruiting participants. Report actual participant numbers and procedure. Do not claim statistical significance from a small convenience sample.

The prototype cannot establish that one explanation type causes less overreliance. It uses five scripted scenarios and a narrow task setting. A larger controlled study with more varied tasks and a suitable sample would be needed for stronger conclusions.

## 7. Development evidence and authorship
Complete this section with your own dated development record, genuine Git commits, screenshots, test output and decisions made after inspecting the application. Distinguish implemented features, simulated behaviour and planned improvements. Disclose AI assistance according to University policy.

## References
- University of Birmingham, *Intelligent Interactive Systems*, Week 1 lecture materials: *Ingredients of an Intelligent Interactive System* and *Human-Centred Intelligent Interaction*.
- University of Birmingham, *Intelligent Interactive Systems*, Week 3, Lecture 9: *Prompting as Interaction: Specifying and Checking a Model Call*.
- University of Birmingham, *Intelligent Interactive Systems*, Week 4, Lecture 10: *Context Engineering and Memory*.
- University of Birmingham, *Intelligent Interactive Systems*, Week 4, Lecture 11: *Retrieval, Grounding and Provenance*.
- University of Birmingham, *Intelligent Interactive Systems*, Week 4, Lecture 12: *Tools, Connectors and the Boundary*.


## Updated implementation note (24 November 2026)

The revised interface locks the explanation condition after the first submitted response, preventing a single run from mixing no, full and partial explanation conditions. The results screen now reports acceptance of correct recommendations and acceptance of incorrect recommendations separately, alongside overall decision accuracy, overall AI acceptance and mean confidence. Acceptance of incorrect recommendations is interpreted only as a behavioural indicator of possible overreliance; confidence is confidence in the user's decision, not a direct trust measure.

The automated test suite was expanded to ten tests. In the prepared project environment, `pytest -q` reported 10 passed. The student must repeat this check locally before claiming it as their own verification. The supplied demonstration screenshots still document only one completed Partial explanation run. No completed No explanation or Full explanation run is claimed in this report.
