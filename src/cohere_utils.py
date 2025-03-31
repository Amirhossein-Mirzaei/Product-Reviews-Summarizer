from langchain_community.llms import Cohere
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Define PromptTemplate
summarizer_prompt = PromptTemplate(
    input_variables=['review_text'],
    template="""
     متن زیر شامل یک یا چند کامنت بررسی کاربران در مورد یک محصول به خصوص است. لطفاً یک خلاصه کوتاه از تمام نظرات ایجاد کرده به نحوی که نیاز به بررسی کردن و خواندن تمام نظرات توسط کابران نباشدو لحن دوستانه و در عین حال حرفه ای داشته باشد
    و مزایا و معایب اصلی را فهرست کنید به طوریکه حداکثر هر مورد آن ۳ یا ۴ کلمه و به صورت کاملا خلاصه باشد از تولید متن طولانی در قسمت مزایا و معایب پرهیز کن و خلاصه در حد سه یا چهار کلمه بنویس:

    بررسی: "{review_text}"

    **خلاصه:**
    **مزایا:**
    - 
    **معایب:**
    - 
    """
)

# Define a function for generating summary and pros/cons
def generate_summary_and_pros_cons(review_text: str, cohere_api_key: str) -> dict:

    llm = Cohere(cohere_api_key=cohere_api_key, model='command-r-plus', max_tokens=200)
    summarizer_chain = LLMChain(llm=llm, prompt=summarizer_prompt)

    output = summarizer_chain.run(review_text=review_text)

    # Initialize sections
    summary_section = ""
    pros_section = ""
    cons_section = ""

    # Check if the expected sections are present in the output
    if "**مزایا:**" in output and "**معایب:**" in output:
        summary_section = output.split("**مزایا:**")[0].strip()
        pros_section = output.split("**مزایا:**")[1].split("**معایب:**")[0].strip()
        cons_section = output.split("**معایب:**")[1].strip()
    else:
        raise ValueError("Output format is not as expected")

    return summary_section, pros_section, cons_section
