import streamlit as st
import functions

todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state["new_todo"]
    todos.append(todo_local)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""


def delete_todo(index_local):
    todos.pop(index_local)
    functions.write_todos(todos)
    # st.rerun()


st.title("My Todo App")
st.subheader("This is my todo app!")
st.write("This app is to increase your productivity.")

st.text_input(label="Adauga ToDo", placeholder="Add new todo... and press ENTER",
              on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.text(f"{index + 1}. " + todo)
    with col2:
        if st.button("Delete", type="primary", key=f"delete_{index}", on_click=lambda i=index: delete_todo(i),
                     args=(index,), use_container_width=True):
            pass

print("It's Working!")
