from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import (
    ELNAnnotation,
    SectionProperties,
)
from nomad.metainfo import (
    Quantity,
    SchemaPackage,
    Section,
)
from nomad.metainfo.metainfo import MEnum

m_package = SchemaPackage()


class SiCDefect(Schema):
    m_def = Section(
        a_eln=ELNAnnotation(
            properties=SectionProperties(
                order=[
                    'defect_name',
                    'defect_type',
                    'defect_charge',
                    'defect_level',
                ],
            )
        )
    )

    defect_name = Quantity(
        type=str,
        description='Name of the defect',
        a_eln=ELNAnnotation(
            component = 'StringEditQuantity',
            label = 'Defect Name',
        ),
    )

    defect_type = Quantity(
        type=MEnum(['Vacancy', 'Interstitial', 'Substitutional']),
        description='Type of the defect',
        a_eln=ELNAnnotation(
            component = 'EnumEditQuantity',
            label = 'Defect Type',
        ),
    )   

    defect_charge = Quantity(
        type=int,
        description='Charge of the defect',
        a_eln=ELNAnnotation(
            component = 'NumberEditQuantity',
            label = 'Defect Charge',
        ),
    )

    defect_level = Quantity(
        type=float,
        unit = 'eV',
        description='Energy level of the defect',
        a_eln=ELNAnnotation(
            component = 'NumberEditQuantity',
            label = 'Defect Level',
            default_display_unit = 'eV',
        ),
    )

# delete the entire normalize method

m_package.__init_metainfo__()
