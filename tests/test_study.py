import pytest

from trustcheck.study import (
    SCENARIOS,
    CONDITIONS,
    make_explanation,
    score_response,
    summarise_responses,
    decision_breakdown,
)


def test_three_conditions_are_available():
    assert CONDITIONS == ["No explanation", "Full explanation", "Partial explanation"]


def test_no_explanation_returns_empty_string():
    assert make_explanation(SCENARIOS[0], "No explanation") == ""


def test_full_and_partial_explanations_are_available_and_distinct():
    scenario = SCENARIOS[0]
    full = make_explanation(scenario, "Full explanation")
    partial = make_explanation(scenario, "Partial explanation")
    assert full
    assert partial
    assert full != partial


def test_unknown_condition_is_rejected():
    with pytest.raises(ValueError):
        make_explanation(SCENARIOS[0], "Unrecognised condition")


def test_accepting_correct_recommendation_is_correct():
    assert score_response(SCENARIOS[1], True)


def test_rejecting_incorrect_recommendation_is_correct():
    assert score_response(SCENARIOS[0], False)


def test_accepting_incorrect_recommendation_is_incorrect():
    assert not score_response(SCENARIOS[0], True)


def test_rejecting_correct_recommendation_is_incorrect():
    assert not score_response(SCENARIOS[1], False)


def test_summary_separates_correct_and_incorrect_recommendation_acceptance():
    responses = [
        {"ai_correct": True, "accepted_ai": True, "correct_decision": True, "confidence": 4},
        {"ai_correct": False, "accepted_ai": True, "correct_decision": False, "confidence": 2},
        {"ai_correct": False, "accepted_ai": False, "correct_decision": True, "confidence": 5},
    ]
    summary = summarise_responses(responses)
    assert summary["decision_accuracy"] == pytest.approx(2 / 3)
    assert summary["ai_acceptance"] == pytest.approx(2 / 3)
    assert summary["mean_confidence"] == pytest.approx(11 / 3)
    assert summary["incorrect_recommendation_acceptance"] == pytest.approx(1 / 2)
    assert summary["correct_recommendation_acceptance"] == pytest.approx(1.0)


def test_empty_summary_is_safe():
    summary = summarise_responses([])
    assert summary["decision_accuracy"] == 0.0
    assert summary["incorrect_recommendation_acceptance"] == 0.0


def test_decision_breakdown_counts_all_four_outcomes():
    responses = [
        {"ai_correct": True, "accepted_ai": True},
        {"ai_correct": True, "accepted_ai": False},
        {"ai_correct": False, "accepted_ai": True},
        {"ai_correct": False, "accepted_ai": False},
    ]

    result = decision_breakdown(responses)

    assert result["Accepted correct recommendations"] == 1
    assert result["Rejected correct recommendations"] == 1
    assert result["Accepted incorrect recommendations"] == 1
    assert result["Rejected incorrect recommendations"] == 1
