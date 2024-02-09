from langchain_openai import OpenAI
from langchain.chains import LLMChain
from langchain.chains.base import Chain
from langchain.prompts import PromptTemplate
from typing import Dict, List

class ConcatenateChain(Chain):
    chain_1: LLMChain
    chain_2: LLMChain

    @property
    def input_keys(self) -> List[str]:
        all_input_vars = set(self.chain_1.input_keys).union(set(self.chain_2.input_keys))
        return all_input_vars

    @property
    def output_keys(self) -> List[str]:
        return ["concat_output"]

    def _call(self, inputs: Dict[str, str]) -> Dict[str, str]:
        output_1 = self.chain_1.run(inputs)
        output_2 = self.chain_2.run(inputs)
        return {"concat_output": output_1 + "\n" + output_2}

llm = OpenAI()

prompt_1 = PromptTemplate(
    template="{job}におすすめのプログラミング言語は何？\nプログラミング言語:",
    input_variables=["job"],
)
chain_1 = LLMChain(llm=llm, prompt=prompt_1, output_key="programming_language")

prompt_2 = PromptTemplate(
    template="{job}の学び方を教えて。",
    input_variables=["job"],
)
chain_2 = LLMChain(llm=llm, prompt=prompt_2, output_key="learning_step")

concat_chain = ConcatenateChain(chain_1=chain_1, chain_2=chain_2, verbose=True)
print(concat_chain.run("医者"))
