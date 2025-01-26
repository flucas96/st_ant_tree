# Streamlit ANT Tree Select Component

The **Streamlit ANT Tree Select Component** adds a hierarchical dropdown selector to Streamlit, based on [Ant Design Tree Select](https://ant.design/components/tree-select/). It supports nested selections, multiple selection, and search functionality.

---

## Installation

Install with pip:

```bash
pip install st-ant-tree
```

---

## Usage

The component is initialized by calling `st_ant_tree`. It returns a list of selected values.

```python
from st_ant_tree import st_ant_tree

# Define tree data
tree_data = [
    {
        "value": "parent_1",
        "title": "Parent 1",
        "children": [
            {"value": "child_1", "title": "Child 1"},
            {"value": "child_2", "title": "Child 2"},
        ],
    },
    {"value": "parent_2", "title": "Parent 2"},
]

# Use the component
selected_values = st_ant_tree(
    treeData=tree_data,
    treeCheckable=True,
    allowClear=True
)

st.write(f"Selected values: {selected_values}")
```

---

## Tree Data Structure

The tree data should be a list of dictionaries, where each dictionary represents a tree node. Keys include:

- `value` (required): The value returned when the node is selected.
- `title` (required): The label shown in the dropdown (can include HTML).
- `children` (optional): A list of child nodes (nested structure).
- `disabled` (optional): Disables the node.

---

### Default Selection

To set a default selection, use the `defaultValue` parameter with a list of node values.

```python
# Define tree data
tree_data = [
    {
        "value": "parent_1",
        "title": "Parent 1",
        "children": [
            {"value": "child_1", "title": "Child 1"},
            {"value": "child_2", "title": "Child 2"},
        ],
    },
    {"value": "parent_2", "title": "Parent 2"},
]

# Set default selection
selected_values = st_ant_tree(
    treeData=tree_data,
    defaultValue=["child_1"],  # List of default selected values
    treeCheckable=True
)
```

---

## Parameters

Key parameters and their purpose:

- `treeData` (list): The hierarchical data for the dropdown.
- `defaultValue` (list): Preselected values.
- `allowClear` (bool): Enables clearing selected values.
- `treeCheckable` (bool): Adds checkboxes for multi-select.
- `showSearch` (bool): Enables search functionality.
- `max_height` (int): Maximum height of the dropdown.
- `width_dropdown` (str): Width of the dropdown (e.g., `"90%"`).
- `placeholder` (str): Placeholder text for the selector.
- `treeLine` (bool): Displays lines connecting tree nodes.

---

### Example: Searchable Dropdown

```python
# Define tree data
tree_data = [
    {
        "value": "parent_1",
        "title": "Parent 1",
        "children": [
            {"value": "child_1", "title": "Child 1"},
            {"value": "child_2", "title": "Child 2"},
        ],
    },
    {"value": "parent_2", "title": "Parent 2"},
]

# Create a searchable dropdown
selected_values = st_ant_tree(
    treeData=tree_data,
    showSearch=True,
    placeholder="Search and select",
    treeCheckable=True
)

st.write(f"Selected values: {selected_values}")
```

---

## Features

- **Nested Selections**: Supports parent-child relationships in dropdowns.
- **Multiple Selection**: Enable with `treeCheckable=True`.
- **Search**: Matches input with both `value` and `title` of nodes.
- **Custom Styling**: Use HTML in `title` or modify dropdown dimensions.

