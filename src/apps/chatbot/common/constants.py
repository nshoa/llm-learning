from enum import Enum


class PromptTechnique(str, Enum):
    zero_shot_prompting = "zero_shot_prompting"
    few_shot_prompting = "few_shot_prompting"
    chain_of_thought_prompting = "chain_of_thought_prompting"
    zero_shot_chain_of_thought_prompting = "zero_shot_chain_of_thought_prompting"
    self_consistency_prompting = "self_consistency_prompting"
    tree_of_thoughts_prompting = "tree_of_thoughts_prompting"
    directional_stimulus_prompting = "directional_stimulus_prompting"
    prompt_chaining_prompting = "prompt_chaining_prompting"
