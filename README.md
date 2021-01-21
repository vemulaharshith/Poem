# 📚 Poem Generator v2 ✒️
A RNN based Poem generator trained on Project Gutenberg's data from Shakespeare's sonnets. You can interact with the app [here](https://share.streamlit.io/sauravmaheshkar/poem-generator/main/app.py).

![](https://github.com/SauravMaheshkar/Poem-Generator/blob/main/assets/app.png)

The dataset used to train this model comes from Project Gutenberg EBook. The processed dataset was taken from Laurencemoroney's storage. You can find the processed data [here](https://storage.googleapis.com/laurencemoroney-blog.appspot.com/sonnets.txt). This project was largely inspired from the assignments from deeplearning.ai's Deep Learning Specialisation.

# Steps to Reproduce

## Docker Approach

```
docker pull docker.pkg.github.com/sauravmaheshkar/poem-generator/poem:v0.1
docker run -p 8501:8501 app:latest 
```

## Conda Approach

```
mkdir <project_name>
cd <project_name>
git init
git clone https://github.com/SauravMaheshkar/Poem-Generator.git
conda env create -f environment.yml
conda activate poem
streamlit run app.py
```
