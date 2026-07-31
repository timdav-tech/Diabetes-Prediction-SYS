import streamlit as st, random, time, datetime
import sqlite3
import ast
#import os  

# Connect to the database
con = sqlite3.connect("db.db")
cur = con.cursor()

# Create the table if it doesn't exist
cur.execute("""
CREATE TABLE IF NOT EXISTS people (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    letters TEXT,
    note TEXT
)
""")
con.commit()

st.title("Hello World")

# Data to store
name = "John Doe"
letters = ["A", "B", "C"]
note = "John is from Ohio"

# Insert a new row
if st.button('Add New Row'):
    cur.execute(
    "INSERT INTO people (name, letters, note) VALUES (?, ?, ?)",
    (name, str(letters), note)
)
con.commit()

# Display all rows
for row in cur.execute(
    "SELECT id, name, letters, note FROM people ORDER BY name"
):
    person_id = row[0]
    name = row[1]
    letters = ast.literal_eval(row[2])
    note = row[3]

    st.write(f"ID: {person_id}")
    st.write(f"Name: {name}")
    st.write(f"Letters: {letters}")
    st.write(f"Note: {note}")
    st.write("---")

for row in cur.execute('SELECT rowid, name, letters, note FROM db ORDER BY name'): 
  with st.expander(row[1]): 
    with st.form(f'ID-{row[0]}'): 
      name=st.text_input('Name', row[1]) 
      letters=st.multiselect('Letters', ['A', 'B', 'C'], ast.literal_eval(row[2])) 
      note=st.text_area('Note', row[3])
      if st.form_submit_button('Save'): 
        cur.execute( 
          'UPDATE db SET name=?, letters=?, note=? WHERE name=?;',  
          (name, str(letters), note, str(row[1])) 
        ) 
        con.commit() 
        #
      if st.form_submit_button("Delete"): 
        cur.execute(f'DELETE FROM db WHERE rowid="{row[0]}";') 
        con.commit() 
       # st.rerun() 

if st.button('Add New option'): 
  cur.execute('INSERT INTO db(name, letters, note) VALUES(?,?,?)', ('','[]','')) 
  con.commit() 

time.sleep(1) 
coins = ['http://re-bol.com/heads.jpg', 'http://re-bol.com/tails.jpg'] 
coin = random.choice(coins) 
st.image(coin) 
if st.button('Flip'): 
    st.rerun() 


cam=st.selectbox( 
'Choose a Cam',  
[ 
'', 
'pitriverbridge/pitriverbridge.jpg', 
'johnsongrade/johnsongrade.jpg', 
'perez/perez.jpg', 
'mthebron/mthebron.jpg', 
'eurekaway/eurekaway.jpg', 
'sr70us395/sr70us395.jpg', 
'bogard/bogard.jpg', 
'eastriverside/eastriverside.jpg', 
] 
) 
if cam: 
    st.image('https://cwwp2.dot.ca.gov/data/d2/cctv/image/' + cam)


con.commit()

st.subheader('Time & Date')
if st.button('Now'):
   now = datetime.datetime.now
   st.write(now())

st.subheader('Number of words')
text = st.text_area('Type or paste some  text') 
if text: 
  words = text.split() 
st.write(f'Number of words in your text:\n\n{len(words)}')

st.subheader('Latin Generator')
text = st.text_area('Type some  text') 
if text: 
  word_list = text.split(' ') 
  pig_latin = ' ' 
  for word in word_list: 
    if word.isalpha(): 
      pigword = word[1:] + word[0] + 'ay' 
      pig_latin = pig_latin + pigword + ' ' 
    else: 
      pig_latin += word 
  st.write(pig_latin.strip(' '))

st.subheader('Calculator')
if 'total' not in st.session_state: 
  st.session_state.total='' 
if st.button('Clear'): st.session_state.total='' 
col1, col2, col3, col4, col5=st.columns([1,1,1,3,4]) 
if col1.button(':red[1]'): st.session_state.total+='1' 
if col2.button(':blue[2]'): st.session_state.total+='2' 
if col3.button('3'): st.session_state.total+='3' 
if col4.button('+'): st.session_state.total+='+' 
if col1.button('4'): st.session_state.total+='4' 
if col2.button('5'): st.session_state.total+='5' 
if col3.button('6'): st.session_state.total+='6' 
if col4.button('-'): st.session_state.total+='-' 
if col1.button('7'): st.session_state.total+='7' 
if col2.button('8'): st.session_state.total+='8' 
if col3.button('9'): st.session_state.total+='9' 
if col4.button('.'): st.session_state.total+='.' 
if col1.button('0'): st.session_state.total+='0' 
if col2.button('*'): st.session_state.total+='*' 
if col3.button('/'): st.session_state.total+='/' 
if col4.button('='):  
  st.session_state.total=str(eval(st.session_state.total)) 
st.text_input('Result', st.session_state.total)

st.subheader('Markdown Editor')
code=st.text_area('Markdown Code') 
if code: 
  st.markdown(code) 


# Uncomment the line above to delete the file containing 
# all messages, and start over with a fresh chat room. 
col1, col2=st.columns([1,1]) 
with col2: 
  with open('chat.txt', 'a+') as file: pass 
  with open('chat.txt', 'r+') as file: 
    msg=file.read() 
st.text_area('msg', msg, height=150, label_visibility='collapsed') 
with col1: 
  with st.form('New Message', clear_on_submit=True): 
        name=st.text_input('Name') 
        message=st.text_area('Message')  
        timestamp=datetime.datetime.now() 
        if st.form_submit_button('Add Message'): 
         newmsg = (f'---  {name}   {timestamp}\n\n{message}\n\n{msg}')
st.write('this is the beginning')

st.subheader('Minimal Cash Register')
if 'purchased' not in st.session_state: 
  st.session_state.purchased=[] 
with st.form('Add Item', clear_on_submit=True): 
  itmcol, prccol, btncol=st.columns([6,2,1]) 
  item=itmcol.text_input('Item', placeholder='item', label_visibility='collapsed') 
  price=prccol.number_input('Price', label_visibility='collapsed') 
  if btncol.form_submit_button('Add'): 
    timestamp=datetime.datetime.now() 
    st.session_state.purchased.append({'item': item, 'price': price}) 
    st.markdown('---') 
    itemcol, pricecol=st.columns([4,1]) 
    subtotal=0 
    for itm in st.session_state.purchased: 
      itemcol.write(itm['item']) 
      pricecol.write(itm['price']) 
      subtotal += (itm['price']) 
    st.markdown('---') 
    plccol, lblcol, numcol=st.columns([3,1,1]) 
    lblcol.write('Subtotal') 
    numcol.write('{:.2f}'.format(subtotal)) 
    lblcol.write('Tax') 
    numcol.write('{:.2f}'.format(subtotal* .06)) 
    lblcol.write('Total') 
    numcol.write('{:.2f}'.format(subtotal * 1.06))
        
with open('chat.txt', 'w') as file: 
  file.write(newmsg)




con.close()


#4432 5226 3489 1850



