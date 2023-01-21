
import React from "react"
import ReactDOM from "react-dom"
import TreeComponent from "./AntTree"

// Lots of import to define a Styletron engine and load the light theme of baseui


// Wrap your CustomSlider with the baseui them
ReactDOM.render(
  <React.StrictMode>
    <TreeComponent />
  </React.StrictMode>,
  document.getElementById("root")
)