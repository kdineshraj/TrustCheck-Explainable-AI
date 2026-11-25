"""Fixed study materials and scoring helpers for the TrustCheck prototype."""

CONDITIONS = ["No explanation", "Full explanation", "Partial explanation"]

SCENARIOS = [
    {
        "id": "S01",
        "context": "A student checks a coursework deadline. The supplied course record states Friday.",
        "recommendation": "The deadline is Thursday.",
        "ai_correct": False,
        "full": "The system says Thursday, but the supplied record says Friday. The recommendation conflicts with the evidence.",
        "partial": "The source record may not support this date. Check the recorded deadline.",
    },
    {
        "id": "S02",
        "context": "A route comparison shows Route A is 2.1 km and Route B is 3.4 km.",
        "recommendation": "Choose Route A.",
        "ai_correct": True,
        "full": "Route A is 2.1 km, compared with 3.4 km for Route B, so it is shorter by 1.3 km.",
        "partial": "The recommendation is based on the distance comparison. Route A has the lower recorded distance.",
    },
    {
        "id": "S03",
        "context": "The inventory record supplied to the system says zero units are available.",
        "recommendation": "The product is available to order now.",
        "ai_correct": False,
        "full": "The inventory record reports zero available units. The recommendation is unsupported by the supplied record.",
        "partial": "The stock information may not support this recommendation. Check the current inventory value.",
    },
    {
        "id": "S04",
        "context": "The schedule lists two appointments on the same day: 10:30 and 14:00.",
        "recommendation": "The 10:30 appointment is earlier.",
        "ai_correct": True,
        "full": "10:30 occurs before 14:00 on the same day, so it is the earlier appointment.",
        "partial": "Compare the two times on the same day. One is in the morning and one is in the afternoon.",
    },
    {
        "id": "S05",
        "context": "A policy excerpt says extensions must be approved before the deadline.",
        "recommendation": "A late submission is automatically accepted without approval.",
        "ai_correct": False,
        "full": "The policy says an extension must be approved before the deadline. It does not support automatic acceptance.",
        "partial": "The retrieved policy mentions prior approval. The recommendation may not match that requirement.",
    },
]


def make_explanation(scenario, condition):
    """Return the explanation for a scenario under the selected condition."""
    if condition == "No explanation":
        return ""
    if condition == "Full explanation":
        return scenario["full"]
    if condition == "Partial explanation":
        return scenario["partial"]
    raise ValueError(f"Unknown explanation condition: {condition}")


def score_response(scenario, accepted_ai):
    """A decision is correct when it accepts correct advice or rejects incorrect advice."""
    return bool(accepted_ai) == bool(scenario["ai_correct"])


def summarise_responses(responses):
    """Calculate descriptive metrics without treating them as validated research findings."""
    if not responses:
        return {
            "decision_accuracy": 0.0,
            "ai_acceptance": 0.0,
            "mean_confidence": 0.0,
            "incorrect_recommendation_acceptance": 0.0,
            "correct_recommendation_acceptance": 0.0,
        }

    total = len(responses)
    incorrect = [r for r in responses if not r["ai_correct"]]
    correct = [r for r in responses if r["ai_correct"]]
    return {
        "decision_accuracy": sum(bool(r["correct_decision"]) for r in responses) / total,
        "ai_acceptance": sum(bool(r["accepted_ai"]) for r in responses) / total,
        "mean_confidence": sum(float(r["confidence"]) for r in responses) / total,
        "incorrect_recommendation_acceptance": (
            sum(bool(r["accepted_ai"]) for r in incorrect) / len(incorrect) if incorrect else 0.0
        ),
        "correct_recommendation_acceptance": (
            sum(bool(r["accepted_ai"]) for r in correct) / len(correct) if correct else 0.0
        ),
    }

def decision_breakdown(responses):
    breakdown = {
        "Accepted correct recommendations": 0,
        "Rejected correct recommendations": 0,
        "Accepted incorrect recommendations": 0,
        "Rejected incorrect recommendations": 0,
    }

    for response in responses:
        if response["ai_correct"] and response["accepted_ai"]:
            breakdown["Accepted correct recommendations"] += 1
        elif response["ai_correct"] and not response["accepted_ai"]:
            breakdown["Rejected correct recommendations"] += 1
        elif not response["ai_correct"] and response["accepted_ai"]:
            breakdown["Accepted incorrect recommendations"] += 1
        else:
            breakdown["Rejected incorrect recommendations"] += 1

    return breakdown
