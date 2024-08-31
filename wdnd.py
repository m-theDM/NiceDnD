#!/usr/bin/env python3
from nicegui import ui
import xml.etree.ElementTree as ET

catalog = 'catalog.txt'
statblock = {}
actions={}
traits={}
legend={}
field_list = ['name', 'size', 'type', 'alignment', 'ac', 'hp', 'speed', 'save',\
              'skill', 'resist', 'vulnerable', 'immune', 'conditionImmune', \
              'senses', 'passive', 'languages', 'cr', 'environment', 'str', \
              'dex', 'con', 'wis', 'int', 'cha']


with open(catalog) as f:
    contents = f.read().splitlines()


def main(_xml):
    traits.clear()
    actions.clear()
    legend.clear()
    _xml_dat = create_xml_tree(_xml.rstrip())
    read_xml(_xml_dat, field_list)
    get_action(_xml_dat)
    get_trait(_xml_dat)
    get_legend(_xml_dat)
#    l_panel.update()
    with left_drawer:
        demog.text = (f"{statblock['size']}, {statblock['type']}, {statblock['alignment']}, ({statblock['environment']})")
        with stat_grid:
            str_value.text = statblock['str']
            dex_value.text = statblock['dex']
            con_value.text = statblock['con']
            int_value.text = statblock['int']
            wis_value.text = statblock['wis']
            cha_value.text = statblock['cha']
        stat_grid.update()
        with info_grid:
            armor_class.text = statblock['ac']
            hit_points.text = statblock['hp']
            speed.text = statblock['speed']
            skills.text = statblock['skill']
            saves.text = statblock['save']
            resist.text = statblock['resist']
            immune.text = statblock['immune']
            condimmu.text = statblock['conditionImmune']
            vulnerable.text = statblock['vulnerable']
            senses.text = statblock['senses']
            languages.text = statblock['languages']
            challenge.text = statblock['cr']
            pass_perc.text = statblock['passive']
        info_grid.update()
    with t_panel:
        t_panel.clear()
        trait_data()
    with a_panel:
        a_panel.clear()
        action_data()
    with l_panel:
        l_panel.clear()
        legend_data()
    with footer:
        source.text = statblock['source']
    footer.update()


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

with ui.left_drawer().classes('bg-blue-100').props('width=400') as left_drawer:
    select = ui.select(label='Enter Monster Name',
                       options=contents,
                       with_input=True,
                       on_change=lambda e: main(e.value),
                       clearable=True,
                       ).classes('w-80')
    demog = ui.label("size, type, alignment, (environment)")
    demog.tailwind.font_style('italic')
    with ui.grid(columns=('auto auto auto auto auto auto')).classes() as stat_grid:
            ui.label('STR').tailwind.font_weight('extrabold')
            ui.label('DEX').tailwind.font_weight('extrabold')
            ui.label('CON').tailwind.font_weight('extrabold')
            ui.label('INT').tailwind.font_weight('extrabold')
            ui.label('WIS').tailwind.font_weight('extrabold')
            ui.label('CHA').tailwind.font_weight('extrabold')
            str_value = ui.label('-')
            dex_value = ui.label('-')
            con_value = ui.label('-')
            int_value = ui.label('-')
            wis_value = ui.label('-')
            cha_value = ui.label('-')
    ui.separator()
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
    with ui.tab_panel('Traits') as t_panel:
        trait_data()
    with ui.tab_panel('Actions') as a_panel:
        action_data()
    with ui.tab_panel('Legendary') as l_panel:
        legend_data()


ui.run()