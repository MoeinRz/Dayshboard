# *************************************************************************** */
#                                                                             */
#                                                                             */
#    assignment.py                                                            */
#                                                                             */
#    By: moeinrz <moeinrezaei330@gmail.com>                                   */
#                                                                             */
#    Created: 2022/12/18 22:04:59 by moeinrz                                  */
#    Updated: 2022/12/18 23:45:49 by moeinrz                                  */
#                                                                             */
# *************************************************************************** */

import streamlit as st

st.title(':zap: Moein Dashbpard')

import streamlit as st
agree = st.checkbox('I agree')

if agree:
    st.write('Great!')


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)

    # Can be used wherever a "file-like" object is accepted:
    dataframe = pd.read_csv(uploaded_file)
    st.write(dataframe)
