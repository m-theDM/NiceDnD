from nicegui import ui
from libwdnd import create_xml_tree, read_xml, get_block, get_stat_mod, \
    read_catalog, select_dir, xml_split, choose_xml, create_xml_dirs, \
    action_data, trait_data, legend_data

@ui.refreshable
def display_monster_cards(_xml) -> None:
                          #, _s_dict, _t_dict, _a_dict, _l_dict, _f_list) -> None:
    # Do I need to have statblock, traits, actions, and legend as globals or can
    # define them here?
    _field_list = ['name', 'size', 'type', 'alignment', 'ac', 'hp', 'speed', 'save',\
              'skill', 'resist', 'vulnerable', 'immune', 'conditionImmune', \
              'senses', 'passive', 'languages', 'cr', 'environment', 'str', \
              'dex', 'con', 'wis', 'int', 'cha']
    _statblock = {}
    _actions = {}
    _traits = {}
    _legend = {}

        # clear trait, action, and legend dictionaries
    # _t_dict.clear()
    # _a_dict.clear()
    # _l_dict.clear()

    # read the monster xml file into an Elementree tree
    _xml_dat = create_xml_tree(_xml.rstrip())

    # Added dictionaries to the next 4 lines.  hah
    read_xml(_xml_dat, _field_list, _statblock)
    get_block(_xml_dat, _actions, 'action')
    get_block(_xml_dat, _traits, 'trait')
    get_block(_xml_dat, _legend, 'legendary')
    
    with ui.card().style('width: 300px') as stat_card:
        _monster_name = ui.label(_statblock['name'])
        _monster_name.tailwind.font_size('2xl').font_weight('bold')
        _demog = ui.label("size, type, alignment, (environment)")
        _demog.text = (f"{_statblock['size']}, {_statblock['type']}, {_statblock['alignment']}, ({_statblock['environment']})")
        _demog.tailwind.font_style('italic')
        ui.separator().style('width: 100%')

        with ui.grid(columns=('auto auto auto auto auto auto')) as stat_grid:
            ui.label('STR').tailwind.font_weight('extrabold').text_decoration('underline')
            ui.label('DEX').tailwind.font_weight('extrabold').text_decoration('underline')
            ui.label('CON').tailwind.font_weight('extrabold').text_decoration('underline')
            ui.label('INT').tailwind.font_weight('extrabold').text_decoration('underline')
            ui.label('WIS').tailwind.font_weight('extrabold').text_decoration('underline')
            ui.label('CHA').tailwind.font_weight('extrabold').text_decoration('underline')
            str_value = ui.label(_statblock['str'])
            str_value.tailwind.align_content('center')
            dex_value = ui.label(_statblock['dex'])
            dex_value.tailwind.align_items('center')
            con_value = ui.label(_statblock['con'])
            con_value.tailwind.align_items('center')
            int_value = ui.label(_statblock['int'])
            int_value.tailwind.align_items('center')
            wis_value = ui.label(_statblock['wis'])
            wis_value.tailwind.align_items('center')
            cha_value = ui.label(_statblock['cha'])
            cha_value.tailwind.align_items('center')
        ui.separator().style('width: 100%')
        
        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Armor Class: ').tailwind.font_weight('extrabold')
            armor_class = ui.label(_statblock['ac'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Hit Points:').tailwind.font_weight('extrabold')
            hit_points = ui.label(_statblock['hp'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Speed:').tailwind.font_weight('extrabold')
            speed = ui.label(_statblock['speed'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Skills:').tailwind.font_weight('extrabold')
            skills =  ui.label(_statblock['skill'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Saves:').tailwind.font_weight('extrabold')
            saves =  ui.label(_statblock['save'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Resistances:').tailwind.font_weight('extrabold')
            resist = ui.label(_statblock['resist'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Immunities:').tailwind.font_weight('extrabold')
            immune =  ui.label(_statblock['immune'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Condition Immunities:').tailwind.font_weight('extrabold')
            condimmu =  ui.label(_statblock['conditionImmune'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Vulnerabilities:').tailwind.font_weight('extrabold')
            vulnerable =  ui.label(_statblock['vulnerable'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Senses:').tailwind.font_weight('extrabold')
            senses = ui.label(_statblock['senses'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Languages:').tailwind.font_weight('extrabold')
            languages =  ui.label(_statblock['languages'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Challenge Rating:').tailwind.font_weight('extrabold')
            challenge =  ui.label(_statblock['cr'])

        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Passive Perception:').tailwind.font_weight('extrabold')
            pass_perc = ui.label(_statblock['passive'])

    with ui.card().classes('right').classes('w-full') as trait_card:
        trait_data(_traits)
    if _traits == {}:
        trait_card.set_visibility(False)
    else:
        trait_card.set_visibility(True)

    with ui.card().classes('right').classes('w-full') as action_card:
        action_data(_actions)
    if _actions == {}:
        action_card.set_visibility(False)
    else:
        action_card.set_visibility(True)

    with ui.card().classes('right').classes('w-full') as legend_card:
        legend_data(_legend)
    if _legend == {}:
        legend_card.set_visibility(False)
    else:
        legend_card.set_visibility(True)
# end display_monster_card


def display_spell_cards(_xml) -> None:
    _field_list = ['name', 'school', 'level', 'ritual', 'time', 'range', \
                   'components', 'duration', 'classes', 'roll']
    _statblock = {}

    with ui.card().style('width: 300px') as stat_card:
        _spell_name = ui.label(_statblock['name'])
        _spell_name.tailwind.font_size('2xl').font_weight('bold')

    
@ui.refreshable
def display_spell_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Spell')
        _name.tailwind.font_size('2xl').font_weight('bold')

@ui.refreshable
def display_item_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Item')
        _name.tailwind.font_size('2xl').font_weight('bold')

@ui.refreshable
def display_race_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Race')
        _name.tailwind.font_size('2xl').font_weight('bold')

@ui.refreshable
def display_background_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Background')
        _name.tailwind.font_size('2xl').font_weight('bold')

@ui.refreshable
def display_class_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Class')
        _name.tailwind.font_size('2xl').font_weight('bold')

@ui.refreshable
def display_feat_cards() -> None:
    with ui.card().style('width: 400px') as spell_card:
        _name = ui.label('Feat')
        _name.tailwind.font_size('2xl').font_weight('bold')

@ui.refreshable
def populate_left_drawer(_selector, _drawer, _row, _contents) -> None:
    _mselect = ui.select(label='Monsters',
                       options=_contents,
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')
    _mselect.tailwind.font_size('lg')
    _sselect = ui.select(label='Spells',
                       options=['spell'],
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')
    _sselect.tailwind.font_size('lg')
    _iselect = ui.select(label='Items',
                       options=['item'],
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')
    _cselect = ui.select(label='Classes',
                       options=['class'],
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')
    _rselect = ui.select(label='Race',
                       options=['races'],
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')
    _bselect = ui.select(label='Backgrounds',
                       options=['background'],
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')
    _fselect = ui.select(label='Feats',
                       options=['feat'],
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')

@ui.refreshable
def populate_right_drawer() -> None:
    ui.select(label='XML File',
              options=['XML File'],
              with_input=True,
              on_change=lambda e: select_xml(e.value),
              clearable=True,
             ).classes('w-96')

def select_xml():
    pass

'''
def on_select(_type, _welcome, _drawer, _card_row) -> None:
    # clear_screen()
    #hide_tabs()
    _welcome.set_visibility(False)
    #display_tabs(_type)
    _drawer.toggle()
    _card_row.clear()
    if _type == 'monster':
        with _card_row:
            display_monster_cards()
    elif _type == 'spell':
        with _card_row:
            display_spell_cards()
    elif _type == 'item':
        with _card_row:
            display_item_cards()
    elif _type == 'race':
        with _card_row:
            display_race_cards()
    elif _type == 'background':
        with _card_row:
            display_background_cards()
    elif _type == 'class':
        with _card_row:
            display_class_cards()
    elif _type == 'feat':
        with _card_row:
            display_feat_cards()
    _card_row.update()
    reset_left_drawer(_drawer)
    # stat_card.set_visibility(True)
    # monster_trait_card.set_visibility(True)
    # monster_action_card.set_visibility(True)
    # monster_legend_card.set_visibility(True)
'''