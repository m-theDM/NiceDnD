#!/usr/bin/env python3
from libwdnd import create_xml_tree, read_xml, get_block, get_stat_mod, \
    read_catalog, select_dir, xml_split, choose_xml, create_xml_dirs, \
    action_data, trait_data, legend_data
from nicegui import ui
import xml.etree.ElementTree as ET
import os

def monster_tabs(_state) -> None:
    with ui.tabs() as tabs:
        if _state == 'off':
            tabs.delete()
        elif _state == 'on':
            ui.tab('Traits')
            ui.tab('Actions')
            ui.tab('Legendary')

def spell_display() -> None:
    monster_tabs('off')
    ui.label('Spell Stuff').classes('absolute-center').tailwind.font_size('2xl').font_weight('extrabold')


def refresh_app(_type) -> None:
    if _type == 'monster':
        monster_tabs('on')
    elif _type == 'spell':
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
    ui.label('NiceD&D 5E Codex').classes('absolute-bottom-right').tailwind.font_size('2xl').font_weight('extrabold')

ui.run()