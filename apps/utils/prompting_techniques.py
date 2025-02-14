from core.common.constants import PromptTechnique

prompting_techniques = {
    PromptTechnique.zero_shot_prompting: """
                You are a helpful assistant. Answer this question in a concise and informative way: {question}
            """,
    PromptTechnique.few_shot_prompting: """
                You are a helpful assistant. Answer the below question, here are some examples to guide you:
                Q: What is the capital of France? 
                A: Paris
                
                Q: Who wrote 'Pride and Prejudice'? 
                A: Jane Austen
                
                Q: A "whatpu" is a small, furry animal native to Tanzania. An example of a sentence that uses the word whatpu is:
                A: We were traveling in Africa and we saw these very cute whatpus.
                
                Q: {question}
                A:
            """,
    PromptTechnique.chain_of_thought_prompting: """
                You are a helpful assistant. Answer the below question, here are some examples to guide you:
                # Example:
                Let's break this down step by step:
                Q: The odd numbers in this group add up to an even number: 4, 8, 9, 15, 12, 2, 1.
                A: 
                    Step 1: All odd numbers are: 1, 9, 15
                    Step 2: Sum of odd numbers is: 1 + 9 + 15 = 25
                    Step 3: 25 is odd. The answer is False.
                    
                Q: {question}
                A:
            """,
    PromptTechnique.zero_shot_chain_of_thought_prompting: """
                You are a helpful assistant. Let’s think step by step and answer the below question:
                Q: {question}
                A:
            """,
    PromptTechnique.self_consistency_prompting: """
                You are a helpful assistant. Answer the below question by generating
                multiple reasoning paths for the following question and pick the most consistent answer:
                Q: {question}
                A: 
            """,
    PromptTechnique.tree_of_thoughts_prompting: """
                Imagine three different experts are answering this question.
                All experts will write down 1 step of their thinking,
                then share it with the group.
                Then all experts will go on to the next step, etc.
                If any expert realises they're wrong at any point then they leave.:
                Q: {question}
                Start by outlining possible approaches.
            """,
    PromptTechnique.directional_stimulus_prompting: """
                You are a helpful assistant.
                Answer this below question based on the hint included in the question if existed: 
                Q: {question}
            """,
    PromptTechnique.prompt_chaining_prompting: """
            Step 1: Extract Relevant Information
            You are a helpful assistant tasked with answering a question based on a provided combined input. 
            The input includes a user's question and the relevant context (document). 
            Your first step is to extract important information or quotes from the question and context that are relevant to answering the question. 
            Output the results in the format <relevant_info></relevant_info>. 
            Respond with "No relevant information found!" if no relevant information can be extracted.
    
            Combined Input:
            ####
            {question}
            ####
    
            Step 2: Compose the Answer
            Using the relevant extracted information (delimited by <relevant_info></relevant_info>), 
            compose a helpful, accurate, and friendly answer to the user's question. 
            Ensure that your response is well-structured, clear, and addresses the question directly.
    
            Combined Input:
            ####
            {question}
            ####
    
            <relevant_info>
            Output from Step 1
            </relevant_info>
        """
}
