import part_data
import os
from string import Template

tree_ecm_parts_header = """
//****************************************************************************************
//  ENTRY COST MODIFIERS
//	These are the part configs
//
//	DO NOT EDIT THIS FILE DIRECTLY!!!
//	This file is generated from RP-0 Parts Browser
//
//****************************************************************************************

@ENTRYCOSTMODS:FOR[xxxRP-0]
{
"""

output_dir = os.getenv('PB_OUTPUT_DIR', "../../../GameData/RP-1/Tree/")
module_part_config_template = Template("    ${name} = ${ecm}\n")
tree_ecm_parts_footer = "}"

def generate_ecm_parts(parts):
    ecm_configs = ""
    for part in parts:
        if part['name'] is not None and len(part['name']) > 0:
            if part['mod'] != 'Engine_Config' and not part['orphan']:
                if part['entry_cost_mods'] is not None and len(part['entry_cost_mods']) > 0:
                    # for purposes I don't full understand, we replace all '.' and '_' characters with '-'
                    # and '?' with ' ' in the part names.  That's what the downstream code expects for whatever reason.
                    ecm_configs += module_part_config_template.substitute(name=part['name'].replace('_','-').replace('.','-').replace('?',' '), ecm=part['entry_cost_mods'])
    text_file = open(output_dir + "ECM-Parts.cfg", "w", newline='\n')
    text_file.write(tree_ecm_parts_header)
    text_file.write(ecm_configs)
    text_file.write(tree_ecm_parts_footer)
    text_file.close()
        