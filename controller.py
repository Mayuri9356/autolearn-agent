from agents.teacher_agent import TeacherAgent
from agents.evaluator_agent import EvaluatorAgent
from agents.refiner_agent import RefinerAgent

class AutoLearnSystem:
    def __init__(self):
        self.teacher = TeacherAgent()
        self.evaluator = EvaluatorAgent()
        self.refiner = RefinerAgent()

    def ask(self, query):
        draft = self.teacher.explain(query)
        score, feedback = self.evaluator.evaluate(draft)

        if score < 8:
            refined = self.refiner.refine(draft, feedback)
            return refined
        
        return draft
