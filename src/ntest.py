#!/usr/bin/env python3
from libwdnd import create_xml_tree, read_xml, get_block, get_stat_mod, \
    read_catalog, select_dir, xml_split, choose_xml, create_xml_dirs, \
    action_data, trait_data, legend_data
from nicegui import ui
import xml.etree.ElementTree as ET
import os

def monster_tabs(_state) -> None:
        if _state == 'off':
            with tabs:
                tabs.clear()
        elif _state == 'on':
            with tabs:
                ui.tab('Traits')
                ui.tab('Actions')
                ui.tab('Legendary')

def display_panel(_panel):
        ui.label('_panel')
        t_panel.update()
        #trait_data(traits)

def spell_display() -> None:
    ui.label('Spell Stuff').classes('absolute-center').tailwind.font_size('2xl').font_weight('extrabold')


def refresh_app(_type) -> None:
    if _type == 'monster':
        monster_tabs('on')
    elif _type == 'spell':
        monster_tabs('off')
        spell_display()
    
with ui.header().classes(replace='row items-center') as header:
    ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    select = ui.select(label='What do you seek?',
                       options=['monster','spell'],
                       with_input=True,
                       on_change=lambda e: refresh_app(e.value),
                    #    on_change=lambda e: select_monster(e.value, \
                    #                                  statblock, \
                    #                                     traits, \
                    #                                     actions, \
                    #                                     legend, \
                    #                                     field_list
                    #                                 ),
                       clearable=True,
                       ).classes('w-96')
    select.tailwind.font_size('lg')
# Can this be handled via the 'visibility' option?
    with ui.tabs() as tabs:
        monster_tabs('off')
    ui.label('NiceD&D 5E Codex').classes('absolute-bottom-right').tailwind.font_size('2xl').font_weight('extrabold')

with ui.tab_panels(tabs, value='Traits').classes('w-full'):
    with ui.tab_panel('Traits').style('width: 90%') as t_panel:
        display_panel('traits')
            # trait_data(traits)
    # with ui.tab_panels(tabs, value='Traits').classes('w-full'):
    #     pass
ui.run()