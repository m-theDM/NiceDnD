from nicegui import ui
from libwdnd import create_xml_tree, read_xml, get_block, get_stat_mod, \
    read_catalog, select_dir, xml_split, choose_xml, create_xml_dirs, \
    get_spell_block

@ui.refreshable
def display_block(_dict) -> None:
    for _x in _dict:
        ui.label(_x).tailwind.font_weight('extrabold').text_decoration('underline')
        for _y in _dict[_x]:
            ui.label(_dict[_x][_y])


@ui.refreshable
def display_spell_block(_dict) -> None:
    for _x in _dict:
        ui.label(_dict[_x])


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
        # trait_data(_traits)
        display_block(_traits)
    if _traits == {}:
        trait_card.set_visibility(False)
    else:
        trait_card.set_visibility(True)

    with ui.card().classes('right').classes('w-full') as action_card:
        # action_data(_actions)
        display_block(_actions)
    if _actions == {}:
        action_card.set_visibility(False)
    else:
        action_card.set_visibility(True)

    with ui.card().classes('right').classes('w-full') as legend_card:
        # legend_data(_legend)
        display_block(_legend)
    if _legend == {}:
        legend_card.set_visibility(False)
    else:
        legend_card.set_visibility(True)
# end display_monster_card



@ui.refreshable
def display_spell_cards(_xml) -> None:
    _field_list = ['name', 'school', 'level', 'ritual', 'time', 'range', \
                   'components', 'duration', 'classes', 'roll']
    _statblock = {}
    _text_block = {}

    # read the monster xml file into an Elementree tree
    _xml_dat = create_xml_tree(_xml.rstrip())
    get_spell_block(_xml_dat, _text_block, 'text')

    # Added dictionaries
    read_xml(_xml_dat, _field_list, _statblock)

    with ui.card().style('width: 600px') as stat_card:
        _spell_name = ui.label(_statblock['name'])
        _spell_name.tailwind.font_size('2xl').font_weight('bold')
        _demog = ui.label("school, level, (ritual)")
        if _statblock['level'] == 'cantrip':
            _demog.text = (f"{_statblock['school']} {_statblock['level']} ({_statblock['ritual']})")
        else:
            _demog.text = (f"{_statblock['level']} {_statblock['school']}, ({_statblock['ritual']})")
        _demog.tailwind.font_style('italic')
        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Range: ').tailwind.font_weight('extrabold')
            _spell_range = ui.label(_statblock['range'])
        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Components: ').tailwind.font_weight('extrabold')
            _spell_comp = ui.label(_statblock['components'])
        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Duration: ').tailwind.font_weight('extrabold')
            _spell_time = ui.label(_statblock['time'])
        ui.separator().style('width: 100%')
        display_spell_block(_text_block)
        ui.separator().style('width: 100%')
        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Allowed Classes: ').tailwind.font_weight('extrabold')
            _spell_class = ui.label(_statblock['classes'])
        # _name = ui.label('Spell')
        # _name.tailwind.font_size('2xl').font_weight('bold')

@ui.refreshable
def display_item_cards(_xml) -> None:
    # _field_list = ['name', 'type', 'magic', 'detail', 'weight', 'ac', \
                #    'description', 'dmg1', 'dmg2', 'dmgType']
    _field_list = ['ac', 'detail', 'dmg1', 'dmg2', 'dmgType', 'item', \
                   'magic', 'name', 'property', 'range', 'roll', 'stealth', \
                    'strength', 'text', 'type', 'value', 'weight',]
    _statblock = {}
    _text_block = {}

    _xml_dat = create_xml_tree(_xml.rstrip())
    get_spell_block(_xml_dat, _text_block, 'text')

    # Added dictionaries
    read_xml(_xml_dat, _field_list, _statblock)
    
    with ui.card().style('width: 600px') as item_card:
        _name = ui.label(_statblock['name'])
        _name.tailwind.font_size('2xl').font_weight('bold')
        _demog = ui.label("type, magical, rarity")
        _demog.text = (f"{_statblock['type']} {_statblock['magic']} ({_statblock['detail']})")
        _demog.tailwind.font_style('italic')
        for _i in ('weight', 'ac'):
            if _statblock[_i] != 'N/A':
                with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
                    _title = ui.label('')
                    _title.text = (f"{_i.title()}")
                    _title.tailwind.font_weight('extrabold')
                    _stat = ui.label(_statblock['weight'])
        if _statblock['dmg1'] == 'N/A' and _statblock['dmg2'] == N/A:
                pass
        else:
            with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
                _title = ui.label('')
                _title.text = (f"Damage:  ")
                _title.tailwind.font_weight('extrabold')
                if _statblock['dmg1'] != 'N/A' and _statblock['dmg2'] != 'N/A':
                    _dmg = ui.label()
                    _dmg.text = (f"One-handed: {_statblock['dmg1']} / Two-handed:  {_statblock['dmg2']}")
                elif _statblock['dmg2'] == 'N/A':
                    _dmg = ui.label()
                    _dmg.text = (f"One-handed: {_statblock['dmg1']}")
                elif _statblock['dmg1'] == 'N/A':
                    _dmg = ui.label()
                    _dmg.text = (f"Two-handed: {_statblock['dmg2']}")

        ui.separator().style('width: 100%')
        display_spell_block(_text_block)
        ui.separator().style('width: 100%')

@ui.refreshable
def display_race_cards(_xml) -> None:
    _field_list = ['ability', 'name', 'proficiency', 'size', \
                   'special', 'speed', 'spellAbility', 'text', 'trait']
    
    _statblock = {}
    _text_block = {}

    _xml_dat = create_xml_tree(_xml.rstrip())
    get_block(_xml_dat, _text_block, 'trait')

    # Added dictionaries
    read_xml(_xml_dat, _field_list, _statblock)

    with ui.card().style('width: 600px') as spell_card:
        _name = ui.label(_statblock['name'])
        _name.tailwind.font_size('2xl').font_weight('bold')
        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Proficiency ').tailwind.font_weight('extrabold')
            _bkgd_prof = ui.label(_statblock['proficiency'])
        ui.separator().style('width: 100%')
        display_block(_text_block)
        ui.separator().style('width: 100%')

@ui.refreshable
def display_background_cards(_xml) -> None:
    _field_list = ['name', 'proficiency', 'trait']

    _statblock = {}
    _text_block = {}

    _xml_dat = create_xml_tree(_xml.rstrip())
    get_block(_xml_dat, _text_block, 'trait')

    # Added dictionaries
    read_xml(_xml_dat, _field_list, _statblock)
    
    with ui.card().style('width: 600px') as bkgd_card:
        _name = ui.label(_statblock['name'])
        _name.tailwind.font_size('2xl').font_weight('bold')
        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Proficiency ').tailwind.font_weight('extrabold')
            _bkgd_prof = ui.label(_statblock['proficiency'])
        ui.separator().style('width: 100%')
        display_block(_text_block)
        ui.separator().style('width: 100%')

@ui.refreshable
def display_class_cards(_xml) -> None:
    _field_list = ['name', 'proficiency', 'hd']

    _statblock = {}
    _text_block = {}

    _xml_dat = create_xml_tree(_xml.rstrip())
    # get_block(_xml_dat, _text_block, 'trait')

    # Added dictionaries
    read_xml(_xml_dat, _field_list, _statblock)

    with ui.card().style('width: 600px') as spell_card:
        _name = ui.label(_statblock['name'])
        _name.tailwind.font_size('2xl').font_weight('bold')
        with ui.row(wrap=False, align_items='stretch').style('width: 100%'):
            ui.label('Proficiency ').tailwind.font_weight('extrabold')
            _bkgd_prof = ui.label(_statblock['proficiency'])
        ui.separator().style('width: 100%')
        # display_block(_text_block)
        ui.separator().style('width: 100%')

@ui.refreshable
def display_feat_cards(_xml) -> None:
    _field_list = ['name', 'prerequisite', 'proficiency', 'text']

    _statblock = {}
    _text_block = {}

    _xml_dat = create_xml_tree(_xml.rstrip())
    get_spell_block(_xml_dat, _text_block, 'text')

    # Added dictionaries
    read_xml(_xml_dat, _field_list, _statblock)

    with ui.card().style('width: 600px') as spell_card:
        _name = ui.label(_statblock['name'])
        _name.tailwind.font_size('2xl').font_weight('bold')
        ui.separator().style('width: 100%')
        display_spell_block(_text_block)
        ui.separator().style('width: 100%')

@ui.refreshable
def populate_left_drawer(_selector, _drawer, _row, _contents='') -> None:
    with open('Monsters/catalog.txt', 'r') as f:
        _m_cont = f.read().splitlines()

    _mselect = ui.select(label='Monsters',
                       options=_m_cont,
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')
    _mselect.tailwind.font_size('lg')

    with open('Spells/catalog.txt', 'r') as f:
        _s_cont = f.read().splitlines()

    _sselect = ui.select(label='Spells',
                       options=_s_cont,
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')
    _sselect.tailwind.font_size('lg')

    with open('Items/catalog.txt', 'r') as f:
        _i_cont = f.read().splitlines()

    _iselect = ui.select(label='Items',
                       options=_i_cont,
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')
    _iselect.tailwind.font_size('lg')

    with open('Classes/catalog.txt', 'r') as f:
        _c_cont = f.read().splitlines()

    _cselect = ui.select(label='Classes',
                       options=_c_cont,
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')

    with open('Races/catalog.txt', 'r') as f:
        _r_cont = f.read().splitlines()

    _rselect = ui.select(label='Race',
                       options=_r_cont,
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')

    with open('Backgrounds/catalog.txt', 'r') as f:
        _b_cont = f.read().splitlines()

    _bselect = ui.select(label='Backgrounds',
                       options=_b_cont,
                       with_input=True,
                       on_change=lambda e: _selector(e.value, _drawer, _row),
                       clearable=True,
                       ).classes('w-96')

    with open('Feats/catalog.txt', 'r') as f:
        _f_cont = f.read().splitlines()

    _fselect = ui.select(label='Feats',
                       options=_f_cont,
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