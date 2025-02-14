from typing import Optional

from pydantic import BaseModel, Field

from core.common.constants import PromptTechnique


class UserQuestionSchema(BaseModel):
    question: str
    prompt_technique: Optional[PromptTechnique] = Field(
        default=None,
        description="""
            The prompting technique to use. 
            Options: zero_shot_prompting, few_shot_prompting, chain_of_thought_prompting, self_consistency_prompting, 
            tree_of_thoughts_prompting, directional_stimulus_prompting, prompt_chaining_prompting. Can be null.
        """
    )
