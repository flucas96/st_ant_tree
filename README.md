Streamlit ANT Tree Select Component

<a href="https://buymeacoffee.com/flucas" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/default-orange.png" alt="Buy Me A Coffee" height="41" width="174"></a>
===

This streamlit component adds ANT Tree Select to Streamlit

https://ant.design/components/tree-select/

#Installation

    pip install st-ant-tree

#Usage

The component gets initialized by calling 'st_ant_tree'. The Component returns a list of all selected values.

    selected_values = st_ant_tree(treeData,....)

## Define the the data for the dropdown. 

The data needs to be a list that contains a dictionary. 

Each data point needs atleast a 'value', which gets returned if it gets selected and a 'title' which will be shown in the selector

**Some examples:**

2 Options (parent 1 and parent 2) that are on the **same level**:

    tree_data = [
        {
        "value": "parent 1",
        "title": "Title 1",
        },
        {
        "value": "parent 2",
        "title": "Title 2",
        }
    ]

We can add children and create **nested** selection trees

    tree_data = [
        {
        "value": "parent 1",
        "title": "Parent 1",
        "children": 
            [
                {"value": "child 1",
                "title": "Child 1"},
                {"value": "child 2",
                "title": "Child 2"},
            ]
        },
        {
        "value": "parent 2",
        "title": "Parent 2",
        }
    ]


It is possible to add **HTML Styling** to the title

    tree_data = [
        {
        "value": "parent 1",
        "title": "Title 1",
        },
        {
        "value": "parent 2",
        "title": """<i> <b style="color:green">Parent 2</b> </i>""",
        }
    ]

## Options that change the behavior

**Allow the user the clear all selected options at once (enables the X on the right side in the search bar).**

    st_ant_tree(...,allowClear = True)




**Enable Checkboxes next to each option** (this also always enables multiple selection!)

    st_ant_tree(...,treeCheckable = True)


**Enable multiple selection (not needed if Checkboxes are enabled)**

    st_ant_tree(...,multiple = True)

**It is possible to decide that the tree nodes will be hidden when filtering** 

    st_ant_tree(...,filterTreeNode = True)

**Expand all Nodes by default**

    st_ant_tree(...treeDefaultExpandAll = True)

**Only expand specific keys**

    #Takes a list of Keys that should be expanded. - Currenly not working

    st_ant_tree(..., treeDefaultExpandedKeys=["key1","key2"])


**Maximum tag count that gets displayed in the search bar**

    st_ant_tree(...,maxTagCount = 5)

**The selector can be disabled**

    st_ant_tree(...,disabled = True)

**Show a Border**

    st_ant_tree(..., bordered = True)

**Define a maximum height (in px) that will not be exceeded**

    st_ant_tree(..., max_height = 500)

**Define the width of the dropdown (in %)**

    st_ant_tree(...,width_dropdown = "90%")

**Show a arrow in the search bar**

    st_ant_tree(...,showArrow = True)

**Show a search icon the search bar**

    st_ant_tree(...,showSearch = True)

**Show tree lines**

    st_ant_tree(...,treeLine = True)

**Set validation status**
    
    #"error" or "warning"

    st_ant_tree(...,status="error")

**Set the placeholder text in the selector**

    st_ant_tree(...,placeholder="Choose an option")









