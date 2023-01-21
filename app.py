import streamlit  as st

from st_ant_tree import st_ant_tree


st.set_page_config(layout="wide")


with st.sidebar:

  st.write("Options")

  placeholder = st.text_input("Placeholder Text","Choose an option")


  with st.expander("Behavior", expanded=True):
    allow_clear = st.checkbox("Allow Clear",value=True)

    tree_checkable = st.checkbox("Tree Checkable",value=True)
    if tree_checkable == True:
      multiple = st.checkbox("Multiple Values",value=True,disabled=True)
      st.caption("Multiple Values are always active when checkboxes are active")
    else:
      multiple = st.checkbox("Multiple Values",value=True,disabled=False)

    filter_treenode = st.checkbox("Filter Tree Node",value=True)
    tree_default_expand_all = st.checkbox("Tree Default Expand All",value=False)

    maxtagcount = st.slider("Max Tag Count",min_value=0,max_value=10,value=5,step=1)

    disabled = st.selectbox("Disabled",[True,False],index=1)



  with st.expander("Styling",expanded=True):
    border = st.checkbox("Border",value=True)

    maxheight = st.slider("Max Height",min_value=100,max_value=1000,value=400,step=10)
    widthdrop= st.slider("Width Dropdown (in %)",min_value=10,max_value=100,value=90,step=10)

    show_arrow = st.checkbox("Show Arrow",value=True)
    show_search = st.checkbox("Show Search",value=True)
    treeline= st.checkbox("Tree Line",value=True)

    status = st.selectbox("Status",["","warning","error"],index=0)





st.title("Ant Design Tree Component for Streamlit")

st.caption("A Streamlit implementation of the Ant Design Tree Component (https://ant.design/components/tree-select/).")

tree_data = [
  {
    "value": "parent 1",
    "title": """Test <i>  <b style="color:green"> parent HTML</b><i> test""",
    "children": [
      {
        "value": "parent 1-0",
        "title": "parent 1-0",
        "children": [
          {
            "value": "leaf1",
            "title": "leaf1",
          },
          {
            "value": "leaf2",
            "title": "leaf2",
          },
        ],
      },
      {
        "value": "parent 1-1",
        "title": "parent 1-1",
        "children": [
          {
            "value": "leaf3",
            "title": """<i> <b style="color:green">leaf3</b> </i>""",
          },
        ],
      },
    ],
  },
]


value = st_ant_tree(treeData=tree_data, allowClear= allow_clear, bordered= border, max_height= maxheight, filterTreeNode= filter_treenode, multiple= multiple,
                    placeholder= placeholder, showArrow= show_arrow, showSearch= show_search, treeCheckable= tree_checkable,
width_dropdown= str(widthdrop) +"%", disabled= disabled, key="1", maxTagCount=maxtagcount,status=status)

st.write(value)


st.code('''
import streamlit  as st

from st_ant_tree import st_ant_tree

#Example Data with some html code
tree_data = [
  {
    "value": "parent 1",
    "title": """Test <i>  <b style="color:green"> parent HTML</b></i> test""",
    "children": [
      {
        "value": "parent 1-0",
        "title": "parent 1-0",
        "children": [
          {
            "value": "leaf1",
            "title": "leaf1",
          },
          {
            "value": "leaf2",
            "title": "leaf2",
          },
        ],
      },
      {
        "value": "parent 1-1",
        "title": "parent 1-1",
        "children": [
          {
            "value": "leaf3",
            "title": """<i> <b style="color:green">leaf3</b> </i>""",
          },
        ],
      },
    ],
  },
]
'''
+ 

f'''
value = st_ant_tree(treeData=tree_data, allowClear= {allow_clear}, bordered= {border}, max_height= {maxheight}, filterTreeNode= {filter_treenode}, 
multiple= {multiple}, placeholder= "{placeholder}", showArrow= {show_arrow}, showSearch= {show_search}, treeCheckable= {tree_checkable},
width_dropdown= "{str(widthdrop)}%", disabled= {disabled}, maxTagCount={maxtagcount})
''')