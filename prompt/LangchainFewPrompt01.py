from langchain.prompts.few_shot import FewShotPromptTemplate
from langchain.prompts.prompt import PromptTemplate
from langchain.prompts.example_selector import SemanticSimilarityExampleSelector
from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings

examples = [
  {
    "question1": "Who lived longer, Muhammad Ali or Alan Turing?",
    "answer":"2"
  }
]

if __name__ == '__main__':
    # 使用PromptTemplate 给出两个变量。 在给出一个模版，使用了变量对应的占位符
    example_prompt = PromptTemplate(input_variables=["question1", "answer"], template="Question: {question1}\n{answer}")
    # 将examples第一个内容给到使用PromptTemplate 并将内容按照template 格式化后输出
    print(example_prompt.format(**examples[0]))

    # 将examples的内容按照example_prompt进行格式化  然后再拼接上suffix
    # prompt = FewShotPromptTemplate(
    #     examples=examples,
    #     example_prompt=example_prompt,
    #     suffix="Question: {input}",
    #     input_variables=["input"]
    # )
    # print(prompt.format(input="Who was the father of Mary Ball Washington?"))

    example_selector = SemanticSimilarityExampleSelector.from_examples(
        # This is the list of examples available to select from.
        examples,
        # This is the embedding class used to produce embeddings which are used to measure semantic similarity.
        OpenAIEmbeddings(openai_api_key="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"),
        # This is the VectorStore class that is used to store the embeddings and do a similarity search over.
        Chroma,
        # This is the number of examples to produce.
        k=1
    )

    question = "Who was the father of Mary Ball Washington?"
    selected_examples = example_selector.select_examples({"question": question})
    print(f"Examples most similar to the input: {question}")
    for example in selected_examples:
        print("\n")
        for k, v in example.items():
            print(f"{k}: {v}")