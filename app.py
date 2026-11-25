import streamlit as st
import pandas as pd

from trustcheck.study import (
    CONDITIONS,
    SCENARIOS,
    make_explanation,
    score_response,
    summarise_responses,
    decision_breakdown,
)

st.set_page_config(page_title="TrustCheck", page_icon="🧭", layout="wide")

for key, default in [
    ("responses", []),
    ("scenario_index", 0),
    ("condition", CONDITIONS[2]),
]:
    if key not in st.session_state:
        st.session_state[key] = default

st.title("🧭 TrustCheck")
st.subheader("Can explanations help people recognise unreliable AI recommendations?")
st.write(
    "A small interactive prototype. Recommendations are simulated; "
    "some are intentionally incorrect."
)

with st.sidebar:
    st.header("Study setup")
    st.selectbox(
        "Explanation condition",
        CONDITIONS,
        key="condition",
        disabled=bool(st.session_state.responses),
        help="Choose a condition before starting. It is locked after the first response.",
    )
    if st.session_state.responses:
        st.caption("Condition locked for this run. Reset the session to choose another condition.")
    else:
        st.caption("Choose one condition and keep it selected throughout the five scenarios.")
    st.write(f"Responses recorded: **{len(st.session_state.responses)}**")
    if st.button("Reset session"):
        st.session_state.responses = []
        st.session_state.scenario_index = 0
        st.rerun()

if st.session_state.scenario_index >= len(SCENARIOS):
    st.success("You completed this scenario set.")
    if st.session_state.responses:
        df = pd.DataFrame(st.session_state.responses)
        metrics = summarise_responses(st.session_state.responses)
        breakdown = decision_breakdown(st.session_state.responses)

        st.subheader("Decision breakdown")

        breakdown_df = pd.DataFrame({
            "Outcome": list(breakdown.keys()),
            "Count": list(breakdown.values()),
        })

        st.dataframe(breakdown_df, use_container_width=True, hide_index=True)
        a, b, c = st.columns(3)
        a.metric("Decision accuracy", f"{metrics['decision_accuracy'] * 100:.0f}%")
        b.metric("AI acceptance", f"{metrics['ai_acceptance'] * 100:.0f}%")
        c.metric("Mean confidence", f"{metrics['mean_confidence']:.1f}/5")

        d, e = st.columns(2)
        d.metric(
            "Acceptance of incorrect recommendations",
            f"{metrics['incorrect_recommendation_acceptance'] * 100:.0f}%",
        )
        e.metric(
            "Acceptance of correct recommendations",
            f"{metrics['correct_recommendation_acceptance'] * 100:.0f}%",
        )

        st.caption(
            "Acceptance of incorrect recommendations is a behavioural indicator "
            "of possible overreliance; it is not a complete measure of trust."
        )
        st.dataframe(df, use_container_width=True)
        st.download_button(
            "Download responses (CSV)",
            df.to_csv(index=False).encode("utf-8"),
            "trustcheck_responses.csv",
            "text/csv",
        )
        st.info(
            "These are demonstration results, not validated research findings. "
            "Do not compare conditions using a single run."
        )

    if st.button("Start again"):
        st.session_state.responses = []
        st.session_state.scenario_index = 0
        st.rerun()
    st.stop()

scenario = SCENARIOS[st.session_state.scenario_index]
condition = st.session_state.condition

st.progress((st.session_state.scenario_index + 1) / len(SCENARIOS))
st.caption(
    f"Scenario {st.session_state.scenario_index + 1} of {len(SCENARIOS)}"
    f" · Condition: {condition}"
)

left, right = st.columns([1.2, 1])
with left:
    st.markdown("### Decision task")
    st.write(scenario["context"])
    st.markdown("### AI recommendation")
    st.info(scenario["recommendation"])

    explanation = make_explanation(scenario, condition)
    if explanation:
        st.markdown("### Explanation")
        st.write(explanation)
    else:
        st.caption("No explanation is provided in this condition.")

with right:
    st.markdown("### Your judgement")
    accepted = st.radio(
        "Would you accept the recommendation?",
        ["Accept", "Reject"],
        index=None,
        key=f"accept_{scenario['id']}",
    )
    confidence = st.slider(
        "Confidence in your decision",
        1,
        5,
        3,
        key=f"conf_{scenario['id']}",
    )
    reason = st.text_area(
        "What influenced your decision? (optional)",
        key=f"reason_{scenario['id']}",
    )

    if st.button("Submit decision", type="primary", disabled=accepted is None):
        accept_bool = accepted == "Accept"
        st.session_state.responses.append(
            {
                "scenario_id": scenario["id"],
                "condition": condition,
                "ai_correct": scenario["ai_correct"],
                "accepted_ai": accept_bool,
                "correct_decision": score_response(scenario, accept_bool),
                "confidence": confidence,
                "reason": reason.strip(),
            }
        )
        st.session_state.scenario_index += 1
        st.rerun()

st.divider()
st.caption(
    "All scenarios are scripted. No live AI model, external service, "
    "or personal data is used."
)
