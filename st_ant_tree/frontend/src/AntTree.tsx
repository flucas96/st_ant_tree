import React, { useEffect, useRef, useState } from "react";
import {
  ComponentProps,
  Streamlit,
  withStreamlitConnection,
} from "streamlit-component-lib";

import { TreeSelect } from 'antd';
import type { SizeType } from 'antd/es/config-provider/SizeContext';
import parse, { Element } from 'html-react-parser';

// Parse HTML strings in tree node titles
const parser = (input: string) =>
  parse(input, {
    replace: domNode => {
      if (domNode instanceof Element && domNode.attribs.class === 'remove') {
        return <></>;
      }
    }
  });

// Check if dropdown is open via aria-expanded attribute
function getAriaControls(id: string) {
  if (document.getElementById(id)?.getAttribute("aria-expanded") == null) {
    return "first_time";
  }
  return document.getElementById(id)?.getAttribute("aria-expanded");
}

// Calculate current dropdown height from DOM
function find_dropdown() {
  var dropdown = Array.from(document.getElementsByClassName("ant-select-dropdown"));
  var height_of_dropdown = 0;

  dropdown.forEach((element) => {
    // Use scrollHeight to get full content height, not just visible (fixes #13)
    var height = Math.max(
      (element as HTMLElement).offsetHeight,
      (element as HTMLElement).scrollHeight
    );
    if (height && height % 1 === 0) {
      height_of_dropdown = height;
    }
  });

  return height_of_dropdown + 100;
}

// Recursively process treeData: parse HTML titles, optionally disable parents
function loop_through_treeData(treeData: any, only_children_select: boolean) {
  treeData.forEach((element: any) => {
    if (element.title && typeof element.title === "string") {
      element.title = parser(element.title);
    }
    if (element.children) {
      if (only_children_select) {
        element.disabled = true;
      }
      loop_through_treeData(element.children, only_children_select);
    }
  });
}

// Collect all leaf node values (for defaultCheckedAll)
function collectAllLeafValues(treeData: any[]): string[] {
  const values: string[] = [];
  function walk(nodes: any[]) {
    for (const node of nodes) {
      if (node.children && node.children.length > 0) {
        walk(node.children);
      } else {
        values.push(node.value);
      }
    }
  }
  walk(treeData);
  return values;
}

const TreeComponent = (props: ComponentProps) => {
  const [value, setValue] = useState<any>(undefined);
  const [searchValue, setSearchValue] = useState('');
  const initializedRef = useRef(false);

  const {
    treeData, allowClear, bordered, max_height, width_dropdown, disabled,
    multiple, placeholder, status, showArrow, showSearch,
    treeCheckable, treeDefaultExpandAll, treeDefaultExpandedKeys, treeLine,
    defaultValue, min_height_dropdown,
    maxTagCount, key, only_children_select, overall_css,
    size, defaultCheckedAll, filterTreeNode: filterEnabled,
  } = props.args;

  // Fix #7: Sync controlled value when defaultValue prop changes
  useEffect(() => {
    if (defaultValue !== undefined && defaultValue !== null) {
      setValue(defaultValue);
      Streamlit.setComponentValue(defaultValue);
    }
  }, [JSON.stringify(defaultValue)]);

  // Fix #3: Check all leaf nodes on first load when defaultCheckedAll is true
  useEffect(() => {
    if (defaultCheckedAll && !initializedRef.current && treeData?.length > 0) {
      initializedRef.current = true;
      const allLeaves = collectAllLeafValues(treeData);
      setValue(allLeaves);
      Streamlit.setComponentValue(allLeaves);
    }
  }, [defaultCheckedAll, treeData]);

  // Fix #12: Recalculate frame height when component becomes visible (e.g. in tabs)
  useEffect(() => {
    Streamlit.setFrameHeight();

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          Streamlit.setFrameHeight();
        }
      });
    });

    const root = document.getElementById('root');
    if (root) observer.observe(root);
    return () => observer.disconnect();
  }, []);

  // Fix #5: Filter by title (string-safe, handles numeric values and HTML-parsed titles)
  const filterTreeNode = (inputValue: string, treeNode: unknown): boolean => {
    const node = treeNode as { title: any; value: any; children?: any[] };
    const searchString = inputValue.toLowerCase();
    const titleStr = typeof node.title === 'string' ? node.title : String(node.value);
    const valueStr = String(node.value);
    return titleStr.toLowerCase().includes(searchString) ||
           valueStr.toLowerCase().includes(searchString);
  };

  // Dropdown open/close handler — adjusts iframe height
  const onDropdownVisibleChange = () => {
    setTimeout(function() {
      var current_state = getAriaControls(key);
      var height = find_dropdown();
      var set_height = Math.max(height, min_height_dropdown);

      if (current_state === "true") {
        Streamlit.setFrameHeight(set_height);
      } else {
        Streamlit.setFrameHeight();
      }
    }, 1);
  };

  // Fix #10: onChange properly sends null when value is cleared
  const onChange = (newValue: any) => {
    setValue(newValue);
    Streamlit.setComponentValue(newValue === undefined ? null : newValue);
  };

  const onSearch = (val: string) => {
    setSearchValue(val);
  };

  function onTreeExpand_func() {
    setTimeout(function() {
      var height = find_dropdown();
      var set_height = Math.max(height, min_height_dropdown);
      Streamlit.setFrameHeight(set_height);
    }, 1);
  }

  // Process tree data (parse HTML, handle only_children_select)
  loop_through_treeData(treeData, only_children_select);

  // Fix #2: Default CSS to prevent border disappearing on re-focus
  const defaultCss = `
    .ant-select-selector {
      border: 1px solid #d9d9d9 !important;
      transition: border-color 0.3s;
    }
    .ant-select-focused .ant-select-selector {
      border-color: #4096ff !important;
      box-shadow: 0 0 0 2px rgba(5, 145, 255, 0.1) !important;
    }
  `;

  return (
    <div>
      <style dangerouslySetInnerHTML={{ __html: defaultCss + (overall_css || '') }} />
      <TreeSelect
        id={key}
        showSearch={showSearch}
        showArrow={showArrow}
        multiple={multiple}
        disabled={disabled}
        treeCheckable={treeCheckable}
        treeLine={treeLine}
        status={status}
        size={size as SizeType}
        treeDefaultExpandedKeys={treeDefaultExpandedKeys}
        placement="bottomLeft"
        style={{ width: width_dropdown, marginTop: "10px", position: "relative", zIndex: 1000 }}
        onSearch={onSearch}
        value={value}
        dropdownStyle={{ maxHeight: max_height, overflow: 'auto', width: width_dropdown }}
        dropdownAlign={{ offset: [0, 0] }}
        placeholder={placeholder}
        allowClear={allowClear}
        treeDefaultExpandAll={treeDefaultExpandAll}
        onChange={onChange}
        treeData={treeData}
        onDropdownVisibleChange={onDropdownVisibleChange}
        onTreeExpand={onTreeExpand_func}
        maxTagCount={maxTagCount}
        filterTreeNode={filterEnabled ? filterTreeNode : undefined}
        onClear={() => {
          // Fix #10: Send null (not undefined) so Python receives None
          setValue(undefined);
          Streamlit.setComponentValue(null);
          setSearchValue('');
        }}
        searchValue={searchValue}
        bordered={bordered}
      />
    </div>
  );
};

export default withStreamlitConnection(TreeComponent);
