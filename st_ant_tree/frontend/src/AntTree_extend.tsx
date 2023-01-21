import React, { useEffect, useState } from "react";
import {
  ComponentProps,
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib";

import { TreeSelect } from 'antd';


class TreeComponent extends StreamlitComponentBase {

  value: string | undefined = undefined;
  componentDidMount(): void {
    // After we're rendered for the first time, tell Streamlit that our height
    // has changed.
    Streamlit.setFrameHeight()
  }

  componentDidUpdate(): void {
    // After we're re-rendered, tell Streamlit that our height may have changed.
    Streamlit.setFrameHeight()
  }


  
  private setValue = (newValue: string) => {
    this.setState({ value: newValue });
    console.log(newValue)
    Streamlit.setComponentValue(newValue);
  };

  // private getValue = (): string | undefined => {
  //   return this.state.value;
  // };


  render = (): React.ReactNode => {
    const { args } = this.props;
    const { treeData, allowClear, bordered, max_height, width_dropdown, disabled,
      dropdownStyle, filterTreeNode, multiple, placeholder, placement,
      showArrow, showSearch, treeCheckable, treeDefaultExpandAll, treeDefaultExpandedKes,
      treeLine, on_change, on_select, on_search, defaultValue } = args;


    console.log(treeData)


    const onChange = (newValue: string) => {
      this.setValue(newValue);
      console.log(newValue)
      Streamlit.setComponentValue(newValue);
      on_change_func();
    };

    const onSelect = (newValue: string) => {
      on_select_func();
    };

    const onSearch = (newValue: string) => {
      on_search_func();
    };

    

    //parse tree data as json string

    //get current height

    var expanded = false;

    // const onDropdownVisibleChange = () => {

    //   if (expanded) {
    //     Streamlit.setFrameHeight();
    //     console.log("triggerd - not expanded")

    //   }
    //   else {
    //     Streamlit.setFrameHeight(max_height + 10);
    //     console.log("triggerd - expanded")
    //   }
    //   expanded = !expanded;
    // }

    if (on_change) {
      var on_change_func = Function(on_change);
    }
    else {
      var on_change_func = Function();
    }
    
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

    return (
      <TreeSelect

        treeData={treeData}
        allowClear={allowClear}
        bordered={bordered}
        disabled={disabled}
        dropdownStyle={{ maxHeight: max_height, overflow: 'auto', width: width_dropdown}}
        filterTreeNode={filterTreeNode}
        multiple={multiple}
        placeholder={placeholder}
        placement={placement}
        showArrow={showArrow}
        showSearch={showSearch}
        treeCheckable={treeCheckable}
        treeDefaultExpandAll={treeDefaultExpandAll}

        treeDefaultExpandedKeys={treeDefaultExpandedKes}
        treeLine={treeLine}
       // value={}
       value = {this.value}
        onChange={onChange}
        onSelect={onSelect}
        onSearch={onSearch}
        onDropdownVisibleChange={this.componentDidUpdate}
        defaultValue={defaultValue_tree}
      />
    );
  };



}
// const TreeComponent = (props: ComponentProps) => {
//   const [value, setValue] = useState<string | undefined>(undefined);


//   const {treeData, allowClear, bordered, max_height, width_dropdown, disabled,
//     dropdownStyle,filterTreeNode,multiple, placeholder, placement,
//     showArrow, showSearch, treeCheckable, treeDefaultExpandAll, treeDefaultExpandedKes,
//     treeLine, on_change, on_select, on_search, defaultValue} = props.args;


//   useEffect(() => {
//     Streamlit.setFrameHeight();
//   }, []);


//   const onChange = (newValue: string) => {
//     setValue(newValue);
//     console.log(newValue)
//     Streamlit.setComponentValue(newValue);
//     on_change_func();
//   };

//   const onSelect = (newValue: string) => {
//     on_select_func();
//   };

//   const onSearch = (newValue: string) => {
//     on_search_func();
//   };


//   //parse tree data as json string


//   //get current height


//   var expanded = false;

//   const onDropdownVisibleChange = () => {
//     if (expanded) {
//       Streamlit.setFrameHeight();
//       console.log("triggerd - not expanded")

//     }
//     else {
//       Streamlit.setFrameHeight(max_height + 10);
//       console.log("triggerd - expanded")
//     }
//     expanded = !expanded;
//   };

//   if (on_change) {
//     var on_change_func = Function(on_change);
//   }
//   else {
//     var on_change_func = Function();
//   }

//   if (on_select) {
//     var on_select_func = Function(on_select);
//   }
//   else {
//     var on_select_func = Function();
//   }

//   if (on_search) {
//     var on_search_func = Function(on_search);
//   }
//   else {
//     var on_search_func = Function();
//   }

//   if (defaultValue) {
//     var defaultValue_tree = defaultValue;
//   }
//   else {
//     var defaultValue_tree = undefined;
//   }

  
//   return (
//     <TreeSelect
//       showSearch = {showSearch}
//       showArrow = {showArrow}
//       filterTreeNode = {filterTreeNode}
//       multiple = {multiple}
//       disabled = {disabled}
//       treeCheckable = {treeCheckable}
//       treeLine = {treeLine}
//       treeDefaultExpandedKeys = {treeDefaultExpandedKes}
//       placement = {placement}
//       style={{ width: width_dropdown, marginTop: "10px" }}
//       onSearch={onSearch}
//       onSelect={onSelect}
//       defaultValue={defaultValue_tree}

//       value={value}
//       dropdownStyle={{ maxHeight: max_height, overflow: 'auto' }}
//       placeholder= {placeholder}
//       allowClear = {allowClear}
//       treeDefaultExpandAll = {treeDefaultExpandAll}
//       onChange={onChange}
//       treeData={treeData}
//       onDropdownVisibleChange={onDropdownVisibleChange}
//       onClear = {() => {Streamlit.setComponentValue(undefined)}}

//       //on clear
//       bordered = {bordered}


//     />
//   );
// };


export default withStreamlitConnection(TreeComponent);
