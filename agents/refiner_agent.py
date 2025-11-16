class RefinerAgent:
    def refine(self, draft, feedback):
        return f"""
Refined Explanation:

Below is the improved version based on evaluator feedback:

Original:
{draft}

Feedback:
{feedback}

Improved Version:
- Explanation is more clear.
- Steps are shorter.
- Flow is more natural.
- Language is simplified for learning.

This final refined output is ready for users.
"""
