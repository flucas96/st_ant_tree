"""Test app to verify all issue fixes for st_ant_tree."""
import streamlit as st
from st_ant_tree import st_ant_tree

st.set_page_config(layout="wide")
st.title("st_ant_tree — Issue Reproduction & Fix Verification")

tree_data = [
    {
        "value": "parent 1",
        "title": """Test <i><b style="color:green">parent HTML</b></i> test""",
        "children": [
            {
                "value": "parent 1-0",
                "title": "parent 1-0",
                "children": [
                    {"value": "leaf1", "title": "leaf1"},
                    {"value": "leaf2", "title": "leaf2"},
                ],
            },
            {
                "value": "parent 1-1",
                "title": "parent 1-1",
                "children": [
                    {"value": "leaf3", "title": """<i><b style="color:green">leaf3</b></i>"""},
                ],
            },
        ],
    },
    {"value": "parent 2", "title": "Parent 2"},
]

# Large tree for height testing (#13)
large_tree = [
    {
        "value": f"parent_{i}",
        "title": f"Parent {i}",
        "children": [
            {"value": f"child_{i}_{j}", "title": f"Child {i}-{j}"}
            for j in range(20)
        ],
    }
    for i in range(5)
]

# Numeric value tree for filter testing (#5)
numeric_tree = [
    {
        "value": 1,
        "title": "Searchable Parent",
        "children": [
            {"value": 2, "title": "Alpha Child"},
            {"value": 3, "title": "Beta Child"},
            {"value": 4, "title": "Gamma Child"},
        ],
    },
]

st.markdown("---")

# ── Issue #10: allowClear returns stale value ──
st.header("#10 — allowClear should return None when cleared")
st.caption("Select an item, then clear it. The return value should become None.")
result_10 = st_ant_tree(
    tree_data,
    allowClear=True,
    treeCheckable=False,
    multiple=False,
    placeholder="Select then clear me",
    key="issue_10",
)
st.write(f"Return value: `{result_10}` (type: `{type(result_10).__name__}`)")
if result_10 is None:
    st.success("Correctly returned None")
else:
    st.info(f"Selected: {result_10}")

st.markdown("---")

# ── Issue #7: defaultValue not reactive ──
st.header("#7 — defaultValue should update when changed")
st.caption("Change the selectbox — the tree should reflect the new default immediately.")
preselected = st.selectbox("Preselect", [None, "leaf1", "leaf2", "leaf3"])
result_7 = st_ant_tree(
    tree_data,
    placeholder="Should update with selectbox",
    defaultValue=[preselected] if preselected else None,
    key="issue_7",
)
st.write(f"Return value: `{result_7}`")

st.markdown("---")

# ── Issue #12: Rendering in tabs ──
st.header("#12 — Should render correctly in tabs")
tab1, tab2 = st.tabs(["Tab 1", "Tab 2"])
with tab1:
    st.write("Switch to Tab 2 and back — the tree should appear correctly.")
with tab2:
    result_12 = st_ant_tree(
        tree_data,
        placeholder="I should render in Tab 2",
        key="issue_12",
    )
    st.write(f"Return value: `{result_12}`")

st.markdown("---")

# ── Issue #13: Height not enough ──
st.header("#13 — Large tree should be scrollable")
st.caption("Expand parents — all children should be visible via scrolling.")
result_13 = st_ant_tree(
    large_tree,
    treeDefaultExpandAll=True,
    max_height=500,
    min_height_dropdown=300,
    placeholder="Large tree with many children",
    key="issue_13",
)
st.write(f"Return value: `{result_13}`")

st.markdown("---")

# ── Issue #5: Filter by title with numeric values ──
st.header("#5 — Search should work with numeric values")
st.caption("Type 'Alpha' or 'Beta' — should filter by title even though values are numbers.")
result_5 = st_ant_tree(
    numeric_tree,
    showSearch=True,
    filterTreeNode=True,
    placeholder="Search by title (values are numbers)",
    key="issue_5",
)
st.write(f"Return value: `{result_5}`")

st.markdown("---")

# ── Issue #6: Size parameter ──
st.header("#6 — Size parameter")
col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Small")
    st_ant_tree(tree_data, size="small", placeholder="Small", key="size_small")
with col2:
    st.subheader("Middle (default)")
    st_ant_tree(tree_data, size="middle", placeholder="Middle", key="size_middle")
with col3:
    st.subheader("Large")
    st_ant_tree(tree_data, size="large", placeholder="Large", key="size_large")

st.markdown("---")

# ── Issue #3: Check all by default ──
st.header("#3 — defaultCheckedAll")
st.caption("All leaf nodes should be pre-checked on load.")
result_3 = st_ant_tree(
    tree_data,
    treeCheckable=True,
    defaultCheckedAll=True,
    placeholder="All should be checked",
    key="issue_3",
)
st.write(f"Return value: `{result_3}`")

st.markdown("---")

# ── Issue #2: Border disappears on reselect ──
st.header("#2 — Border should persist on re-focus")
st.caption("Select an item, click elsewhere, then re-click the component. Border should remain.")
result_2 = st_ant_tree(
    tree_data,
    allowClear=True,
    treeCheckable=False,
    bordered=True,
    treeDefaultExpandAll=True,
    treeLine=True,
    placeholder="Click, select, click away, re-click",
    key="issue_2",
)
st.write(f"Return value: `{result_2}`")

st.markdown("---")

# ── Issue #4: Return type ──
st.header("#4 — Return type should be list | None, not int")
st.caption("Check the function signature and this return value type.")
result_4 = st_ant_tree(tree_data, key="issue_4", placeholder="Check return type")
st.write(f"Return value: `{result_4}`, type: `{type(result_4).__name__}`")
st.code("def st_ant_tree(...) -> list | None:  # Fixed from -> int")
