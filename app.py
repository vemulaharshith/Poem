import json
import streamlit as st
from tensorflow.keras.models import load_model
from keras_preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences

def load_data():

    model = load_model("data/Shakespeare.h5", compile = False)

    with open('data/tokenizer.json') as f:
        data = json.load(f)
        tokenizer = tokenizer_from_json(data)

    return model, tokenizer

model, tokenizer = load_data()

def generate(seed_text, next_words = 50):
  for _ in range(next_words):
	  token_list = tokenizer.texts_to_sequences([seed_text])[0]
	  token_list = pad_sequences([token_list], maxlen=10, padding='pre')
	  predicted = model.predict_classes(token_list, verbose=0)
	  output_word = ""
	  for word, index in tokenizer.word_index.items():
		  if index == predicted:
			  output_word = word
			  break
	  seed_text += " " + output_word

  return seed_text


## Basic Page Setup
st.set_page_config(page_title = "Poem Generator",
    page_icon = "📚")
st.title("✒️ Poem Generator")
st.markdown("---")

## Sidebar
st.sidebar.header("📚 An RNN based Poem generator trained on Project Gutenberg's data from Shakespeare's sonnets ✒️")
st.sidebar.markdown("---")
st.sidebar.markdown("Here's the [link](https://storage.googleapis.com/laurencemoroney-blog.appspot.com/sonnets.txt) to the processed dataset from Laurencemoroney , which was originally extracted from The Project Gutenberg EBook of Shakespeare's Sonnets, by William Shakespeare")

## Text Input
text = st.text_input("Enter first line", value = "Help me Saurav, you're my only hope")

## Button
if st.button("Generate"):
    poem = generate(text)
    st.write(poem)

## End Credits
st.markdown("---")
st.markdown("If you liked this project and would like to read the code and see some of my other work, don't forget to ⭐the [repository](https://github.com/SauravMaheshkar/Poem-Generator) and follow [me](https://github.com/SauravMaheshkar).")
