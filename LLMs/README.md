### Files description:

* Agent_MP_LangChain.ipynb contains the code for the Chat Agent based on pretraind ChatGPT moodel agumented with tools.
  The agent can request the information about chemical system from Materials Project (https://next-gen.materialsproject.org/)
  answer questions using this information, and plot phase diagram.
* extract_paper_data_llama3.py is a script to extract additional information on Li-ion materials from the collection of papers on Li-ion conductore with llama3 model.
  The results of extruction are summarised in LiIonDatabase_extracted_info.xlsx. This was done as a part of unfinished project about using
  embedding of additional information (which we extracted) to enhance representations of materials via concatinating the representation derived
  by CrabNet encoder from composition, and encoding produced by LLM embedder from textual description of a compound based on extracted information.
