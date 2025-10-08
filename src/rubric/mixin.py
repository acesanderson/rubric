from pydantic import BaseModel, Field
from typing import Literal


class PartnershipEvaluationMixin:
    """
    Mixin providing business logic and human-readable methods for partnership evaluations
    """

    @property
    def rubric(self) -> str:
        """
        Returns a general description of the LinkedIn Learning Partnership Evaluation Rubric
        """
        return """
LinkedIn Learning Partnership Evaluation Rubric

This rubric evaluates potential Professional Certificate partnerships using three key dimensions (15 points total):

1. Partner General Recognition (1-5 points)
   How well-known is this brand to the general professional audience?
   • 5 = Household names (Microsoft, Google, Adobe)
   • 1 = Unknown outside their specific niche

2. Partner Domain Authority (1-5 points) 
   How respected is this partner specifically in this skill area?
   • 5 = THE recognized expert/leader in this domain
   • 1 = Not known for this particular skill area

3. Skill Career Impact (1-5 points)
   How much does this skill boost career prospects in North America?
   • 5 = Critical career-advancing skills (AI, cloud, data, leadership)
   • 1 = Nice-to-have but not career-differentiating

Priority Classification:
• 13-15 points: Strategic Priority (Tier 1) - Immediate pursuit
• 10-12 points: Strong Candidate (Tier 2) - High priority  
• 7-9 points: Tactical Partnership (Tier 3) - Consider if resources allow
• 3-6 points: Pass unless exceptional circumstances

Focus: North American market, individual career development perspective.
        """.strip()

    @property
    def human_readable_summary(self) -> str:
        """
        Returns a natural language description of the evaluation for human audiences
        """

        # Score interpretation helpers
        def score_to_text(score: int, dimension: str) -> str:
            levels = {1: "very low", 2: "low", 3: "moderate", 4: "high", 5: "very high"}
            return f"{levels[score]} {dimension}"

        recognition_desc = score_to_text(
            self.general_recognition_score, "brand recognition"
        )
        authority_desc = score_to_text(self.domain_authority_score, "domain expertise")
        impact_desc = score_to_text(self.career_impact_score, "career impact")

        # Priority tier explanation
        tier_explanations = {
            "Strategic Priority (Tier 1)": "immediate pursuit recommended",
            "Strong Candidate (Tier 2)": "high priority for partnership development",
            "Tactical Partnership (Tier 3)": "consider if resources allow",
            "Pass": "partnership not recommended unless exceptional circumstances",
        }

        tier_explanation = tier_explanations[self.priority_tier]

        return f"""
{self.partner_name}'s "{self.certificate_topic}" certificate scores {self.total_score}/15 points ({self.priority_tier.lower()}).

The partnership features {recognition_desc} among professionals, {authority_desc} in this specific skill area, and {impact_desc} for learners' career advancement. This combination suggests {tier_explanation}.

Key strengths: {self._identify_strengths()}
{self._identify_concerns()}
        """.strip()

    def _identify_strengths(self) -> str:
        """Helper to identify key partnership strengths"""
        strengths = []
        if self.general_recognition_score >= 4:
            strengths.append("strong brand recognition")
        if self.domain_authority_score >= 4:
            strengths.append("established domain authority")
        if self.career_impact_score >= 4:
            strengths.append("high-value skill for career advancement")

        if not strengths:
            strengths.append("solid foundation for partnership development")

        return ", ".join(strengths)

    def _identify_concerns(self) -> str:
        """Helper to identify potential partnership concerns"""
        concerns = []
        if self.general_recognition_score <= 2:
            concerns.append("limited brand awareness")
        if self.domain_authority_score <= 2:
            concerns.append("weak domain expertise")
        if self.career_impact_score <= 2:
            concerns.append("limited career advancement value")

        if concerns:
            return f"Areas for consideration: {', '.join(concerns)}"
        else:
            return "No significant concerns identified."


class PartnershipEvaluation(PartnershipEvaluationMixin, BaseModel):
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
