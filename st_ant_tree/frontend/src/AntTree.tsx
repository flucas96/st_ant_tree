import React, { useEffect, useState } from "react";
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,

} from "streamlit-component-lib";


import { TreeSelect } from 'antd';
import parse, {Element } from 'html-react-parser';

interface TreeNode {
  title: string | JSX.Element;
  key: string;
  disabled?: boolean;
  children?: TreeNode[];
  style?: React.CSSProperties; // Optional style object for custom styling
}

//parser to parse the html from the strings in treeData
const parser = (input: string) =>
  parse(input, {
    replace: domNode => {
      if (domNode instanceof Element && domNode.attribs.class === 'remove') {
        return <></>;
      }
    }
  });


//function that takes the id of an element an return its aria controls -> Used to track wether the dropdown is open or not
function getAriaControls(id: string) {
  //check if the element hast the attribute aria-expanded

  if (document.getElementById(id)?.getAttribute("aria-expanded") == null) {
    return "first_time";
  }
  else {
  return document.getElementById(id)?.getAttribute("aria-expanded");
  }

}

function find_dropdown() {
//function to get the height of the dropdown

  var dropdown = Array.from(document.getElementsByClassName("ant-select-dropdown"));

  var height_of_dropdown = 0;
  dropdown.forEach((element) => {
  var height = (element as HTMLElement).offsetHeight;

    //if height is an integer return it
    if (height) {
      //test integer
      if (height % 1 === 0) {
        height_of_dropdown = height;
      }
    }
  });

  height_of_dropdown = height_of_dropdown + 100;

  return height_of_dropdown;
  }


////Tree Component////
const TreeComponent = (props: ComponentProps) => {
  const [value, setValue] = useState<string | undefined>(undefined);
  const [searchValue, setSearchValue] = useState('');


  const {
    treeData, allowClear, bordered, max_height, width_dropdown, disabled,
     multiple, placeholder, status, showArrow, showSearch,
    treeCheckable, treeDefaultExpandAll, treeDefaultExpandedKeys, treeLine,
    on_change, on_select, on_search, defaultValue, min_height_dropdown,
    maxTagCount, key, treeDefaultSelectedKeys, only_children_select, overall_css
  } = props.args;
  
  useEffect(() => {
    Streamlit.setFrameHeight();
  }, []);


  const filterTreeNode = (inputValue: string, treeNode: unknown): boolean => {
    const node = treeNode as { title: string; value: string; children?: any[] };
    const searchString = inputValue.toLowerCase();
    return node.title.toLowerCase().includes(searchString) ||
           node.value.toLowerCase().includes(searchString);
  };
  


  //Everything the the dropdown visibility changes the height of the component must change as well
  const onDropdownVisibleChange = () => {

    setTimeout(function() {
      var current_state = getAriaControls(key)
      var height = find_dropdown() 
    //if height is 0 set it to 50 
    var set_height = 0;
    if (height < min_height_dropdown) {
      set_height = min_height_dropdown;
    }
    else {
      set_height = height;
    }
    if (current_state == "true") {
      Streamlit.setFrameHeight(set_height);
    }
    else {
      Streamlit.setFrameHeight();
     // Streamlit.setFrameHeight(min_height_dropdown);
    }
    }, 1);
  };


  // if (on_change) {
  //   var on_change_func = Function(on_change);
  // }
  // else {
  //   var on_change_func = Function();
  // }

  if (on_select) {
    var on_select_func = Function(on_select);
  }
  else {
    var on_select_func = Function();
  }

  if (on_search) {
    var on_search_func = Function(on_search);
  }
  else {
    var on_search_func = Function();
  }

  if (defaultValue) {
    var defaultValue_tree = defaultValue;
  }
  else {
    var defaultValue_tree = undefined;
  }

  
  const onChange = (newValue: string) => {
    setValue(newValue);
    const valueToSend = newValue === undefined ? null : newValue;
    Streamlit.setComponentValue(valueToSend);
   // on_change_func();
  };

  const onSelect = () => {
    on_select_func();
  };

  const onSearch = () => {
    on_search_func();
  };


  function onTreeExpand_func() {
    //wait one seconds than execute find_dropdown
    //timeout Function weil HTML Keys nicht schnell genug geupdatet werden..
    setTimeout(function() {
      var height = find_dropdown()

      var set_height = 0;

      if (height == 0) {
        set_height = min_height_dropdown;
      }
      else {
        set_height = height;
      }
      Streamlit.setFrameHeight(set_height);
    }, 1);

  }

  //function to loop through treeData and parse the html if necessary
//   function loop_through_treeData(treeData: any) {
//     treeData.forEach((element: any) => {
//       //if element.title is a string
//       if (element.title && typeof element.title === "string")
//       {
//         element.title = parser(element.title)
//       }

//       //detect how many children the element has if those have children too without looping through them all 
//       if (element.children) {
//         //if the element has children loop through them
//         loop_through_treeData(element.children)
//       }
//     });

//   }
// loop_through_treeData(treeData)

 // Function to loop through treeData and modify it as necessary
// Function to loop through treeData and modify it as necessary
// Parser to ensure the output is either a string or a single JSX Element

loop_through_treeData(treeData)

function loop_through_treeData(treeData: any) {
  treeData.forEach((element: any) => {
    //if element.title is a string
    if (element.title && typeof element.title === "string")
    {
      element.title = parser(element.title)
    }

    //detect how many children the element has if those have children too without looping through them all 
    if (element.children) {
      //if the element has children loop through them
      if (only_children_select) {
        element.disabled = true;
      }
      loop_through_treeData(element.children)
    }
  });

}




  return (
    <div>
    <style dangerouslySetInnerHTML={{ __html: overall_css }} />
    <TreeSelect
      id  = {key}
      showSearch = {showSearch}
      showArrow = {showArrow}
     // filterTreeNode = {filterTreeNode}
      multiple = {multiple}
      disabled = {disabled}
      treeCheckable = {treeCheckable}
      treeLine = {treeLine}
      status= {status}
      treeDefaultExpandedKeys = {treeDefaultExpandedKeys}
      placement = "bottomLeft"
      style={{ width: width_dropdown, marginTop: "10px" }}
      onSearch={onSearch}
      onSelect={onSelect}
      defaultValue={defaultValue_tree}
      value={value}
      dropdownStyle={{ maxHeight: max_height, overflow: 'auto', width: width_dropdown }}
      dropdownAlign = {{offset: [0, 0]}}
      placeholder= {placeholder}
      allowClear = {allowClear}
      treeDefaultExpandAll = {treeDefaultExpandAll}
      onChange={onChange}
      treeData={treeData}
      onDropdownVisibleChange={onDropdownVisibleChange}
      onTreeExpand = {onTreeExpand_func}
      maxTagCount = {maxTagCount}
      onClear = {() => {Streamlit.setComponentValue(undefined)}}

      //on clear
      bordered = {bordered}

      
    />
    </div>
  );
  
};



export default withStreamlitConnection(TreeComponent);
