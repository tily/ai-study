from loguru import logger
from langchain.callbacks import FileCallbackHandler
from langchain.chains import LLMChain
from langchain_openai import OpenAI
from langchain.prompts import PromptTemplate

logfile = "output.log"
logger.add(logfile, colorize=True, enqueue=True)
handler = FileCallbackHandler(logfile)

llm = OpenAI()
prompt = PromptTemplate.from_template("1 + {number} = ")
chain = LLMChain(llm=llm, prompt=prompt, callbacks=[handler])
logger.info(chain.run(number=2))

