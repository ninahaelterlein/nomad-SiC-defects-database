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
from nomad.datamodel.results import (
    Results,
)
from nomad.metainfo import (
    Quantity,
    SchemaPackage,
    Section,
)

from .utils import (
    Defect,
    MyProperties,
)

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
        ),
    )

    defect_type = Quantity(
        type=str,
        description='Type of the defect',
        a_eln=dict(
            component = 'EnumEditQuantity',
            props = dict(
                suggestions=[
                    'Vacancy', 
                    'Interstitial', 
                    'Substitutional'
                ]
            ),
        ),
    )   

    defect_charge = Quantity(
        type=int,
        description='Charge of the defect',
        a_eln=ELNAnnotation(
            component = 'NumberEditQuantity',
        ),
    )

    defect_level = Quantity(
        type=float,
        unit = 'eV',
        description='Energy level of the defect',
        a_eln=ELNAnnotation(
            component = 'NumberEditQuantity',
            default_display_unit = 'eV',
        ),
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)

        if archive.results is None:
            archive.results = Results()
    
        if archive.results.properties is None:
            archive.results.properties = MyProperties()
    
        if archive.results.properties.defect is None:
            archive.results.properties.defect = Defect()

        archive.results.properties.defect.name = self.defect_name



m_package.__init_metainfo__()
