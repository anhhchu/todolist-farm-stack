import axios from "axios";
import React from "react";

const BASE_URL = `${process.env.REACT_APP_API_URL}/api/todo`;

function TodoItem(props) {
  const deleteTodoHandler = (title) => {
    axios.delete(`${BASE_URL}/${title}`).then((res) => console.log(res.data));
  };
  return (
    <div>
      <p>
        <span style={{ fontWeight: "bold, underline" }}>
          {props.todo.title} : {props.todo.description}
        </span> 

        <button
          onClick={() => deleteTodoHandler(props.todo.title)}
          className="btn btn-outline-danger my-2 mx-2"
        >
          X
        </button>
      </p>
    </div>
  );
}

export default TodoItem;