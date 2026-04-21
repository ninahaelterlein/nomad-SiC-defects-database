
#import yaml
from nomad.config.models.ui import (
    App,
    Column,
    SearchQuantities,
)

#here could be widgets imported from a yaml file

schema = 'nomad_sic_defects_database.schema.defect_schema'

sic_defects_database_app = App(
    label = 'The SiC Defects Database',
    path = 'sic_defects_database',
    category = 'Defects',
    description = 'Search entries of the SiC Defects Database',
    search_quantities = SearchQuantities(include=[f'*#{schema}']),
    columns = [
        Column(
            quantity='data.defect_name',
            selected=True,
            label='Defect Name',
        ), 
        Column(
            quantity='data.defect_type',
            selected=True,
            label='Defect Type',
        ),
        Column(
            quantity='data.defect_charge',
            selected=True,
            label='Defect Charge',
        ),
        Column(
            quantity='data.defect_level',
            selected=True,
            label='Defect Level (eV)',
        ),
    ],
    filters_locked={
        'entry_type': 'SiCDefect',
    },
)
"""
    menu = Menu(
        title = 'Energy Level',
        items = [
            MenuItemHistogram(
                x=Axis(
                    search_quantity = f'data.defect_level#{schema}',
                    scale =ScaleEnum.LINEAR,
                    title = 'Defect Level',
                    unit = 'eV',
                ),
                y=AxisScale(
                    scale = ScaleEnum.LINEAR,
                ),
                title = 'Defect Level',
                show_input = False,
                mbins = 30,
            ),
        ],
    ),
)
"""