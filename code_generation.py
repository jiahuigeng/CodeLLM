import pandas as pd
from prompts import *
from utils import *
from utils_llm import *
import argparse

# def code_gen_from_numpy_url(url, task, version, lib, func_name):
#     '''
#     '''
#     # func_name = "numpy.unstack"
#     # lib = "NumPy"
#     # version = '2.1.0'
#     # description
#     if lib == "numpy":
#         crawler = numpy_crawler
        
#     description = crawler(url)
#     if task == "completion":
#         res = get_gpt_complete_prompt(func_name=func_name, lib=lib, version= version, description=description)
        
#     return res
    
    
    
def numpy_code_generation():
    client = get_gpt_model()
    df_input = pd.read_excel("API_update.xlsx", sheet_name="numpy")
    print(df_input.__len__())
    for index, row in df_input.iterrows():
        print(index)
        api = row["API"]
        typ = row["Type"]
        text_description = row["Description"]
        link = row["Description_full_link"]
        version = row['Version']
        
        if typ == "new":
            # code_description = code_gen_from_numpy_url(link, task='completion', version=version, lib=lib, func_name=api)
            code_desc = numpy_crawler(link)
            df_input.at[index, "code_description"] = code_desc
            
            inp_pmp = get_gpt_complete_prompt(func_name=api, lib="numpy", version= version, description=description)
            res = prompt_gpt(client,inp_pmp)
            df_input.at[index, "code_completion"] = res
            
            
            
            
        elif typ == 'deprecated':
            # if "
            pass
            
        
        # elif typ == 'obsolate':
        #     pass
            
            
        
        df_input.to_excel("API_update.xlsx", sheet_name="numpy")
        
        
        
    


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--lib", default="numpy")
    
    args = parser.parse_args()
    
    if args.lib == "numpy":
        numpy_code_generation()
    # code_gen_from_url