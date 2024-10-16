import pandas as pd
from prompts import *
from utils import *
from utils_llm import *


def code_gen_from_url(url, task, lib, vision, func_name):
    '''
    '''
    # func_name = "numpy.unstack"
    # lib = "NumPy"
    # version = '2.1.0'
    # description
    if lib == "numpy":
        crawler = numpy_crawler
        
    description = crawler(url)
    if task == "completion":
        get_gpt_complete_prompt(func_name=func_name, lib=lib, description=description)
    
    
    
    
    


if __name__ == "__main__"::
    code_gen_from_url