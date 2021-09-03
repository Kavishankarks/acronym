import streamlit as st
from PIL import Image
import json

# dic={"ikr":"I Know Right",'lol':"Laugh out loud",'ig':'I guess!','ik':'I know',"wth":"what the hell",':)':'😂'}

dic={}
json_object = json.dumps(dic, indent = 4)

def write():
	json_object = json.dumps(dic, indent = 4)
	with open("acronyms.json", "w") as outfile:
	    outfile.write(json_object)

with open("acronyms.json","r") as file:
	dic1=json.load(file)

dic=dic1

def display():
	st.title("   \t\tAcronym for your texts")
	# st.error("(No more scratching head)")
	st.write("Designed by Kavishankar K S")

def word(a):
    if(a in dic):
    	return dic[a]
    if(a==None or a==""):
    	st.write("Search words")
    return "Not found please can you add if you find it anywhere! "

def addWord():
	st.write("\n\n")
	st.markdown("**_Contribute to this to help others 😊😊:)_**")
	st.write("just add your own words")
	word=st.text_input(label="Enter word to add:")
	if word not in dic:
		dic[word]=st.text_input(label="Enter abrevation of "+word+" :")
		if(dic[word]!=""):
			write()
			st.balloons()
			st.write("thank you we are glad and your word has been added!")
	else:
		st.success("**_Acronym is present:_** "+dic[word])
	
if __name__=='__main__':
	display()
	a=st.text_input(label="Enter word:")
	st.success('**_Acronym:_**  '+word(a))
	# st.text_input(label='Enter abbrevation:')
	addWord()
	image = Image.open('acronyms.jpg')
	st.image(image, caption='word cloud')
	st.title("All added words by our community")
	st.write(dic)


# json_object=json.dumps(dic)

# st.write(json_object)

# with open("sample.json", "a+") as outfile:
#     outfile.write(json_object)

# with open('sample.json', 'r') as openfile:
#     # Reading from json file
#     json_object = json.load(openfile)
#     # st.write(json_object)
