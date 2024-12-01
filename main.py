import streamlit as st

def is_number(num):
    return num.isdigit()

def validation(num):
    first_checksum = 0
    second_checksum = 0
    
    for i in range(len(num)-1, -1, -1):
        tmp_digit = int(num[i])
        if i & 1:
            first_checksum += tmp_digit
            tmp_digit *= 2
            second_checksum += (tmp_digit // 10 + tmp_digit % 10)
        else:
            second_checksum += tmp_digit
            tmp_digit *= 2
            first_checksum += (tmp_digit // 10 + tmp_digit % 10)
            
    return (first_checksum % 10 == 0 or second_checksum % 10 == 0) and len(num) >= 13

def get_card_brand(num):
    if num[0] == '3' and num[1] in ['4', '7'] and len(num) == 15:
        return "AMEX"
    elif num[0] == '5' and int(num[1]) <= 5 and len(num) == 16:
        return "MASTERCARD"
    elif (num[0] == '4' and len(num) == 13) or (num[0] == '4' and int(num[1]) <= 6 and len(num) == 16):
        return "VISA"
    else:
        return "INVALID"

st.set_page_config(page_title="Credit Card Validator", page_icon="💳")

st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTitle {
        color: #2E4053;
        font-size: 3rem !important;
        padding-bottom: 2rem;
    }
    .stTextInput > div > div > input {
        font-size: 1.2rem;
        padding: 1rem;
    }
    .stSuccess, .stError, .stWarning {
        font-size: 1.2rem;
        padding: 1rem;
        border-radius: 0.5rem;
        margin-top: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Credit Card Validator")

col1, col2, col3 = st.columns([1,2,1])
with col2:
    num = st.text_input("Enter Credit Card Number:", "", help="Enter a valid credit card number to verify")

    if num:
        if is_number(num):
            if validation(num):
                result = get_card_brand(num)
                if result == "INVALID":
                    st.error("INVALID")
                else:
                    st.success(f"Valid {result} Card ✅")
        else:
            st.warning("Please enter numbers only ⚠️")