class EvaluatorAgent:
    def evaluate(self, draft_answer, query):
        score = 0

        if len(draft_answer) > 50:
            score += 1
        if "step" in draft_answer.lower():
            score += 1
        if query.lower() in draft_answer.lower():
            score += 1

        return {
            "score": score,
            "feedback": f"Evaluation complete. Score: {score}/3"
        }
