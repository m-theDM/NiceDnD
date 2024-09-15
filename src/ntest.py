#!/usr/bin/env python3
from libndndui import display_monster_cards, display_background_cards, \
    display_spell_cards, display_race_cards, display_class_cards, \
    display_feat_cards, display_item_cards, populate_left_drawer, \
    populate_right_drawer
from libwdnd import create_xml_tree, read_xml, get_block, get_stat_mod, \
    read_catalog, select_dir, xml_split, choose_xml, create_xml_dirs
    
from nicegui import ui
import xml.etree.ElementTree as ET
import os

version = '1.1'
# catalog = 'catalog.txt'

# if not os.path.isfile(catalog):
#     print("No catalog file found.")
#     src_xml_tree = choose_xml()
#     create_xml_dirs(src_xml_tree)

# contents = read_catalog(catalog)


def reset_left_drawer(_drawer) -> None:
    # left_drawer.clear()
    with _drawer:
        # populate_left_drawer.refresh(on_select, left_drawer, card_row, contents)
        populate_left_drawer.refresh()
# end reset_left_drawer


# def show_monster() -> None:
#     demog.text = (f"{_s_dict['size']}, \
#                   {_s_dict['type']}, \
#                   {_s_dict['alignment']}, \
#                   ({_s_dict['environment']})"\
#                  )
# end show_monster

def on_select(_x, _drawer, _card_row) -> None:
    _drawer.toggle()
    _card_row.clear()
    _y = _x.split('/')[0]
    print(_y)

    if _y == 'Monsters':
        with _card_row:
            display_monster_cards(_x)
            display_monster_cards.refresh()
    elif _y == 'Spells':
        with _card_row:
            display_spell_cards(_x)
            display_spell_cards.refresh()
    elif _y == 'Items':
        with _card_row:
            display_item_cards(_x)
            display_item_cards.refresh()
    elif _y == 'Races':
        with _card_row:
            display_race_cards(_x)
            display_race_cards.refresh()
    elif _y == 'Backgrounds':
        with _card_row:
            display_background_cards(_x)
            display_background_cards.refresh()
    elif _y == 'Classes':
        with _card_row:
            display_class_cards(_x)
            display_class_cards.refresh()
    elif _y == 'Feats':
        with _card_row:
            display_feat_cards(_x)
            display_feat_cards.refresh()
    _card_row.update()
    reset_left_drawer(_drawer)
# end on_select

    
with ui.header().classes(replace='row items-center') as header:
    home_button = ui.button(on_click=lambda: left_drawer.toggle(), icon='menu').props('flat color=white')
    # settings_button = ui.button(on_click=lambda: right_drawer.toggle(), icon='settings').props('flat color=white').classes('absolute-right')
    title = ui.label('NiceD&D 5E Codex').classes('left').tailwind.font_size('2xl').font_weight('extrabold')
    version = ui.label().classes('right').tailwind.font_size('lg')
    version.text = (f"Ver. {version}")


# with ui.row(wrap=False, align_items='stretch').style('width: 100%') as card_row:
# #with ui.row(wrap=False).style('background: red; width: 100%') as card_row:
# # with ui.row(wrap=False, align_items='stretch').style('background: red; width: 100%') as card_row:
#     with ui.card().style('width: 100%'):
#         ui.label('')
with ui.grid(columns=('auto auto auto auto')).classes('w-full') as card_row:
    pass
    # with ui.card().style('width: 100%'):
    #     ui.label('card1')
    # with ui.card().style('width: 100%'):
    #     ui.label('card2')
    # with ui.card().style('width: 100%'):
    #     ui.label('card3')


with ui.left_drawer().classes('bg-blue-100').props('width=450') as left_drawer:
    # populate_left_drawer(on_select, left_drawer, card_row, contents)
    populate_left_drawer(on_select, left_drawer, card_row)

# # The settings drawer (right_drawer) is currently hidden.
# with ui.right_drawer().classes('bg-blue-100').props('width=450') as right_drawer:
#     populate_right_drawer()

# settings_button.set_visibility(False)
# right_drawer.set_visibility(False)

ui.run()


'''
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

#card_row.set_visibility(False)
    # with ui.card().style('width: 400px') as stat_card:
    #     monster_name = ui.label('Monster')
    #     monster_name.tailwind.font_size('2xl').font_weight('bold')
    #     demog = ui.label("size, type, alignment, (environment)")
    #     demog.tailwind.font_style('italic')
    #     ui.separator().style('width: 100%')
    #     with ui.grid(columns=('auto auto auto auto auto auto')) as stat_grid:
    #         ui.label('STR').tailwind.font_weight('extrabold').text_decoration('underline')
    #         ui.label('DEX').tailwind.font_weight('extrabold').text_decoration('underline')
    #         ui.label('CON').tailwind.font_weight('extrabold').text_decoration('underline')
    #         ui.label('INT').tailwind.font_weight('extrabold').text_decoration('underline')
    #         ui.label('WIS').tailwind.font_weight('extrabold').text_decoration('underline')
    #         ui.label('CHA').tailwind.font_weight('extrabold').text_decoration('underline')
    #         str_value = ui.label('-')
    #         str_value.tailwind.align_content('center')
    #         dex_value = ui.label('-')
    #         dex_value.tailwind.align_items('center')
    #         con_value = ui.label('-')
    #         con_value.tailwind.align_items('center')
    #         int_value = ui.label('-')
    #         int_value.tailwind.align_items('center')
    #         wis_value = ui.label('-')
    #         wis_value.tailwind.align_items('center')
    #         cha_value = ui.label('-')
    #         cha_value.tailwind.align_items('center')
    #     ui.separator().style('width: 100%')
    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Armor Class: ').tailwind.font_weight('extrabold')
    #         armor_class = ui.label('9')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Armor Class: ').tailwind.font_weight('extrabold')
    #         armor_class = ui.label('20')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Hit Points:').tailwind.font_weight('extrabold')
    #         hit_points = ui.label('30')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Speed:').tailwind.font_weight('extrabold')
    #         speed = ui.label('')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Skills:').tailwind.font_weight('extrabold')
    #         skills =  ui.label('')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Saves:').tailwind.font_weight('extrabold')
    #         saves =  ui.label('')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Resistances:').tailwind.font_weight('extrabold')
    #         resist = ui.label('')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Immunities:').tailwind.font_weight('extrabold')
    #         immune =  ui.label("cold, fire; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered")

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Condition Immunities:').tailwind.font_weight('extrabold')
    #         condimmu =  ui.label('')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Vulnerabilities:').tailwind.font_weight('extrabold')
    #         vulnerable =  ui.label('')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Senses:').tailwind.font_weight('extrabold')
    #         senses = ui.label('')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Languages:').tailwind.font_weight('extrabold')
    #         languages =  ui.label('')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Challenge Rating:').tailwind.font_weight('extrabold')
    #         challenge =  ui.label('')

    #     with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
    #         ui.label('Passive Perception:').tailwind.font_weight('extrabold')
    #         pass_perc = ui.label('')
        # ui.image('https://picsum.photos/id/684/640/360')
        # with ui.card_section():
        #     ui.label('Lorem ipsum dolor sit amet, consectetur adipiscing elit, ...')

        # with ui.tabs() as header_tabs:
        #     header_tabs.classes('right')
        #     with header_tabs:
        #         traits_tab = ui.tab('Traits')
        #         traits_tab.set_visibility(True)
        #         actions_tab = ui.tab('Actions')
        #         actions_tab.set_visibility(True)
        #         legend_tab = ui.tab('Legendary')
        #         legend_tab.set_visibility(True)
        #         spelld_tab = ui.tab('Spells')
        #         spelld_tab.set_visibility(False)
        #         itemd_tab = ui.tab('Items')
        #         itemd_tab.set_visibility(False)
        # with ui.tab_panels(header_tabs, value='').classes('w-full'):
        #     with ui.tab_panel('Traits').style('width: 90%') as t_panel:
        #         panel_ctl(t_panel)
        #     with ui.tab_panel('Actions').style('width: 90%') as a_panel:
        #         panel_ctl(a_panel)
        #     with ui.tab_panel('Legendary').style('width: 90%') as l_panel:
        #         panel_ctl(l_panel)
        #     with ui.tab_panel('Spells').style('width: 90%') as s_panel:
        #         panel_ctl(s_panel)
        #     with ui.tab_panel('Items').style('width: 90%') as i_panel:
        #         panel_ctl(i_panel)
        #     with ui.tab_panel('Race').style('width: 90%') as r_panel:
        #         panel_ctl(r_panel)
        #     with ui.tab_panel('Backgrounds').style('width: 90%') as b_panel:
        #         panel_ctl(b_panel)
        #     with ui.tab_panel('Classes').style('width: 90%') as c_panel:
        #         panel_ctl(c_panel)
        #     with ui.tab_panel('Feats').style('width: 90%') as f_panel:
        #         panel_ctl(f_panel)
    # stat_card.set_visibility(False)
    # monster_trait_card.set_visibility(False)
    # monster_action_card.set_visibility(False)
    # monster_legend_card.set_visibility(False)
'''


'''
I need to split the main panel into two sections.  One for the static data and one for the tabs.



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
'''
'''
@ui.refreshable
def populate_left_drawer() -> None:
    _mselect = ui.select(label='Monsters',
                       options=['monster'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value, welcome, left_drawer, card_row),
                       clearable=True,
                       ).classes('w-96')
    _mselect.tailwind.font_size('lg')
    _sselect = ui.select(label='Spells',
                       options=['spell'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value, welcome, left_drawer, card_row),
                       clearable=True,
                       ).classes('w-96')
    _sselect.tailwind.font_size('lg')
    _iselect = ui.select(label='Items',
                       options=['item'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value, welcome, left_drawer, card_row),
                       clearable=True,
                       ).classes('w-96')
    _cselect = ui.select(label='Classes',
                       options=['class'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value, welcome, left_drawer, card_row),
                       clearable=True,
                       ).classes('w-96')
    _rselect = ui.select(label='Race',
                       options=['races'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value, welcome, left_drawer, card_row),
                       clearable=True,
                       ).classes('w-96')
    _bselect = ui.select(label='Backgrounds',
                       options=['background'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value, welcome, left_drawer, card_row),
                       clearable=True,
                       ).classes('w-96')
    _fselect = ui.select(label='Feats',
                       options=['feat'],
                       with_input=True,
                       on_change=lambda e: on_select(e.value, welcome, left_drawer, card_row),
                       clearable=True,
                       ).classes('w-96')
'''
'''
def display_monster_cards() -> None:
    with ui.card().style('width: 400px') as stat_card:
        monster_name = ui.label('Monster')
        monster_name.tailwind.font_size('2xl').font_weight('bold')
        demog = ui.label("size, type, alignment, (environment)")
        demog.tailwind.font_style('italic')
        ui.separator().style('width: 100%')
        with ui.grid(columns=('auto auto auto auto auto auto')) as stat_grid:
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
        ui.separator().style('width: 100%')
        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Armor Class: ').tailwind.font_weight('extrabold')
            armor_class = ui.label('20')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Hit Points:').tailwind.font_weight('extrabold')
            hit_points = ui.label('30')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Speed:').tailwind.font_weight('extrabold')
            speed = ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Skills:').tailwind.font_weight('extrabold')
            skills =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Saves:').tailwind.font_weight('extrabold')
            saves =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Resistances:').tailwind.font_weight('extrabold')
            resist = ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Immunities:').tailwind.font_weight('extrabold')
            immune =  ui.label("cold, fire; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered")

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Condition Immunities:').tailwind.font_weight('extrabold')
            condimmu =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Vulnerabilities:').tailwind.font_weight('extrabold')
            vulnerable =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Senses:').tailwind.font_weight('extrabold')
            senses = ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Languages:').tailwind.font_weight('extrabold')
            languages =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Challenge Rating:').tailwind.font_weight('extrabold')
            challenge =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Passive Perception:').tailwind.font_weight('extrabold')
            pass_perc = ui.label('')

    with ui.card().classes('right').style('width: 30%') as monster_trait_card:
        ui.label('Trait Card')
        ui.label('This is where the text goes that explains the traits of the monster.  This could be a very large section')

    with ui.card().classes('right').style('width: 30%') as monster_action_card:
        ui.label('Action Card')
        ui.label('This is where the text goes that explains the actions of the monster.  This could be a very large section')

    with ui.card().classes('right').style('width: 30%') as monster_legend_card:
        ui.label('Legendary Action Card')
        ui.label('This is where the text goes that explains the legendary actions of the monster.  This could be a very large section')
'''
    
'''
with ui.card().style('width: 400px') as stat_card:
        spell_name = ui.label('Spell')
        spell_name.tailwind.font_size('2xl').font_weight('bold')
        demog = ui.label("size, type, alignment, (environment)")
        demog.tailwind.font_style('italic')
        ui.separator().style('width: 100%')
        with ui.grid(columns=('auto auto auto auto auto auto')) as stat_grid:
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
        ui.separator().style('width: 100%')
        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Armor Class: ').tailwind.font_weight('extrabold')
            armor_class = ui.label('9')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Armor Class: ').tailwind.font_weight('extrabold')
            armor_class = ui.label('20')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Hit Points:').tailwind.font_weight('extrabold')
            hit_points = ui.label('30')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Speed:').tailwind.font_weight('extrabold')
            speed = ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Skills:').tailwind.font_weight('extrabold')
            skills =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Saves:').tailwind.font_weight('extrabold')
            saves =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Resistances:').tailwind.font_weight('extrabold')
            resist = ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Immunities:').tailwind.font_weight('extrabold')
            immune =  ui.label("cold, fire; bludgeoning, piercing, and slashing from nonmagical attacks that aren't silvered")

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Condition Immunities:').tailwind.font_weight('extrabold')
            condimmu =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Vulnerabilities:').tailwind.font_weight('extrabold')
            vulnerable =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Senses:').tailwind.font_weight('extrabold')
            senses = ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Languages:').tailwind.font_weight('extrabold')
            languages =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Challenge Rating:').tailwind.font_weight('extrabold')
            challenge =  ui.label('')

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Passive Perception:').tailwind.font_weight('extrabold')
            pass_perc = ui.label('')
''' 
'''
def display_spell_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Spell')
        _name.tailwind.font_size('2xl').font_weight('bold')

def display_item_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Item')
        _name.tailwind.font_size('2xl').font_weight('bold')

def display_race_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Race')
        _name.tailwind.font_size('2xl').font_weight('bold')

def display_background_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Background')
        _name.tailwind.font_size('2xl').font_weight('bold')

def display_class_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Class')
        _name.tailwind.font_size('2xl').font_weight('bold')

def display_feat_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Feat')
        _name.tailwind.font_size('2xl').font_weight('bold')
'''

'''
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

'''


'''
def clear_screen() -> None:
    pass
    # tabs.clear()
    # print('Cleared tabs.')
    # t_panel.clear()
    # print('Cleared panels.')
'''


'''
    # with ui.tabs() as header_tabs:
    #     header_tabs.classes('absolute-center')
    #     with header_tabs:
    #         traits_tab = ui.tab('Traits')
    #         traits_tab.set_visibility(False)
    #         actions_tab = ui.tab('Actions')
    #         actions_tab.set_visibility(False)
    #         legend_tab = ui.tab('Legendary')
    #         legend_tab.set_visibility(False)
    #         spelld_tab = ui.tab('Spells')
    #         spelld_tab.set_visibility(False)
    #         itemd_tab = ui.tab('Items')
    #         itemd_tab.set_visibility(False)
'''