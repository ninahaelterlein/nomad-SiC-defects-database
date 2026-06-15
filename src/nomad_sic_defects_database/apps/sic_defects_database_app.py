"""
Search Quantities are all defined in data, because nomad.config.models.ui states:
Controls the quantities that are available in the search interface.
Search quantities correspond to pieces of information that can be queried in the
search interface of the app, but also targeted in the rest of the app configuration.
You can load quantities from custom schemas as search quantities,
but note that not all quantities will be loaded: only scalar values are
supported at the moment. The include and exlude attributes can use glob syntax to
target metainfo, e.g. results.* or *.#myschema.schema.MySchema.
"""

from importlib.resources import files

import yaml
from nomad.config.models.ui import (
    App,
    Axis,
    AxisScale,
    Column,
    Dashboard,
    Menu,
    MenuItemHistogram,
    MenuItemTerms,
    MenuSizeEnum,
    ScaleEnum,
    SearchQuantities,
)

# Access the YAML file packaged in the module
try:
    yaml_path = files('nomad_sic_defects_database.apps').joinpath(
        'sic_defects_database_dashboard.yaml'
    )
    with yaml_path.open('r') as additional_file:
        widgets = yaml.safe_load(additional_file)
except Exception as e:
    raise RuntimeError(f'Failed to load widgets from YAML file: {e}')


schema = 'nomad_sic_defects_database.schema_packages.defect_schema.SiCDefect'

sic_defects_database_app = App(
    label='The SiC Defects Database',
    path='sic_defects_database',
    category='Defects',
    description='Search entries of the SiC Defects Database',
    search_quantities=SearchQuantities(include=[f'*#{schema}']),
    columns=[
        Column(
            search_quantity='entry_name',
            selected=True,
            label='Entry Name',
        ),
        Column(
            search_quantity='results.material.compound_type',
            selected=True,
            label='Name',
        ),
        Column(
            search_quantity='data.results_search.microscopic_defect',
            selected=True,
            label='Microscopic Defect',
        ),
        Column(
            search_quantity='results.material.elements',
            selected=False,
            label='Extrinsic Elements',
        ),
        Column(
            search_quantity='data.results_search.intrinsic_components',
            selected=False,
            label='Intrinsic Elements',
        ),
        Column(
            search_quantity='data.results_search.initial_charge_state',
            selected=True,
            label='Initial Charge State',
        ),
        Column(
            search_quantity='data.results_search.charge_transition',
            selected=True,
            label='Charge Transition Level (Delta)',
        ),
        Column(
            search_quantity='data.results_search.electrical_capture_cross_section',
            selected=False,
            label='Electrical Capture Cross Section',
        ),
        Column(
            search_quantity='data.results_search.capture_mechanism',
            selected=False,
            label='Capture Mechanism',
        ),
        Column(
            search_quantity='data.results_search.energy_level',
            selected=True,
            label='Energy Level (Valence Band)',
        ),
        Column(
            search_quantity='data.results_search.defect_type',
            selected=True,
            label='Defect Type',
        ),
    ],
    menu=Menu(
        items=[
            Menu(
                title='Defect Level',
                size=MenuSizeEnum.MD,
                items=[
                    MenuItemHistogram(
                        x=Axis(
                            search_quantity=f'data.results_search.energy_level#{schema}',
                            scale=ScaleEnum.LINEAR,
                            title='Defect Level',
                            # unit = 'eV',
                        ),
                        y=AxisScale(
                            scale=ScaleEnum.LINEAR,
                        ),
                        title='Energy Level (Valence Band)',
                        show_input=False,
                        n_bins=30,
                    ),
                ],
            ),
            Menu(
                title='Capture',
                size=MenuSizeEnum.MD,
                items=[
                    MenuItemHistogram(
                        x=Axis(
                            search_quantity=f'data.results_search.electrical_capture_cross_section#{schema}',
                            scale=ScaleEnum.LOG,
                            title='Electrical Capture Cross Section',
                            # unit = 'cm^2',
                        ),
                        y=AxisScale(
                            scale=ScaleEnum.LINEAR,
                        ),
                        title='Electrical Capture Cross Section',
                        show_input=False,
                        n_bins=30,
                    ),
                    MenuItemTerms(
                        search_quantity=f'data.results_search.capture_mechanism#{schema}',
                        title='Capture Mechanism',
                        show_input=True,
                        options=3,
                        width=10,
                    ),
                ],
            ),
            Menu(
                title='Charge',
                size=MenuSizeEnum.MD,
                items=[
                    MenuItemTerms(
                        search_quantity=f'data.results_search.initial_charge_state#{schema}',
                        title='Initial Charge State',
                        show_input=True,
                        options=7,
                        width=10,
                    ),
                    MenuItemHistogram(
                        x=Axis(
                            search_quantity=f'data.results_search.charge_transition#{schema}',
                            scale=ScaleEnum.LINEAR,
                            title='Charge Transition Level (Delta)',
                        ),
                        y=AxisScale(
                            scale=ScaleEnum.LINEAR,
                        ),
                        title='Charge Transition (Delta)',
                        show_input=False,
                        n_bins=3,
                    ),
                    MenuItemTerms(
                        search_quantity=f'data.results_search.defect_type#{schema}',
                        title='Defect Type',
                        show_input=True,
                        options=4,
                        width=10,
                    ),
                ],
            ),
        ],
    ),
    filters_locked={
        'entry_type': 'SiCDefect',
    },
    dashboard=Dashboard.parse_obj(widgets),
)
