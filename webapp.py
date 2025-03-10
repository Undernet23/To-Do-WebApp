import streamlit as st
import  functions

todos = functions.get_todos()

def add_todo():
    todo_local = st.session_state["new_todo"]
    # if todo_local not in todos and todo_local:
    todos.append(todo_local + '\n')
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


st.title("My to-do app.")
st.subheader("This is my to-do app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=f"{index}.{todo}")
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[f"{index}.{todo}"]
        st.rerun()

st.text_input(label=" " ,placeholder="Add new to-do...",
              on_change=add_todo, key='new_todo')