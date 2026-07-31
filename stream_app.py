import streamlit as st
import pandas as pd
import numpy as np
import datetime as dt
import requests
import streamlit as st, requests

st.title("Hello world!")

with st.sidebar:
    st.header('About app')
    st.write('This is my first web!')
st.header('This is a header with a divider', divider='rainbow')
st.text("This is just the beginning")
st.write('My_First_Web')


st.header("_Streamlit_ is :blue[cool] :sunglasses:")

if st.button("click me"):
    st.write('Hello timo, How can i help you today?')

st.button(" :red[Enter your first input]")

if st.button("Current Time"):
    st.write(dt.datetime.now())


st.subheader('Guess Age From Name')
name = st.text_input('Your Name')
if name:
    r=requests.get(f'https://api.agify.io/?name={name}').json()
    st.write(f'Your age is predicted to be {r["age"]}')



#st.header('Pokemon Images')
#mypokemon=['charizard', 'None ', 'pikachu','eevee','snorlax','garchomp','lucario']
#pokemon=st.selectbox('Select a Pokemon', mypokemon)
#if pokemon:
 #   r=requests.get(f'https://pokeapi.co/api/v2/pokemon/{pokemon}').json()
 #   for img in r['sprites'].values():
  #      if img is not None:
   #         if str(img)[-4:]=='.png':
    #            st.image(img)
#else pokemon
    
st.write('None')


st.subheader('Columns')
col1, col2 = st.columns(2)

with col1:
    x = st.slider('Choose an x value', 1, 10)
with col2:
    st.write('The value of :red[***x***] is', x)

st.subheader('Area_Chart')
chart_data = pd.DataFrame(np.random.randn(20, 3), columns=['a','b','c'])
st.area_chart(chart_data)

st.title('Title')
st.header('Header')
st.subheader('Subheader')
st.caption('Caption')
st.code('print("this is some code")')
st.text('Text')
st.markdown('- *Markdown*')
st.latex('\sum_{k=0}^{n-1} ar^k')
st.dataframe(pd.DataFrame({'a':[1, 2, 3],'b':['A', 'B', 'C']}))
st.table({'a':[1, 2, 3],'b':['A', 'B', 'C']})

col1, col2 = st.columns(2)
with col1:
    st.metric('Temp', '75', '5')
with col2:
    st.metric('Wind', '9', '-4')
st.json({'a':[1, 2, 3],'b':['A', 'B', 'C']})
st.button('Button')
st.download_button('Download Button', b'asdf')
st.checkbox('Checkbox')
st.radio('Radio',[1,2,3])
st.selectbox('Selectbox', ['a','b','c'])
st.multiselect('Multiselect', ['a','b','c'])
st.slider('Slider')
st.select_slider('Select Slider', ['a','b','c'])
st.text_input('Text Input')
st.number_input('Number Input')
st.text_area('Text Area')
st.date_input('Date Input')
st.time_input('Time Input')
st.file_uploader('File Uploader')
st.camera_input('Camera')
st.color_picker('Color Picker')
#st.image('tulips.jpg')
#st.audio('audio.mp3')
#st.video('video.mp4')
st.sidebar.selectbox('Menu', ['a','b','c'])
col1, col2 = st.columns([1,2])
col1.text_input('Thinner Column')
col2.text_input('Thicker Column')
tab1, tab2 = st.tabs(['TAB 1','TAB 2'])
tab1.text_area('text in tab 1')
tab2.date_input('date in tab 2')
st.expander('Expander')
st.container()
placeholder = st.empty()
placeholder.text('Hide this placeholder container')
if st.button('Hide'): placeholder.empty()

st.progress(35)
st.spinner('Spinner')

if st.checkbox('Balloons', False):
    st.balloons()
if st.checkbox('Snow', False):
    st.snow()
st.error('Error')
st.warning('Warning')
st.info('Info')
st.success('Success')
st.exception(RuntimeError('This is a fake error.'))
st.form('')
#st.form_submit_button('')



df=pd.DataFrame(np.random.randn(20, 3), columns=['a', 'b', 'c'])
st.line_chart(df)
st.area_chart(df)
st.bar_chart(df)
#treemap=pd.read_csv("C:/TIMO & AI/ML FOLDER/LinkedIn April.csv.csv")
#st.treemap = "my_module.ipynb"
#st.write(treemap)
#st.map(treemap)

note=st.text_input('Enter a Note') 
if note: 
        with open('notes.txt', 'a+') as file: 
            file.write(f'{note}\n') 

with open('notes.txt', 'r+') as file: 
    st.text(file.read())

with st.form('My Form', clear_on_submit=True): 
    name=st.text_input('Name') 
mrkdwn=st.text_area('Markdown', '## Subheader\n- item 1\n- item 2') 
file=st.file_uploader('Image', ['png', 'jpg', 'gif', 'bmp']) 
    #if st.form_submit_button('Submit'): 
     #         st.markdown(f'# {name}\n{mrkdwn}') 
      #        st.image(file)

with st.form('Form 1', clear_on_submit=True): 
        name=st.text_input('Name') 
        if st.form_submit_button('Update'): 
# run some database code 
            st.write(f'Name updated to {name}') 
            if st.form_submit_button('Delete'): 
# run some database code 
                st.write(f'Name {name} deleted') 
with st.form('Form 2', clear_on_submit=True): 
        hobby=st.text_input('Hobby') 
        if st.form_submit_button('Save'): 
# run some database code 
             st.write(f'{hobby} saved') 

message_area=st.empty() 
with st.form('Form 3', clear_on_submit=True): 
    name=st.text_input('Name') 
    if st.form_submit_button('Update'): 
# run some database code 
        message_area.write(f'Name updated to {name}') 
    if st.form_submit_button('Delete'): 
# run some database code 
        message_area.write(f'Name {name} deleted') 

if 'total' not in st.session_state: 
    st.session_state.total=0 
# st.session_state['total']=0  # synonymous with the line above 
if st.button('+'): 
    st.session_state.total+=1 
st.write(st.session_state.total) 

total=0 
if st.button('*'): 
    total+=1 
st.write(total)

@st.cache_data
def long_function(repetitions): 
    total=0 
    for reps in range(repetitions): 
        total+=1 
    return total 
val=st.number_input('count up to', value=99999999) 
if val: 
    st.write(f'first run:{long_function(val)}') 
st.write(f'second run, cached value appears quickly: {long_function(val)}') 


st.divider()

st.caption("""
Developed by **Folorunsho Timothy**

Machine Learning Engineer | Mobile App Developer | Mechatronics Engineering Student

📧 timothyfolorunsho995@gmail.com

This tool is intended for educational purposes only and does not replace professional medical diagnosis.
""")