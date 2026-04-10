from __future__ import annotations

import streamlit.components.v1 as components
import os

_RELEASE = True


if not _RELEASE:
    _component_func = components.declare_component(
        "st_ant_tree",
        url="http://localhost:3000",
    )
else:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("st_ant_tree", path=build_dir)

def st_ant_tree(
    treeData: list = [],
    allowClear: bool = True,
    bordered: bool = True,
    max_height: int = 400,
    width_dropdown: str = "90%",
    disabled: bool = False,
    dropdownStyle: str = "{}",
    style: str = "{}",
    filterTreeNode: bool = True,
    multiple: bool = False,
    placeholder: str = "Choose an option",
    showArrow: bool = True,
    showSearch: bool = True,
    treeCheckable: bool = True,
    treeDefaultExpandAll: bool = False,
    treeDefaultExpandedKeys: list = [],
    treeLine: bool = True,
    onChange: str = None,
    onSelect: str = "",
    onSearch: str = "",
    onTreeExpand: str = "",
    onTreeLoad: str = "",
    defaultValue=None,
    min_height_dropdown: int = 100,
    maxTagCount: int = False,
    status: str = None,
    key: str = "first_tree",
    only_children_select: bool = False,
    disable_disabled_style: bool = False,
    overall_css: str = "",
    size: str = None,
    defaultCheckedAll: bool = False,
) -> list | None:
    """Streamlit component wrapping Ant Design TreeSelect.

    Parameters
    ----------
    treeData : list of dict (default = [])
        The data of the tree. Each dict should have 'value', 'title', and
        optionally 'children' (list) and 'disabled' (bool).
    allowClear : bool (default = True)
        Whether to show a clear button.
    bordered : bool (default = True)
        Whether to show border.
    max_height : int (default = 400)
        The max height of the dropdown in pixels.
    width_dropdown : str (default = "90%")
        The CSS width of the dropdown.
    disabled : bool (default = False)
        Whether the dropdown is disabled.
    dropdownStyle : str (default = "{}")
        The style of the dropdown.
    style : str (default = "{}")
        The style of the whole selector.
    filterTreeNode : bool (default = True)
        Whether to enable search filtering on tree nodes.
    multiple : bool (default = False)
        Whether to allow multiple selection.
    placeholder : str (default = "Choose an option")
        The placeholder text.
    showArrow : bool (default = True)
        Whether to show the arrow icon.
    showSearch : bool (default = True)
        Whether to show the search input.
    treeCheckable : bool (default = True)
        Whether tree nodes can be checked with checkboxes.
    treeDefaultExpandAll : bool (default = False)
        Whether to expand all tree nodes by default.
    treeDefaultExpandedKeys : list (default = [])
        The keys of the default expanded tree nodes.
    treeLine : bool (default = True)
        Whether to show tree node connecting lines.
    defaultValue : list or str (default = None)
        The default selected value(s).
    min_height_dropdown : int (default = 100)
        The minimum height of the dropdown in pixels.
    maxTagCount : int (default = False)
        Maximum number of tags to display.
    status : str (default = None)
        Validation status: 'error' or 'warning'.
    key : str (default = "first_tree")
        The unique key for the component instance.
    only_children_select : bool (default = False)
        If True, only leaf nodes can be selected (parents are disabled).
    disable_disabled_style : bool (default = False)
        Whether to disable the disabled styling.
    overall_css : str (default = "")
        Additional CSS to inject into the component.
    size : str (default = None)
        Size of the select input: 'large', 'middle', or 'small'.
    defaultCheckedAll : bool (default = False)
        If True, all leaf nodes are checked on initial load.

    Returns
    -------
    list or None
        The selected values as a list, or None if nothing is selected.
    """
    component_value = _component_func(
        treeData=treeData,
        allowClear=allowClear,
        bordered=bordered,
        max_height=max_height,
        width_dropdown=width_dropdown,
        disabled=disabled,
        dropdownStyle=dropdownStyle,
        style=style,
        filterTreeNode=filterTreeNode,
        multiple=multiple,
        placeholder=placeholder,
        showArrow=showArrow,
        showSearch=showSearch,
        treeCheckable=treeCheckable,
        treeDefaultExpandAll=treeDefaultExpandAll,
        treeDefaultExpandedKeys=treeDefaultExpandedKeys,
        treeLine=treeLine,
        defaultValue=defaultValue,
        min_height_dropdown=min_height_dropdown,
        maxTagCount=maxTagCount,
        status=status,
        key=key,
        only_children_select=only_children_select,
        disable_disabled_style=disable_disabled_style,
        overall_css=overall_css,
        size=size,
        defaultCheckedAll=defaultCheckedAll,
    )

    return component_value
