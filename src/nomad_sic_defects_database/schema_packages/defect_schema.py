from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

from nomad.config import config
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

m_package = SchemaPackage()


class SiCDefect(Schema):
    m_def = Section(
        a_eln=ELNAnnotation(
            properties=SectionProperties(
                order=[
                    'defect_name',
                    'defect_type',
                    'defect_charge',
                    'defect_leverl',
                ],
            )
        )
    )

    defect_name = Quantity(
        type=str,
        description='Name of the defect',
        a_eln=ELNAnnotation(
            component = 'RichTextEditQuantity',
            label = 'Defect Name',
        ),
    )

    defect_type = Quantity(
        type=str,
        description='Type of the defect',
        a_eln=ELNAnnotation(
            component = 'ELNComponentEnum',
            label = 'Defect Type',
            options = ['Vacancy', 'Interstitial', 'Substitutional'],
        ),
    )   

    defect_charge = Quantity(
        type=int,
        description='Charge of the defect',
        a_eln=ELNAnnotation(
            component = 'ELNComponentEnum',
            label = 'Defect Charge',
            options = [-2, -1, 0, 1, 2],
        ),
    )

    defect_level = Quantity(
        type=float,
        description='Energy level of the defect in eV',
        a_eln=ELNAnnotation(
            component = 'ELNComponentEnum',
            label = 'Defect Level (eV)',
        ),
    )


    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

        logger.info('NewSchema.normalize', parameter=configuration.parameter)
        self.message = f'Hello {self.name}!'


m_package.__init_metainfo__()
