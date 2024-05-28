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
    st.rerun()
# Adaugă stiluri CSS


st.markdown("""
    <style>
    .delete-button {
        background-color: red;
        color: white;
        border: none;
        padding: 0.5em 1em;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        
        font-size: 1em;
        margin: 0.2em;
        cursor: pointer;
        border-radius: 4px;
    }
    .delete-button:hover {
        background-color: darkred;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("My Todo App")
st.subheader("This is my todo app!")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    col1, col2 = st.columns([0.8, 0.2])
    with col1:
        st.text(todo)
    with col2:
        # Folosește stilul CSS personalizat pentru butonul de ștergere
        if st.button("Delete", key=f"delete_{index}", on_click=lambda i=index: delete_todo(i),
                     args=(index,), help="Click to delete this todo", use_container_width=True):
            st.markdown(f'<button class="delete-button">Delete</button>', unsafe_allow_html=True)

st.text_input(label="Adauga ToDo", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')

print("Is Working!")
# streamlit run web.py
