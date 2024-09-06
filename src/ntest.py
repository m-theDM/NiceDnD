#!/usr/bin/env python3
from libwdnd import create_xml_tree, read_xml, get_block, get_stat_mod, \
    read_catalog, select_dir, xml_split, choose_xml, create_xml_dirs, \
    action_data, trait_data, legend_data
from nicegui import ui
import xml.etree.ElementTree as ET
import os

def display_tabs(_type) -> None:
    if _type == 'monster':
        traits_tab.set_visibility(True)
        actions_tab.set_visibility(True)
        legend_tab.set_visibility(True)
    elif _type == 'spell':
        spelld_tab.set_visibility(True)
    elif _type == 'item':
        itemd_tab.set_visibility(True)

def hide_tabs() -> None:
    traits_tab.set_visibility(False)
    actions_tab.set_visibility(False)
    legend_tab.set_visibility(False)
    spelld_tab.set_visibility(False)
    itemd_tab.set_visibility(False)

def panel_ctl(_panel):
    # if _panel == start_panel:
    #     with _panel:
    #         _welcome = ui.label('<-- Begin your search in the menu on the left.').classes('center')
    #         _welcome.tailwind.font_size('4xl')
    # else:
    ui.label('panel info')
    _panel.update()
        #trait_data(traits)

# def spell_display() -> None:
#     ui.label('Spell Stuff').classes('absolute-center').tailwind.font_size('2xl').font_weight('extrabold')


def clear_screen() -> None:
    pass
    # tabs.clear()
    # print('Cleared tabs.')
    # t_panel.clear()
    # print('Cleared panels.')


def on_select(_type) -> None:
    # clear_screen()
    hide_tabs()
    welcome.set_visibility(False)
    display_tabs(_type)
    left_drawer.toggle()

    
with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    with ui.tabs() as header_tabs:
        header_tabs.classes('absolute-center')
        with header_tabs:
            traits_tab = ui.tab('Traits')
            traits_tab.set_visibility(False)
            actions_tab = ui.tab('Actions')
            actions_tab.set_visibility(False)
            legend_tab = ui.tab('Legendary')
            legend_tab.set_visibility(False)
            spelld_tab = ui.tab('Spells')
            spelld_tab.set_visibility(False)
            itemd_tab = ui.tab('Items')
            itemd_tab.set_visibility(False)
    title = ui.label('NiceD&D 5E Codex').classes('left').tailwind.font_size('2xl').font_weight('extrabold')
    welcome = ui.label('<-- Begin your search in the menu on the left.').classes('absolute-right')
    welcome.tailwind.font_size('2xl')
'''



I need to split the main panel into two sections.  One for the static data and one for the tabs.



'''
with ui.tab_panels(header_tabs, value='').classes('w-full'):
    # with ui.tab_panel('Start').style('width: 90%') as start_panel:
    #     panel_ctl(start_panel)
    with ui.tab_panel('Traits').style('width: 90%') as t_panel:
        panel_ctl(t_panel)
    with ui.tab_panel('Actions').style('width: 90%') as a_panel:
        panel_ctl(a_panel)
    with ui.tab_panel('Legendary').style('width: 90%') as l_panel:
        panel_ctl(l_panel)
    with ui.tab_panel('Spells').style('width: 90%') as s_panel:
        panel_ctl(s_panel)
    with ui.tab_panel('Items').style('width: 90%') as i_panel:
        panel_ctl(i_panel)
    with ui.tab_panel('Race').style('width: 90%') as r_panel:
        panel_ctl(r_panel)
    with ui.tab_panel('Backgrounds').style('width: 90%') as b_panel:
        panel_ctl(b_panel)
    with ui.tab_panel('Classes').style('width: 90%') as c_panel:
        panel_ctl(c_panel)
    with ui.tab_panel('Feats').style('width: 90%') as f_panel:
        panel_ctl(f_panel)
            # trait_data(traits)
    # with ui.tab_panels(tabs, value='Traits').classes('w-full'):
    #     pass
with ui.left_drawer().classes('bg-blue-100').props('width=450') as left_drawer:
    m_select = ui.select(label='Monsters',
                       options=['monster'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value),
                       clearable=True,
                       ).classes('w-96')
    m_select.tailwind.font_size('lg')
    s_select = ui.select(label='Spells',
                       options=['spell'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value),
                       clearable=True,
                       ).classes('w-96')
    i_select = ui.select(label='Items',
                       options=['item'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value),
                       clearable=True,
                       ).classes('w-96')
    c_select = ui.select(label='Classes',
                       options=['class'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value),
                       clearable=True,
                       ).classes('w-96')
    r_select = ui.select(label='Races',
                       options=['class'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value),
                       clearable=True,
                       ).classes('w-96')
    b_select = ui.select(label='Backgrounds',
                       options=['class'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value),
                       clearable=True,
                       ).classes('w-96')
    f_select = ui.select(label='Feats',
                       options=['class'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value),
                       clearable=True,
                       ).classes('w-96')

ui.run()