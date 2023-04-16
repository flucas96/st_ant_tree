import streamlit.components.v1 as components
import os

_RELEASE = True


if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "st_ant_tree",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3000",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_ant_tree", path=build_dir)

def st_ant_tree(treeData:list = [], allowClear:bool = True, bordered:bool = True, max_height:int = 400, width_dropdown: str = "90%", disabled:bool = False, 
    	dropdownStyle: str = "{}", style: str = "{}",filterTreeNode: bool = True, multiple: bool = False, placeholder: str = "Choose an option",
        showArrow: bool = True, showSearch: bool = True, treeCheckable: bool = True, treeDefaultExpandAll: bool = False,
        treeDefaultExpandedKeys: list = [], treeLine: bool = True, onChange: str = "", onSelect: str = "", onSearch: str = "", defaultValue = None, onTreeExpand: str = "", onTreeLoad:str = "", min_height_dropdown: int = 100,
        maxTagCount:int= False,status: str=None, key = "first_tree") -> int:
    """

    Parameters
    ----------
    treeData : list of dict (default = [])
        The data of the tree. The data should be in the form of a list of dictionaries.
    allowClear : bool (default = True)
        Whether allow clear.
    bordered : bool (default = True)
        Whether show border.
    max_height : int (default = 400)
        The max height of the dropdown.
    width_dropdown : int (default = "100%")
        The width of the dropdown.
    disabled : bool (default = False)
        Whether the dropdown is disabled.
    dropdownStyle : str (default = "{}")
        The style of the dropdown.
    style : str (default = "{}")
        The style of the whole selector.
    filterTreeNode : bool (default = True)
        Whether filter tree node.
    multiple : bool (default = False)  
        Whether allow multiple selection. --> Immer True wenn checkable = True
    placeholder : str (default = "Choose an option")
        The placeholder of the dropdown.
    showArrow : bool (default = True)
        Whether show arrow.
    showSearch : bool (default = True)
        Whether show search.
    treeCheckable : bool (default = True)
        Whether tree node can be checked.
    treeDefaultExpandAll : bool (default = False)
        Whether default expand all tree nodes.
    treeDefaultExpandedKeys : list (default = [])
        The keys of the default expanded tree nodes.
    treeLine : bool (default = True)
        Whether show tree node line.
    onChange : str (default = "")
        The callback function when the value of the dropdown changes. - The function must be JavaScript e.g. console.log("Hello World")
    onSelect : str (default = "")
        The callback function when a tree node is selected. - The function must be JavaScript e.g. console.log("Hello World")
    onSearch : str (default = "")
        The callback function when the search input changes.- The function must be JavaScript e.g. console.log("Hello World")
    defaultValue : str (default = None)
        The default value of the dropdown.
    onTreeExpand : str (default = "")
        The callback function when a tree node is expanded.
    onTreeLoad : str (default = "")
        The callback function when a tree node is loaded.
    min_height_dropdown : int (default = 100)
        The min height of the dropdown.
    status : str (default = None)
        The status of the dropdown. 'error'  'warning'
    key : str (default = "first_tree")
        The key of the dropdown.

    Returns
    -------
    The selected options as a list of strings.

    """
    #  dropdownStyle={{ maxHeight: max_height, overflow: 'auto', width: width_dropdown }}

    #        style={{ width: width_dropdown, marginTop: "10px" }}



    component_value = _component_func(treeData = treeData, allowClear = allowClear, bordered = bordered, max_height = max_height, width_dropdown = width_dropdown, disabled = disabled,
        dropdownStyle = dropdownStyle, style  = style, filterTreeNode = filterTreeNode, multiple = multiple, placeholder = placeholder,
        showArrow = showArrow, showSearch = showSearch, treeCheckable = treeCheckable, treeDefaultExpandAll = treeDefaultExpandAll,
        treeDefaultExpandedKeys = treeDefaultExpandedKeys, treeLine = treeLine, on_change = onChange, on_celect = onSelect, on_search = onSearch, default= defaultValue, defaultValue = defaultValue, min_height_dropdown = min_height_dropdown, onTreeExpand = onTreeExpand,
        onTreeLoad = onTreeLoad, maxTagCount = maxTagCount,status=status,key = key)

    return component_value
