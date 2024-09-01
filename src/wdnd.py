#!/usr/bin/env python3
from libwdnd import create_xml_tree, read_xml, get_block, get_stat_mod, \
    read_catalog, select_dir, xml_split, choose_xml, create_xml_dirs, \
    action_data, trait_data, legend_data
from nicegui import ui
import xml.etree.ElementTree as ET
import os

catalog = 'catalog.txt'
field_list = ['name', 'size', 'type', 'alignment', 'ac', 'hp', 'speed', 'save',\
              'skill', 'resist', 'vulnerable', 'immune', 'conditionImmune', \
              'senses', 'passive', 'languages', 'cr', 'environment', 'str', \
              'dex', 'con', 'wis', 'int', 'cha']
statblock = {}
actions = {}
traits = {}
legend = {}

if not os.path.isfile(catalog):
    print("No catalog file found.")
    src_xml_tree = choose_xml()
    create_xml_dirs(src_xml_tree)
else:
    contents = read_catalog(catalog)


def on_select(_xml, _s_dict, _t_dict, _a_dict, _l_dict, _f_list):

    # clear trait, action, and legend dictionaries
    _t_dict.clear()
    _a_dict.clear()
    _l_dict.clear()

    # read the monster xml file into an Elementree tree
    _xml_dat = create_xml_tree(_xml.rstrip())

    # Added dictionaries to the next 4 lines.  hah
    read_xml(_xml_dat, _f_list, _s_dict)
    get_block(_xml_dat, _a_dict, 'action')
    get_block(_xml_dat, _t_dict, 'trait')
    get_block(_xml_dat, _l_dict, 'legendary')

    # display statblock data in left.drawer
    with left_drawer:
        demog.text = (f"{_s_dict['size']}, {_s_dict['type']}, {_s_dict['alignment']}, ({_s_dict['environment']})")
        with stat_grid:
            str_value.text = _s_dict['str'],get_stat_mod(_s_dict['str'])
            dex_value.text = _s_dict['dex'],get_stat_mod(_s_dict['dex'])
            con_value.text = _s_dict['con'],get_stat_mod(_s_dict['con'])
            int_value.text = _s_dict['int'],get_stat_mod(_s_dict['int'])
            wis_value.text = _s_dict['wis'],get_stat_mod(_s_dict['wis'])
            cha_value.text = _s_dict['cha'],get_stat_mod(_s_dict['cha'])
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
    
    # clear the trait panel and refill it with new data
    with t_panel:
        t_panel.clear()
        trait_data(_t_dict)

    # clear the action panel and refill it with new data
    with a_panel:
        a_panel.clear()
        action_data(_a_dict)
    
    # clear the legendary action panel and refill it with new data
    with l_panel:
        l_panel.clear()
        legend_data(_l_dict)
    
    # refresh the footer with source information
    with footer:
        source.text = _s_dict['source']
    footer.update()

'''
def get_attribute(_tree, _attr):
    try:
        _value = _tree.find(_attr).text
        if _value == None:
            _value = 'none'

        if _attr == 'size':
            statblock[_attr] = convert_size(_value)
        else:
            statblock[_attr] = _value
        print(_attr + " : " + statblock[_attr])
    except:
        print("Failed to find " + _attr + ".")


def create_xml_tree(_data_file):
    try:
        _data_file = _data_file.rstrip()
        _tree = ET.parse(_data_file)
        return _tree
    except:
        print(f"Error with {_data_file}: XML data file not found.")


def read_xml(_tree, _list):
    for _field in _list:
        get_attribute(_tree, _field)
    get_source(_tree, 'trait')


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


def get_source(_tree, _type):
    for _elem in _tree.findall(_type):
        _elemname = _elem.find('name').text
        if _elemname == 'Source':
            _elemtext = _elem.find('text').text
            statblock['source'] = _elemtext


def get_action(_tree):
    for _e in _tree.findall('action'):
        _e_name = _e.find('name').text
        actions[_e_name] = {}

        _idx = 0
        for _t in _e.findall('text'):
            if _t.text == None:
                continue
#            print(_t.text)
            actions[_e_name][_idx] = _t.text
            _idx += 1

#    print(str(len(actions)) + " actions")
    print(actions)

def get_trait(_tree):
    for _e in _tree.findall('trait'):
        _e_name = _e.find('name').text
        if _e_name == 'Source':
            continue

        traits[_e_name] = {}

        _idx = 0
        for _t in _e.findall('text'):
            if _t.text == None:
                continue
#            print(_t.text)
            traits[_e_name][_idx] = _t.text
            _idx += 1

#    print(str(len(traits)) + " traits")
    print(traits)


def get_legend(_tree):
    for _e in _tree.findall('legendary'):
        _e_name = _e.find('name').text
        legend[_e_name] = {}

        _idx = 0
        for _t in _e.findall('text'):
            if _t.text == None:
                continue
#            print(_t.text)
            legend[_e_name][_idx] = _t.text
            _idx += 1

#    print(str(len(legend)) + " legendary actions")
    print(legend)

@ui.refreshable
def action_data() -> None:
    for _x in actions:
        ui.label(_x).tailwind.font_weight('extrabold')
        for _y in actions[_x]:
            ui.label(actions[_x][_y])


@ui.refreshable
def trait_data() -> None:
    for _x in traits:
        ui.label(_x).tailwind.font_weight('extrabold')
        for _y in traits[_x]:
            ui.label(traits[_x][_y])


@ui.refreshable
def legend_data() -> None:
    for _x in legend:
        ui.label(_x).tailwind.font_weight('extrabold')
        for _y in legend[_x]:
            ui.label(legend[_x][_y])
'''

with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    ui.label('D&D 5E Codex').tailwind.font_size('2xl').font_weight('extrabold')
    with ui.tabs() as tabs:
        ui.tab('Traits')
        ui.tab('Actions')
        ui.tab('Legendary')

with ui.footer(value=False) as footer:
    ui.label('Source:  ').tailwind.font_size('xl').font_weight('extrabold')
    source = ui.label('N/A')
    source.tailwind.font_size('lg')

with ui.left_drawer().classes('bg-blue-100').props('width=450') as left_drawer:
    select = ui.select(label='Enter Monster Name',
                       options=contents,
                       with_input=True,
                       on_change=lambda e: on_select(e.value, \
                                                     statblock, \
                                                        traits, \
                                                        actions, \
                                                        legend, \
                                                        field_list
                                                    ),
                       clearable=True,
                       ).classes('w-96')
    select.tailwind.font_size('lg')
    demog = ui.label("size, type, alignment, (environment)")
    demog.tailwind.font_style('italic')
    ui.separator().style('width: 90%')
    with ui.grid(columns=('auto auto auto auto auto auto')).classes() as stat_grid:
            ui.label('STR').tailwind.font_weight('extrabold').text_decoration('underline')
            ui.label('DEX').tailwind.font_weight('extrabold').text_decoration('underline')
            ui.label('CON').tailwind.font_weight('extrabold').text_decoration('underline')
            ui.label('INT').tailwind.font_weight('extrabold').text_decoration('underline')
            ui.label('WIS').tailwind.font_weight('extrabold').text_decoration('underline')
            ui.label('CHA').tailwind.font_weight('extrabold').text_decoration('underline')
            str_value = ui.label('-')
            str_value.tailwind.align_content('center')
            dex_value = ui.label('-')
            dex_value.tailwind.align_items('center')
            con_value = ui.label('-')
            con_value.tailwind.align_items('center')
            int_value = ui.label('-')
            int_value.tailwind.align_items('center')
            wis_value = ui.label('-')
            wis_value.tailwind.align_items('center')
            cha_value = ui.label('-')
            cha_value.tailwind.align_items('center')
    ui.separator().style('width: 90%')
    with ui.grid(columns='auto auto').classes() as info_grid:
            ui.label('Armor Class: ').tailwind.font_weight('extrabold')
            armor_class = ui.label('')

            ui.label('Hit Points:').tailwind.font_weight('extrabold')
            hit_points = ui.label('')

            ui.label('Speed:').tailwind.font_weight('extrabold')
            speed = ui.label('')

            ui.label('Skills:').tailwind.font_weight('extrabold')
            skills =  ui.label('')

            ui.label('Saves:').tailwind.font_weight('extrabold')
            saves =  ui.label('')

            ui.label('Resistances:').tailwind.font_weight('extrabold')
            resist = ui.label('')

            ui.label('Immunities:').tailwind.font_weight('extrabold')
            immune =  ui.label('')

            ui.label('Condition Immunities:').tailwind.font_weight('extrabold')
            condimmu =  ui.label('')

            ui.label('Vulnerabilities:').tailwind.font_weight('extrabold')
            vulnerable =  ui.label('')

            ui.label('Senses:').tailwind.font_weight('extrabold')
            senses = ui.label('')

            ui.label('Languages:').tailwind.font_weight('extrabold')
            languages =  ui.label('')

            ui.label('Challenge Rating:').tailwind.font_weight('extrabold')
            challenge =  ui.label('')

            ui.label('Passive Perception:').tailwind.font_weight('extrabold')
            pass_perc = ui.label('')

with ui.page_sticky(position='bottom-right', x_offset=20, y_offset=20):
    with ui.button(on_click=footer.toggle, icon='contact_support').props('fab'):
        ui.tooltip('Source').classes('bg-green').tailwind.font_size('lg')

with ui.tab_panels(tabs, value='Traits').classes('w-full'):
    with ui.tab_panel('Traits').style('width: 90%') as t_panel:
        trait_data(traits)
    with ui.tab_panel('Actions').style('width: 90%') as a_panel:
        action_data(actions)
    with ui.tab_panel('Legendary').style('width: 90%') as l_panel:
        legend_data(legend)


ui.run()