# Interactive Password Strength Meter & Generator

import streamlit as st
import random
import re
import string

st.set_page_config(
    page_title='Password Strength Meter & Generator',
    page_icon=':material/lock:',
    layout='centered'
)

st.title(':material/lock: Password Strength Meter & Generator')

# Navigation Tab - 2nos
tab1, tab2 = st.tabs(['Password Strength Meter', 'Password Generator'])

# Tab-1 : Password Strength Meter
with tab1:
    st.subheader('Evaluate Your Password')

    password = st.text_input(
        'Type or Paste Your Password Below:',
        type='password',
        key='pwd_input'
    )

    if password:
        # Rule evaluations using Regular Expression(regex) and string checks
        length_ok = len(password) >= 8
        upper_ok = bool(re.search(r'[A-Z]', password))
        lower_ok = bool(re.search(r'[a-z]', password))
        digit_ok = bool(re.search(r'\d', password))
        spchar_ok = bool(re.search(r'[@$!%*?&^#]', password))

        # Compute overall score out of 5
        score = sum([length_ok, upper_ok, lower_ok, digit_ok, spchar_ok])

        st.markdown('### Security Analysis')

        progress_val = score / 5

        st.progress(
            progress_val,
            text=f'Strength Score:{score}/5({int(progress_val*100)}%)'
        )

        # Visual Feedback based on Score
        if score == 5:
            st.success("**Strong Password!** Excellent Security Practices")
        elif score >= 3:
            st.warning('**Moderate Password!** Consider Adding Missing Character Types')
        else:
            st.error('**Weak Password!** Consider Adding Missing Character Types')

        # Requirements Checklist
        st.markdown('### Criteria Checklist:')

        st.checkbox(
            'At least 8 Characters long',
            value=length_ok,
            disabled=True
        )
        st.checkbox(
            'Contains Uppercase Letters(A-Z)',
            value=upper_ok,
            disabled=True
        )
        st.checkbox(
            'Contains Lowercase Letters(a-z)',
            value=lower_ok,
            disabled=True
        )
        st.checkbox(
            'Contains Numbers(0-9)',
            value=digit_ok,
            disabled=True
        )
        st.checkbox(
            'Contains Special Characters(@$!%*?&^#)',
            value=spchar_ok,
            disabled=True
        )

    else:
        st.info('Please Enter A Password Above to See Its Security Breakdown.')

# Tab-2: Password Generator
with tab2:
    st.subheader('Generate a Secured Password')

    pass_len = st.slider('Select Password Length:', 6, 32, 12)

    use_upper = st.checkbox('Include Uppercase Letters(A-Z)', value=True)
    use_lower = st.checkbox('Include Lowercase Letters(a-z)', value=True)
    use_digit = st.checkbox('Include Numbers(0-9)', value=True)
    use_spchar = st.checkbox('Include Special Characters(@$!%*?&^#)', value=True)

    if st.button('Generate Secure Password'):
        char_pool = ""

        if use_upper:
            char_pool += string.ascii_uppercase

        if use_lower:
            char_pool += string.ascii_lowercase

        if use_digit:
            char_pool += string.digits

        if use_spchar:
            char_pool += string.punctuation

        if not char_pool:
            st.error('Please Select atleat one character type option!')
        else:
            generated_password = "".join(
                random.choice(char_pool) for _ in range(pass_len)
            )

            st.success('Your Secured Password')
            st.code(generated_password, language="")