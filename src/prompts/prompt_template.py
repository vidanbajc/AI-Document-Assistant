from langchain_core.prompts import ChatPromptTemplate

def get_prompt_template() -> ChatPromptTemplate:
    prompt = ChatPromptTemplate.from_messages([

        ("system", """You are an AI assistant that answers questions using only provided context. 
                      Rules:
                        - Answer only what the user asked.
                        - Do not add unnecessary explanations.
                        - Do not repeat the question.
                        - Do not mention the context, documents, or file names in your answer.
                        - Match answer length to the complexity of the question, short questions deserve short answers, max 3-4 sentences.
                        - Always respond in the same language the question was asked in.
                        - If the answer is not in the context, say: "I don't have enough information about this topic."
                      Provide a clear and natural response."""),

        ("human", """Context: {context} 
                     Question: {question}""")
    ])

    return prompt