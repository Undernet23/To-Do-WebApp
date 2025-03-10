import streamlit as st
import  functions

todos = functions.get_todos()

st.set_page_config(layout="wide")

def add_todo():
    todo_local = st.session_state["new_todo"]
    # if todo_local not in todos and todo_local:
    todos.append(todo_local + '\n')
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My To-Do App.")
st.subheader("Below you can add things that you plan to do.")
st.write("This app can be used to <b>increase your productivity</b>.",
         unsafe_allow_html=True)


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}.{todo}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{index}.{todo}"]
        st.rerun()

st.text_input(label=" " ,placeholder="Add new to-do...",
              on_change=add_todo, key='new_todo')