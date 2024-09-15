#!/usr/bin/env python3
from libndndui import display_monster_cards, display_background_cards, \
    display_spell_cards, display_race_cards, display_class_cards, \
    display_feat_cards, display_item_cards, populate_left_drawer, \
    populate_right_drawer
from libwdnd import create_xml_tree, read_xml, get_block, get_stat_mod, \
    read_catalog, select_dir, xml_split, choose_xml, create_xml_dirs, \
    action_data, trait_data, legend_data
from nicegui import ui
import xml.etree.ElementTree as ET
import os

with ui.header().classes(replace='row items-center') as header:
    # home_button = ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    # settings_button = ui.button(on_click=lambda: right_drawer.toggle(), icon='settings').props('flat color=white').classes('absolute-right')
    title = ui.label('NiceD&D 5E Codex').classes('left').tailwind.font_size('2xl').font_weight('extrabold')
    

# with ui.row(wrap=False, align_items='stretch').style('width: 100%') as card_row:
# #with ui.row(wrap=False).style('background: red; width: 100%') as card_row:
# # with ui.row(wrap=False, align_items='stretch').style('background: red; width: 100%') as card_row:
# #with ui.row(wrap=False, align_items='stretch').classes('w-full').style('background: red') as card_row:
#     with ui.card().style('width: 100%'):
#         ui.label('')
with ui.grid(columns=('auto auto auto auto')).classes('w-full') as main_grid:
    with ui.card().style('width: 100%'):
        ui.label('card1')
    with ui.card().style('width: 100%'):
        ui.label('card2')
    with ui.card().style('width: 100%'):
        ui.label('card3')
    with ui.card().style('width: 100%'):
        ui.label('card4')

ui.run()