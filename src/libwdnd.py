import xml.etree.ElementTree as ET
import os
from nicegui import ui

def read_catalog(_cat):
    with open(_cat) as f:
        _c = f.read().splitlines()
        return(_c)


def get_attribute(_tree, _attr, _dict):
    try:
        _value = _tree.find(_attr).text

        if _attr == 'size':
            _dict[_attr] = convert_size(_value)
        else:
            _dict[_attr] = _value
        print(_attr + " : " + _dict[_attr])
    except:
        _dict[_attr] = 'N/A'
        print("Failed to find " + _attr + ".")


def create_xml_tree(_data_file):
    try:
        _data_file = _data_file#.rstrip()
        _tree = ET.parse(_data_file)
        return _tree
    except:
        print(f"Error with {_data_file}: XML data file not found.")


def read_xml(_tree, _list, _dict):
    for _field in _list:
        get_attribute(_tree, _field, _dict)
    get_source(_tree, 'trait', _dict)


def convert_size(_s):
    _size_dict = {
        "T": "tiny",
        "S": "small",
        "M": "medium",
        "L": "large",
        "H": "huge",
        "G": "gargantuan"
    }
    try:
        return(_size_dict[_s])
    except:
        print("Size not in dictionary.")


def get_source(_tree, _type, _dict):
    for _elem in _tree.findall(_type):
        _elemname = _elem.find('name').text
        if _elemname == 'Source':
            _elemtext = _elem.find('text').text
            _dict['source'] = _elemtext


def get_block(_tree, _dict, _attr):
    for _e in _tree.findall(_attr):
        _e_name = _e.find('name').text
        if _attr == 'trait' and _e_name == 'Source':
            continue

        _dict[_e_name] = {}

        _idx = 0
        for _t in _e.findall('text'):
            if _t.text == None:
                continue
#            print(_t.text)
            _dict[_e_name][_idx] = _t.text
            _idx += 1

#    print(str(len(actions)) + " actions")
    print(_dict)

'''
def get_action(_tree, _dict):
    for _e in _tree.findall('action'):
        _e_name = _e.find('name').text
        _dict[_e_name] = {}

        _idx = 0
        for _t in _e.findall('text'):
            if _t.text == None:
                continue
#            print(_t.text)
            _dict[_e_name][_idx] = _t.text
            _idx += 1

#    print(str(len(actions)) + " actions")
   # print(_dict)

def get_trait(_tree, _dict):
    for _e in _tree.findall('trait'):
        _e_name = _e.find('name').text
        if _e_name == 'Source':
            continue

        _dict[_e_name] = {}

        _idx = 0
        for _t in _e.findall('text'):
            if _t.text == None:
                continue
#            print(_t.text)
            _dict[_e_name][_idx] = _t.text
            _idx += 1

#    print(str(len(traits)) + " traits")
   # print(_dict)


def get_legend(_tree, _dict):
    for _e in _tree.findall('legendary'):
        _e_name = _e.find('name').text
        _dict[_e_name] = {}

        _idx = 0
        for _t in _e.findall('text'):
            if _t.text == None:
                continue
#            print(_t.text)
            _dict[_e_name][_idx] = _t.text
            _idx += 1

#    print(str(len(legend)) + " legendary actions")
   # print(_dict)

def on_select(_xml, _s_dict, _t_dict, _a_dict, _l_dict, _f_list):
    _t_dict.clear()
    _a_dict.clear()
    _l_dict.clear()
    _xml_dat = create_xml_tree(_xml.rstrip())
    # Added dictionaries to the next 4 lines.  hah
    read_xml(_xml_dat, _f_list, _s_dict)
    get_action(_xml_dat, _a_dict)
    get_trait(_xml_dat, _t_dict)
    get_legend(_xml_dat, _l_dict)
#    l_panel.update()
    with left_drawer:
        demog.text = (f"{_s_dict['size']}, {_s_dict['type']}, {_s_dict['alignment']}, ({_s_dict['environment']})")
        with stat_grid:
            str_value.text = _s_dict['str']
            dex_value.text = _s_dict['dex']
            con_value.text = _s_dict['con']
            int_value.text = _s_dict['int']
            wis_value.text = _s_dict['wis']
            cha_value.text = _s_dict['cha']
        stat_grid.update()
        with info_grid:
            armor_class.text = _s_dict['ac']
            hit_points.text = _s_dict['hp']
            speed.text = _s_dict['speed']
            skills.text = _s_dict['skill']
            saves.text = _s_dict['save']
            resist.text = _s_dict['resist']
            immune.text = _s_dict['immune']
            condimmu.text = _s_dict['conditionImmune']
            vulnerable.text = _s_dict['vulnerable']
            senses.text = _s_dict['senses']
            languages.text = _s_dict['languages']
            challenge.text = _s_dict['cr']
            pass_perc.text = _s_dict['passive']
        info_grid.update()
    with t_panel:
        t_panel.clear()
        trait_data(_t_dict)
    with a_panel:
        a_panel.clear()
        action_data(_a_dict)
    with l_panel:
        l_panel.clear()
        legend_data(_l_dict)
    with footer:
        source.text = _s_dict['source']
    footer.update()
'''

def get_stat_mod(_stat):
    if _stat == "1":
        _stat_mod = "(-5)"
    elif _stat == "2" or _stat == "3":
        _stat_mod = "(-4)"
    elif _stat == "4" or _stat == "5":
        _stat_mod = "(-3)"
    elif _stat == "6" or _stat == "7":
        _stat_mod = "(-2)"
    elif _stat == "8" or _stat == "9":
        _stat_mod = "(-1)"
    elif _stat == "10" or _stat == "11":
        _stat_mod = "(+0)"
    elif _stat == "12" or _stat == "13":
        _stat_mod = "(+1)"
    elif _stat == "14" or _stat == "15":
        _stat_mod = "(+2)"
    elif _stat == "16" or _stat == "17":
        _stat_mod = "(+3)"
    elif _stat == "18" or _stat == "19":
        _stat_mod = "(+4)"
    elif _stat == "20" or _stat == "21":
        _stat_mod = "(+5)"
    elif _stat == "22" or _stat == "23":
        _stat_mod = "(+6)"
    elif _stat == "24" or _stat == "25":
         _stat_mod = "(+7)"
    elif _stat == "26" or _stat == "27":
         _stat_mod = "(+8)"
    elif _stat == "28" or _stat == "29":
        _stat_mod = "(+9)"
    elif _stat == "30":
        _stat_mod = "(+10)"    
    else:
        _stat_mod = "(X)"

    return _stat_mod


@ui.refreshable
def action_data(_dict) -> None:
    for _x in _dict:
        ui.label(_x).tailwind.font_weight('extrabold').text_decoration('underline')
        for _y in _dict[_x]:
            ui.label(_dict[_x][_y])


@ui.refreshable
def trait_data(_dict) -> None:
    for _x in _dict:
        ui.label(_x).tailwind.font_weight('extrabold').text_decoration('underline')
        for _y in _dict[_x]:
            ui.label(_dict[_x][_y])


@ui.refreshable
def legend_data(_dict) -> None:
    for _x in _dict:
        ui.label(_x).tailwind.font_weight('extrabold').text_decoration('underline')
        for _y in _dict[_x]:
            ui.label(_dict[_x][_y])


def select_dir(_node):
    if _node == "monster":
        _dir = "Monsters"
    elif _node == "item":
        _dir = "Items"
    elif _node == "class":
        _dir = "Classes"
    elif _node == "race":
        _dir = "Races"
    elif _node == "spell":
        _dir = "Spells"
    elif _node == "background":
        _dir = "Backgrounds"
    elif _node == "feat":
        _dir = "Feats"

    return _dir


def xml_split(_node, _tree, _dir):
#    node = _node
    root = _tree.getroot()

    for item in root.findall(_node):
        _name = item.find('name').text
        _name = _name.replace("/", "-")
#        print(_node," --> ",_dir," --> ",_name)
        if not os.path.exists(_dir):
            os.makedirs(_dir)
        with open(_dir + '/' + _name + '.xml', 'wb') as f:
            ET.ElementTree(item).write(f)
#        with open('catalog.txt', 'wb') as c:
        catalog = open("catalog.txt", "a")
        catalog.write(_dir + '/' + _name + ".xml\n")
        catalog.close


def choose_xml():
    file_idx = 0
    file_dict = {}
    for x in os.listdir():
        if x.endswith(".xml"):
            # Prints only text file present in My Folder
            file_dict[file_idx] = x
            print(file_idx, " ", x)
            file_idx += 1

    if file_idx < 1:
        print("No XML file found.")
        exit()

    if file_idx == 1:
        print("Found ", file_dict[0].rstrip(), " in the current directory.")
        source_xml = file_dict[0]
    else:
        select_xml = input("Select the number of the source XML file:  ")
        source_xml = file_dict[select_xml]

    #xml_file = file_dict[0].rstrip()
    Tree = ET.parse(source_xml)
    return(Tree)


def create_xml_dirs(_tree):
    _cats = ["monster","item","class","race","spell","background","feat"]

    for _c in _cats:
        _dir = select_dir(_c)
        xml_split(_c, _tree, _dir)
        