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
    DefectSearchProjection,
)

m_package = SchemaPackage()


class SiCDefect(Schema):

    m_def = Section(
        label='SiC Defect',
        a_eln=dict(lane_width='800px'),
        categories=[UseCaseElnCategory],
    )
    
    comps = SubSection(section_def=Comps)
    energy = SubSection(section_def=Energy)
    charge = SubSection(section_def=Charge)
    capture = SubSection(section_def=Capture)

    #just for search purposes right at the moment, not to be filled in by the user
    results_search = SubSection(section_def=DefectSearchProjection)


    def normalize(self, archive, logger):
        super().normalize(archive, logger)


        #mirror results (only needed now, because of search issues, can be removed later)
        if self.results_search is None:
            self.results_search = DefectSearchProjection()

        if archive.results.properties.defect.energy_level is not None:
            self.results_search.energy_level = archive.results.properties.defect.energy_level
        if archive.results.properties.defect.capture_mechanism is not None:
            self.results_search.capture_mechanism = archive.results.properties.defect.capture_mechanism
        if archive.results.properties.defect.initial_charge_state is not None:
            self.results_search.initial_charge_state = archive.results.properties.defect.initial_charge_state
        if archive.results.properties.defect.charge_transition is not None:
            self.results_search.charge_transition = archive.results.properties.defect.charge_transition
        if archive.results.properties.defect.microscopic_defect is not None:
            self.results_search.microscopic_defect = archive.results.properties.defect.microscopic_defect
        if archive.results.properties.defect.intrinsic_components is not None:
            self.results_search.intrinsic_components = archive.results.properties.defect.intrinsic_components
        if archive.results.properties.defect.extrinsic_elements is not None:
            self.results_search.extrinsic_elements = archive.results.properties.defect.extrinsic_elements
        if archive.results.properties.defect.name is not None:
            self.results_search.name = archive.results.properties.defect.name
        if archive.results.properties.defect.electrical_capture_cross_section is not None:
            self.results_search.electrical_capture_cross_section = archive.results.properties.defect.electrical_capture_cross_section





m_package.__init_metainfo__()
