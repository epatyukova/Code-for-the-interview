#imports
import fitz
import transformers
import torch
import pandas as pd
import os
import fitz  # PyMuPDF
import shutil
import numpy as np
import re

def extract_conclusion(pdf_path):
    pdf_document = fitz.open(pdf_path)
    context=''
    conclusion_switch=False
    for page in pdf_document:
        #test=page.get_text('text')
        #if(re.search('structure',text.lower())):
            #context+=text
        text=page.get_text("text")
        text=text.replace('\n','')
        text=text.replace('- ','')
        if(re.search('conclusion',text.lower())):
            conclusion_switch=True
        if(conclusion_switch==True):
            context+=text
    
    context_words=context.split(' ')
    new_context=''
    for x in context_words:
        if(not re.search('acknowledg',x.lower())):
            new_context+=x+' '
        else:
            break
    
    pdf_document.close()

    return new_context


def extract_data(df_path: str,
                 pdfs_path: str):
    
    #Loading up dataset
    df = pd.read_csv(df_path)
    model_id = "meta-llama/Meta-Llama-3-8B-Instruct"

    pipeline = transformers.pipeline(
        "text-generation",
        model=model_id,
        model_kwargs={"torch_dtype": torch.float16},
        device_map="auto",
        token='your_token')
    
    conclusion=[]
    
    # for i in range(len(df)):
    for i in range(len(df)):
        doi=df.iloc[i]['source']
        compound=df.iloc[i]['composition']
        pdf_path=pdfs_path+doi.replace('/',' ')+'.pdf'
        #print(pdf_path)
        try:
            context=extract_conclusion(pdf_path)
            #print(len(context))
        except:
            context=''
            #print(len(context))

        prompt = "What are structure property relationship in"+compound+"? Try to make it shorter."

        messages = [
        {"role": "system", "content": context},
        {"role": "user", "content": prompt},
        ]

        prompt = pipeline.tokenizer.apply_chat_template(
            messages, 
            tokenize=False, 
            add_generation_prompt=True
        )

        terminators = [
        pipeline.tokenizer.eos_token_id,
        pipeline.tokenizer.convert_tokens_to_ids("<|eot_id|>")
        ]

        outputs = pipeline(
            prompt,
            max_new_tokens=256,
            eos_token_id=terminators,
            do_sample=True,
            temperature=0.2,
            top_p=0.9)
        conclusion.append(outputs[0]["generated_text"][len(prompt):])

    df['strcut-prop']=conclusion
    df.to_csv('result.csv')
    # response = outputs[0]["generated_text"][len(prompt):]
    # response = response.replace('\x01', '') #eliminating some ASCII characters
    # response = response.replace('\x05', '')
    # df.loc[df['source'] == doi, '{se}'] = response
    # df.to_excel('datasets/LiIonDatabase.xlsx', index=False)

if __name__ == '__main__':
    extract_data(df_path='LiIonDatabase.csv', 
                 pdfs_path='Li-ion-papers/')
