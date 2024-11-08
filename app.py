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


  with st.expander("'on' Fuctions",expanded=True):
    on_change = st.text_area("on_change","""console.log("Value chagned")""")





st.title("Ant Design Tree Component for Streamlit")

st.caption("A Streamlit implementation of the Ant Design Tree Component (https://ant.design/components/tree-select/).")

selectbox = st.radio("Select Example Data", ["Example 1", "Example 2"], index=0)

if selectbox == "Example 1":
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
            "value": "value1",
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
else:


  tree_data = [{'value': 1, 'title': '<b>Albert Bauer GmbH Flensburg</b>'}, {'value': 2, 'title': '<b>Albert Bauer GmbH Husum</b>'}, {'value': 3, 'title': '<b>Albert Bauer GmbH Schleswig</b>'}, {'value': 4, 'title': '<b>Albert Bauer GmbH Weddingstedt</b>'}, {'value': 5, 'title': '<b>AssenheimerMulfinger GmbH & Co. KG - AutoArenA</b>'}, {'value': 6, 'title': '<b>AssenheimerMulfinger GmbH & Co. KG - Autodienst Burkart</b>'}, {'value': 7, 'title': '<b>AssenheimerMulfinger GmbH & Co. KG - Eppingen</b>'}, {'value': 8, 'title': '<b>AssenheimerMulfinger GmbH & Co. KG - Gaildorf</b>'}, {'value': 9, 'title': '<b>AssenheimerMulfinger GmbH & Co. KG - Heilbronn</b>'}, {'value': 10, 'title': '<b>AssenheimerMulfinger GmbH & Co. KG - Obereisesheim</b>'}, {'value': 11, 'title': '<b>AssenheimerMulfinger GmbH & Co.  KG - Sinsheim</b>'}, {'value': 12, 'title': '<b>AssenheimerMulfinger GmbH & Co. KG - Öhringen</b>'}, {'value': 13, 'title': '<b>Audi Zentrum Karlsruhe GmbH</b>'}, {'value': 14, 'title': '<b>Auto Heusel GmbH & Co. KG</b>'}, {'value': 15, 'title': '<b>Auto Singer GmbH & Co. KG Buchloe</b>'}, {'value': 16, 'title': '<b>Auto Singer GmbH & Co. KG Marktoberdorf</b>'}, {'value': 17, 'title': '<b>Auto Weller GmbH & Co. KG Dortmund</b>'}, {'value': 18, 'title': '<b>Auto-Häuser GmbH & Co. KG</b>'}, {'value': 19, 'title': '<b>AutoCrew  Melzer (Autohaus Melzer e.K.)</b>'}, {'value': 20, 'title': '<b>Autohaus Eichhorn Mittenberg</b>'}, {'value': 21, 'title': '<b>Autohaus Eichhorn Obernburg</b>'}, {'value': 22, 'title': '<b>Autohaus Graf Hardenberg GmbH Karlsruhe</b>'}, {'value': 23, 'title': '<b>Autohaus H. Tietjen KG Buxtehude</b>'}, {'value': 24, 'title': '<b>Autohaus Hedtke GmbH & Co. KG</b>'}, {'value': 25, 'title': '<b>Autohaus Heermann und Rhein Bad Rappenau</b>'}, {'value': 26, 'title': '<b>Autohaus Heermann und Rhein Heilbronn</b>'}, {'value': 27, 'title': '<b>Autohaus Hofmann GmbH Abensberg</b>'}, {'value': 28, 'title': '<b>Autohaus Hofmann GmbH Ingolstadt</b>'}, {'value': 29, 'title': '<b>Autohaus Hofmann GmbH Neuburg an der Donau</b>'}, {'value': 30, 'title': '<b>Autohaus Hofmann GmbH Pfaffenhofen</b>'}, {'value': 31, 'title': '<b>Autohaus Hofmann GmbH Regensburg</b>'}, {'value': 32, 'title': '<b>Autohaus Kögel GmbH</b>'}, {'value': 33, 'title': '<b>Autohaus Melzer e.K. Chemnitz</b>'}, {'value': 34, 'title': '<b>Autohaus Melzer e.K. Limbach-Oberfrohna</b>'}, {'value': 35, 'title': '<b>Autohaus Rhein Bayreuth</b>'}, {'value': 36, 'title': '<b>Autohaus Rhein Bodensee</b>'}, {'value': 37, 'title': '<b>Autohaus Rhein Franken GmbH</b>'}, {'value': 38, 'title': '<b>Autohaus Rhein Hochfranken</b>'}, {'value': 39, 'title': '<b>Autohaus Rhein Kulmbach</b>'}, {'value': 40, 'title': '<b>Autohaus Rhein Ludwigsburg</b>'}, {'value': 41, 'title': '<b>Autohaus Rhein Rhön-Saale</b>'}, {'value': 42, 'title': '<b>Autohaus Rhein Rothenburg</b>'}, {'value': 43, 'title': '<b>Autohaus Rhein Schweinfurt</b>'}, {'value': 44, 'title': '<b>Autohaus Rhein Tauberfranken</b>'}, {'value': 45, 'title': '<b>Autohaus Tief-Dörfler</b>'}, {'value': 46, 'title': '<b>Autohaus Rhein Würzburg</b>'}, {'value': 47, 'title': '<b>Autohaus Rottmann GmbH</b>'}, {'value': 48, 'title': '<b>Autohaus Ruhe GmbH</b>'}, {'value': 49, 'title': '<b>Autohaus Seitz GmbH</b>'}, {'value': 50, 'title': '<b>Autohaus Stadel Bietigheim-Bissingen</b>'}, {'value': 51, 'title': '<b>Autohaus Stadel Eppingen</b>'}, {'value': 52, 'title': '<b>Autohaus Stadel Heilbronn</b>'}, {'value': 53, 'title': '<b>Autohaus Sternpark GmbH & Co. KG Gilching</b>'}, {'value': 54, 'title': '<b>Autohaus Sternpark GmbH & Co. KG Herrsching</b>'}, {'value': 55, 'title': '<b>Autohaus Sternpark GmbH & Co. KG Soest</b>'}, {'value': 56, 'title': '<b>Autohaus  Sternpark GmbH & Co. KG Werl</b>'}, {'value': 57, 'title': '<b>Autohaus Timmermanns GmbH Düsseldorf</b>'}, {'value': 58, 'title': '<b>Autohaus Timmermanns GmbH Kaarst</b>'}, {'value': 59, 'title': '<b>Autohaus Timmermanns GmbH Nettetal</b>'}, {'value': 60, 'title': '<b>Autohaus Timmermanns GmbH Neuss</b>'}, {'value': 61, 'title': '<b>Autohaus-Gramling Sportwagen GmbH</b>'}, {'value': 62, 'title': '<b>Automag GmbH LBS</b>'}, {'value': 63, 'title': '<b>Automag GmbH WLS</b>'}, {'value': 64, 'title': '<b>Avalon Premium Cars GmbH München</b>'}, {'value': 65, 'title': '<b>AVP Autoland GmbH & Co. KG | Altötting</b>'}, {'value': 66, 'title': '<b>AVP Autoland GmbH & Co. KG | AUDI Deggendorf & Großkunden</b>'}, {'value': 67, 'title': '<b>AVP Autoland GmbH & Co. KG | Burghausen</b>'}, {'value':  68, 'title': '<b>AVP Autoland GmbH & Co. KG | Dingolfing</b>'}, {'value': 69, 'title': '<b>AVP Autoland GmbH & Co. KG | Nora Leistungszentrum</b>'}, {'value': 70, 'title': '<b>AVP Autoland GmbH & Co. KG | OZA</b>'}, {'value': 71, 'title': '<b>AVP Autoland GmbH & Co. KG | Regen</b>'}, {'value': 72, 'title': '<b>AVP Autoland GmbH & Co. KG | Seat Cupra Plattling & Dingolfing</b>'}, {'value': 73, 'title': '<b>AVP Autoland GmbH & Co. KG | Skoda Plattling</b>'}, {'value': 74, 'title': '<b>AVP Autoland GmbH & Co. KG | Technikzentrum Plattling</b>'}, {'value': 75, 'title': '<b>AVP Autoland GmbH & Co. KG | VW Deggendorf & VW Nutzfahrzeuge</b>'}, {'value': 76, 'title': '<b>AVP Autoland GmbH & Co. KG | Zwiesel</b>'}, {'value': 77, 'title': '<b>AVP Automobilgruppe Beteiligungs GmbH | Beteiligung  & AVP E-Mobility</b>'}, {'value': 78, 'title': '<b>B&K Cloppenburg</b>'}, {'value': 79, 'title': '<b>B&K Hamburg</b>'}, {'value': 80, 'title': '<b>B&K GmbH Herford</b>'}, {'value': 81, 'title': '<b>B&K Winsen (Luhe)</b>'}, {'value': 82, 'title': '<b>BOB Automobile  GmbH Bochum</b>'}, {'value': 83, 'title': '<b>BOB Automobile GmbH Düsseldorf</b>'}, {'value': 84, 'title': '<b>BOB Automobile GmbH Hagen</b>'}, {'value': 85, 'title': '<b>BOB Automobile GmbH Herne</b>'}, {'value': 86, 'title': '<b>BOB Automobile GmbH Langemarckstraße Essen</b>'}, {'value': 87, 'title': '<b>BOB Automobile GmbH Leverkusen</b>'}, {'value': 88, 'title': '<b>BOB Automobile GmbH Ruhrtalstraße Essen</b>'}, {'value': 89, 'title': '<b>BOB Automobile GmbH Schultenhofstraße Mühlheim</b>'}, {'value': 90, 'title': '<b>BOB Automobile GmbH Witten</b>'}, {'value': 91, 'title': '<b>BOB Automobile GmbH Wolfsbankring Essen</b>'}, {'value': 92, 'title': '<b>BOB Automobile GmbH Wuppertal</b>'}, {'value': 93, 'title': '<b>BOB Automotive Group GmbH</b>'}, {'value': 94, 'title': '<b>E+G Autohandel GmbH & Co. Beteiligungs KG</b>'}, {'value': 95, 'title': '<b>EuroCar Landshut GmbH</b>'}, {'value': 96, 'title': '<b>G+G Autohandel GmbH & Co. KG</b>'}, {'value': 97, 'title': '<b>Gebrauchtwagenzentrum Ostbayern</b>'}, {'value': 98, 'title': '<b>Gohm + Graf  Hardenberg GmbH Aach</b>'}, {'value': 99, 'title': '<b>Gohm + Graf Hardenberg GmbH Konstanz</b>'}, {'value': 100, 'title': '<b>Gohm + Graf Hardenberg GmbH Radolfzell</b>'}, {'value': 101, 'title': '<b>Gohm + Graf Hardenberg GmbH Singen Hochwaldstraße</b>'}, {'value': 102, 'title': '<b>Gohm + Graf Hardenberg GmbH Singen Stockholzstraße</b>'}, {'value': 103, 'title': '<b>Gohm + Graf Hardenberg GmbH Überlingen</b>'}, {'value': 104, 'title': '<b>Graf Hardenberg GmbH & Co. KG Offenburg</b>'}, {'value': 105, 'title': '<b>Graf Hardenberg GmbH & Co. KG Tuttlingen</b>'}, {'value': 106, 'title': '<b>Graf Hardenberg GmbH Bruchsal</b>'}, {'value': 107, 'title': '<b>Graf Hardenberg GmbH Eggenstein</b>'}, {'value': 108, 'title': '<b>Graf Hardenberg GmbH Gengenbach</b>'}, {'value': 109, 'title': '<b>Graf Hardenberg GmbH Karlsruhe</b>'}, {'value': 110, 'title': '<b>Graf Hardenberg GmbH Lahr</b>'}, {'value': 111, 'title': '<b>Graf Hardenberg Karosserie & Lack Zentrum GmbH </b>'}, {'value': 112, 'title': '<b>Graf Hardenberg Sportwagen GmbH Freiburg</b>'}, {'value': 113, 'title': '<b>Graf Hardenberg Sportwagen GmbH Landau</b>'}, {'value': 114, 'title': '<b>Graf Hardenberg Sportwagen GmbH Offenburg</b>'}, {'value': 115, 'title': '<b>Hahn Sportwagen Göppingen GmbH</b>'}, {'value': 116, 'title': '<b>Hedtke Automobile GmbH</b>'}, {'value': 117, 'title': '<b>H&S Senden Karo- und Lackzentrum</b>'}, {'value': 118, 'title': '<b>Volkswagen Zentrum Ulm</b>'}, {'value': 119, 'title': '<b>Hofmann & Wittmann AG und IngoSoftware GmbH</b>'}, {'value': 120, 'title': '<b>Hüsser & Palkoska AG</b>'},  {'value': 121, 'title': '<b>Leseberg Automobile GmbH Ersatzteillager</b>'}, {'value': 122, 'title': '<b>Leseberg Automobile GmbH K&L Werkstatt</b>'}, {'value': 123, 'title': '<b>Leseberg Automobile GmbH LKW Werkstatt</b>'}, {'value': 124, 'title': '<b>Leseberg Automobile GmbH Mercedes-Benz Werkstatt</b>'}, {'value': 125, 'title': '<b>Leseberg Automobile GmbH VW & Skoda Werkstatt</b>'}, {'value': 126, 'title': '<b>Porsche Zentrum Altötting</b>'}, {'value': 127, 'title': '<b>Porsche Zentrum Inntal</b>'}, {'value': 128, 'title': '<b>Porsche Zentrum Landshut</b>'}, {'value': 129, 'title': '<b>Porsche Zentrum Plattling</b>'}, {'value': 130, 'title': '<b>Richard Gramling GmbH & Co. KG</b>'}, {'value': 131, 'title': '<b>Autohaus Scherer Alzey</b>'}, {'value': 132, 'title': '<b>Audi Zentrum Wiesbaden</b>'}, {'value': 133, 'title': '<b>Autohaus Scherer Homburg</b>'}, {'value': 134, 'title': '<b>Autohaus Scherer Ludwigshafen VW</b>'}, {'value': 135, 'title': '<b>Autohaus Scherer Mayen Seat/Skoda</b>'}, {'value': 136, 'title': '<b>Autohaus Scherer Mayen VW</b>'}, {'value': 137, 'title': '<b>Autohaus Scherer Neustadt</b>'}, {'value': 138, 'title': '<b>Porsche Zentrum Saarland</b>'}, {'value': 139, 'title': '<b>Schmidt Automobile GmbH</b>'}, {'value': 140, 'title': '<b>Schwaba Augsburg Süd</b>'}, {'value': 141, 'title': '<b>Schwaba Autocenter</b>'}, {'value': 142, 'title': '<b>Schweizer Lechhausen</b>'}, {'value': 143, 'title': '<b>TCB Automobile GmbH Bochum</b>'}, {'value': 144, 'title': '<b>TCB Automobile GmbH Essen</b>'}, {'value': 145, 'title': '<b>TCB Automobile GmbH Gelsenkirchen</b>'}, {'value': 146, 'title': '<b>TCB Automobile Gevelsberg, Haltern am See, Marl, Oberhausen, Mühlheim</b>'}, {'value': 147, 'title': '<b>TCB Automobile GmbH Kamen</b>'}, {'value': 148, 'title': '<b>TCB Automobile GmbH Recklinghausen</b>'}, {'value': 149, 'title': '<b>Drexl & Ziegler GmbH & Co. KG Augsburg</b>'}, {'value': 150, 'title': '<b>Drexl & Ziegler GmbH & Co. KG Günzburg</b>'}, {'value': 151, 'title': '<b>Drexl & Ziegler GmbH & Co. KG Neusäß</b>'}, {'value': 152, 'title': '<b>Feddersen Automobile GmbH Alfeld</b>'}, {'value': 153, 'title': '<b>Feddersen Automobile GmbH Bad Salzdetfurth</b>'}, {'value': 154, 'title': '<b>Feddersen Automobile Gmbh Gronau</b>'}, {'value': 155, 'title': '<b>Autohaus Eckloff GmbH</b>'}, {'value': 156, 'title': '<b>Hermann GmbH Einbeck</b>'}, {'value': 157, 'title': '<b>Hermann GmbH Goslar</b>'}, {'value': 158, 'title': '<b>Hermann GmbH Göttingen</b>'}, {'value': 159, 'title': '<b>Hermann GmbH Hildesheim</b>'}, {'value': 160, 'title': '<b>Hermann GmbH Höxter</b>'}, {'value': 161, 'title': '<b>Hermann GmbH Mühlhausen</b>'}, {'value': 162, 'title': '<b>Hermann GmbH Northeim</b>'}, {'value': 163, 'title': '<b>Royal Motors Kempen GmbH</b>'}, {'value': 164, 'title': '<b>Volkswagen Zentrum Karlsruhe GmbH</b>'}, {'value': 165, 'title': '<b>Volkswagen Automobile Rhein-Neckar GmbH Mannheim</b>'}, {'value': 166, 'title': '<b>Volkswagen Automobile Rhein-Neckar GmbH Weinheim</b>'}, {'value': 167, 'title': '<b>WWG Autowelt GmbH & Co. KG </b>'}]

default_value = ["parent 1"]

value = st_ant_tree(treeData=tree_data, allowClear= allow_clear, bordered= border, max_height= maxheight, filterTreeNode= filter_treenode, multiple= multiple,
                    placeholder= placeholder, showArrow= show_arrow, showSearch= show_search, treeCheckable= tree_checkable, 
width_dropdown= str(widthdrop) +"%", disabled= disabled, key="1", maxTagCount=maxtagcount,status=status,
only_children_select = True, 
#disable_disabled_style= False
)

st.write(value)


value = st_ant_tree(treeData=tree_data, allowClear= allow_clear, bordered= border, max_height= maxheight, filterTreeNode= filter_treenode, multiple= multiple,
                    placeholder= placeholder, showArrow= show_arrow, showSearch= show_search, treeCheckable= tree_checkable, 
width_dropdown= str(widthdrop) +"%", disabled= disabled, key="2", maxTagCount=maxtagcount,status=status, overall_css=".ant-select-selector {background-color: lightgrey !important;}",
only_children_select = False, 
#disable_disabled_style= False
)

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

value = st_ant_tree(treeData=tree_data, allowClear= True, bordered= border, max_height= maxheight, filterTreeNode= filter_treenode, multiple= False,
                    placeholder= placeholder, showArrow= show_arrow, showSearch= show_search, treeCheckable= False, 
width_dropdown= str(widthdrop) +"%", disabled= disabled, key="4", maxTagCount=maxtagcount,status=status, overall_css=".ant-select-selector {background-color: lightgrey !important;}",
only_children_select = False, 
#disable_disabled_style= False
)

st.write(value)