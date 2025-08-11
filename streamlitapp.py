import os
import json
import traceback
import pandas as pd
from src.mcqgenerator.utils import read_file,get_table_data
import streamlit as st
from src.mcqgenerator.MCQgen import generate_evaluate_chain
from src.mcqgenerator.logger import logging



with open(r"D:\MCQgen\response.json", "r") as file:
    RESPONSE_JSON = json.load(file)


st.title("MCQs Generator")

with st.form("user_inputs"):
    uploaded_file = st.file_uploader("Upload a PDF or txt file")

    mcq_count = st.number_input("No. of MCQs",min_value=3,max_value=50)

    subject = st.text_input("Insert the subject",max_chars=20)

    tone=st.text_input("Complexity of Questions",max_chars=20,placeholder="Simple")

    button = st.form_submit_button("Create MCQs")

    if button and uploaded_file is not None and mcq_count and subject and tone:
        with st.spinner("loading..."):
            try:
                text=read_file(uploaded_file)
                response = generate_evaluate_chain({
                    "text":text,
                    "number":mcq_count,
                    "subject":subject,
                    "tone":tone,
                    "response_json":json.dumps(RESPONSE_JSON)
                })


            except Exception as e:
                st.error(f"Error: {e}")
                st.write(traceback.format_exc())



            else:
                if isinstance(response, dict):

                    quiz = response.get("quiz",None)
                    if quiz is not None:
                        table_data = get_table_data(quiz)
                        if table_data is not None:
                            df = pd.DataFrame(table_data)
                            df.index=df.index+1
                            st.table(df)
                            st.text_area(label="Review",value=response["review"])
                        else:
                            st.error("Error in the table data")

                else:
                    st.write(response)


                