#ToDo: add more sections, eg reference, experimental details, ...


from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

from nomad.datamodel.data import (
    Schema,
    UseCaseElnCategory,
)
from nomad.metainfo import (
    SchemaPackage,
    Section,
    SubSection,
)

from .schema_sections import (
    Capture,
    Charge,
    Comps,
    Energy,
)

m_package = SchemaPackage()


class SiCDefect(Schema):

    m_def = Section(
        label='SiC Defect',
        a_eln=dict(lane_width='800px'),
        categories=[UseCaseElnCategory],
    )
    
    comps = SubSection(section_def=Comps)
    energy_level = SubSection(section_def=Energy)
    charge = SubSection(section_def=Charge)
    capture = SubSection(section_def=Capture)


    def normalize(self, archive, logger):
        super().normalize(archive, logger)




m_package.__init_metainfo__()
