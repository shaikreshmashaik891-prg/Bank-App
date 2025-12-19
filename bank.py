import streamlit as st
import pandas as pd
from supabase import create_client


SUPABASE_URL = "https://wvfatffgraipglnjtihd.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Ind2ZmF0ZmZncmFpcGdsbmp0aWhkIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYxMTY1NTMsImV4cCI6MjA4MTY5MjU1M30.kNQw2YrY7Q9p1q1SA7qO8_WhNC5G-DHLwMAFkVfqaKU"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

#---------------------------------------------
#Streamlit UI
#---------------------------------------------
st.title("HDFC BANK (supabase)")
###########################################
menu =["REGISTER","VIEW"]
choice =st.sidebar.selectbox("Menu",menu)

#-------------------------------------------
# REGISTER
#-------------------------------------------
if choice=="REGISTER":
    name=st.text_input("Enter name")
    age=st.number_input("AGE",min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    bal=st.number_input("BALANCE",min_value=500)
    if st.button("Save"):
        supabase.table("users1").insert({
            "name":name,
            "age":age,
            "account":account,
            "balance":bal}).execute()
        st.success("users added successfully")
#--------------------------------------
# View Students
#--------------------------------------
if choice=="VIEW":
    st.subheader("view users1")
    data=supabase.table("users1").select("*").execute()
    df=pd.DataFrame(data.data)
    st.dataframe(df)
    
