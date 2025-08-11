# Our rubric in a response model
from pydantic import BaseModel, Field
from typing import Literal
from mixin import PartnershipEvaluationMixin


class PartnershipEvaluation(BaseModel, PartnershipEvaluationMixin):
    """
    Comprehensive evaluation of a LinkedIn Learning partnership opportunity
    based on partner quality and skill market dynamics.
    """

    # Basic Information
    partner_name: str = Field(
        description="The name of the partner organization (e.g., 'Microsoft', 'Adobe', 'RSA Security')"
    )

    certificate_topic: str = Field(
        description="The specific skill or topic area for the proposed certificate (e.g., 'Azure AI Fundamentals', 'Photoshop for Beginners')"
    )

    # Scoring Dimensions
    general_recognition_score: Literal[1, 2, 3, 4, 5] = Field(
        description="""
        How well-known is this brand to the general professional audience? Score 1-5:
        1 = Unknown outside their specific niche
        2 = Limited recognition, mainly in tech circles  
        3 = Moderately recognized in professional contexts
        4 = Well-known brand across multiple industries
        5 = Household name, universally recognized (Microsoft, Google, Adobe, Amazon, Apple)
        """
    )

    general_recognition_reasoning: str = Field(
        description="2-3 sentence explanation for the general recognition score, including specific evidence of brand awareness"
    )

    domain_authority_score: Literal[1, 2, 3, 4, 5] = Field(
        description="""
        How respected is this partner specifically in this skill area? Score 1-5:
        1 = Not known for this particular skill area
        2 = Some presence but not a leader in this domain
        3 = Solid reputation in this specific area
        4 = Strong authority, frequently referenced in this domain
        5 = THE recognized expert/leader in this skill (RSA for security, Salesforce for CRM, Docker for containers)
        """
    )

    domain_authority_reasoning: str = Field(
        description="2-3 sentence explanation for the domain authority score, focusing on the partner's specific expertise in this skill area"
    )

    career_impact_score: Literal[1, 2, 3, 4, 5] = Field(
        description="""
        How much does this skill boost someone's career prospects in North America? Score 1-5:
        1 = Nice-to-have but not career-differentiating
        2 = Useful for specific roles or industries
        3 = Solid professional skill with steady demand
        4 = High-value skill that opens career opportunities
        5 = Critical career-advancing skill (AI/ML, cloud computing, data analysis, project management, leadership)
        """
    )

    career_impact_reasoning: str = Field(
        description="2-3 sentence explanation for the career impact score, including job market demand and salary/advancement potential"
    )

    # Summary
    total_score: int = Field(description="Sum of all three scores (3-15 total points)")

    priority_tier: Literal[
        "Strategic Priority (Tier 1)",
        "Strong Candidate (Tier 2)",
        "Tactical Partnership (Tier 3)",
        "Pass",
    ] = Field(
        description="""
        Overall partnership priority based on total score:
        13-15 points = Strategic Priority (Tier 1)
        10-12 points = Strong Candidate (Tier 2) 
        7-9 points = Tactical Partnership (Tier 3)
        3-6 points = Pass
        """
    )

    overall_assessment: str = Field(
        description="3-4 sentence summary of the partnership opportunity, highlighting key strengths/weaknesses and strategic rationale"
    )

    def model_post_init(self, __context) -> None:
        """Automatically calculate total score after initialization"""
        self.total_score = (
            self.general_recognition_score
            + self.domain_authority_score
            + self.career_impact_score
        )

        # Auto-assign priority tier based on score
        if self.total_score >= 13:
            self.priority_tier = "Strategic Priority (Tier 1)"
        elif self.total_score >= 10:
            self.priority_tier = "Strong Candidate (Tier 2)"
        elif self.total_score >= 7:
            self.priority_tier = "Tactical Partnership (Tier 3)"
        else:
            self.priority_tier = "Pass"


# Example usage:
# evaluation = PartnershipEvaluation(
#     partner_name="Microsoft",
#     certificate_topic="Azure AI Fundamentals",
#     general_recognition_score=5,
#     general_recognition_reasoning="Microsoft is a globally recognized technology leader...",
#     domain_authority_score=5,
#     domain_authority_reasoning="Microsoft Azure is the #2 cloud platform globally...",
#     career_impact_score=5,
#     career_impact_reasoning="AI skills are among the fastest growing and highest paying..."
# )
