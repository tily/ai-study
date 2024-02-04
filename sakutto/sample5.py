from langchain.prompts.example_selector.base import BaseExampleSelector
from typing import Dict, List
import numpy as np

class CustomExampleSelector(BaseExampleSelector):

    def __init__(self, examples: List[Dict[str, str]]):
        self.examples = examples

    def add_example(self, example: Dict[str, str]) -> None:
        self.examples.append(example)

    def select_examples(self) -> List[dict]:
        return np.random.choice(self.examples, size=2, replace=False)

examples = [
    {"fruit": "りんご", "color": "赤"},
    {"fruit": "なし", "color": "青"},
    {"fruit": "マンゴー", "color": "黒"},
]

example_selector = CustomExampleSelector(examples)
print(example_selector.examples)

example_selector.add_example({"fruit": "オレンジ", "color": "だいたい"})
print(example_selector.examples)

print(example_selector.select_examples())
