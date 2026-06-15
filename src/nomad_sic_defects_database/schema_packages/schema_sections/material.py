
from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import Quantity


class Material(ArchiveSection):
    polytype = Quantity(
        type=str,
        shape = [],
        description = """
        SiC polytype
        """,
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(
                suggestions=[
                    '3C',
                    '2H',
                    '4H',
                    '6H',
                ]
            ),
        ),
    )

    conduction_type = Quantity(
        type=str,
        shape= [],
        description = """
        Conduction type of the base material
        """,
        a_eln=dict(
            component = 'EnumEditQuantity',
            props = dict(
                suggestions=[
                    'n-type',
                    'p-type',
                ]
            ),
        ),
    )

    doping_concentration = Quantity(
        type = float,
        shape = [],
        unit = '1/cm**3',
        description = """
        Doping concentration of the base material
        """,
        a_eln =dict(
            component = 'NumberEditQuantity',
            defaultDisplayUnit = '1/cm**3',
        ),
        a_display={'unit': '1/cm**3'},
    )

    defect_concentration = Quantity(
        type = float,
        shape = [],
        unit = '1/cm**3',
        description = """
        Defect concentration
        """,
        a_eln =dict(
            component = 'NumberEditQuantity',
        ),
        a_display={'unit': '1/cm**3'},
    )

    def normalize(self,archive,logger):
        super().normalize(archive, logger)
