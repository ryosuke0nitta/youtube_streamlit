import streamlit as st

import time

st.title('Stramlit')
st.write('Dataframe')


st.write('プログレスバー')
latest_iteration=st.empty()
bar=st.progress(0)
for i in range(100):
    latest_iteration.text(f'iteraton{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)

st.write('Display Image')

l,r=st.columns(2)
button=l.button('aa')
if button:
    r.write('fds')

expander=st.expander('問い合わせ')
expander.write('問い合わせ')
option=st.text_input('あなたの趣味')
'あなたが好きな数字は',option,'です'

condition=st.slider('a',0,100,50)
'コンディション：',condition
# if st.checkbox('Show Image'):
#     img= Image.open(r'C:\Users\ryo94\udemy\pythonwebapp\test1_resize.jpg')
#     st.image(img,caption='yes',use_column_width=True)



#st.dataframe(df)

"""
# 章
## 項
"""