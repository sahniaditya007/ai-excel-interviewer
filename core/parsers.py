from langchain_core.pydantic_v1 import BaseModel, Field
from typing import Literal

class InterviewEval(BaseModel):
    score_correctness: int = Field(
        description="The score from 1 to 5 for the technical correctness of the answer.",
        ge=1,
        le=5
    )
    score_efficiency: int = Field(
    description="The score from 1 to 5 for the efficiency of the proposed solution. E.g., using INDEX/MATCH over VLOOKUP where appropriate.",
    ge=1,
    le=5
    )
    score_clarity: int = Field(
    description="The score from 1 to 5 for the clarity of the candidate's explanation.",
    ge=1,
    le=5
    )
    feedback: str = Field(
    description="Detailed, constructive feedback for the candidate. Explain why the scores were given. If the answer was incorrect, provide the correct answer or a better approach. This should be a mini-lesson."
    )
    overall_assessment: Literal["Excellent", "Good", "Average", "Needs Improvement"] = Field(
    description="A single, overall assessment of the candidate's answer."
    )
    