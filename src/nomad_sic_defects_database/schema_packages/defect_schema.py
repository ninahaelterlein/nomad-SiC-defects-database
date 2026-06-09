#ToDo: add more sections, eg reference, experimental details, ...


from typing import (
    TYPE_CHECKING,
)

if TYPE_CHECKING:
    pass

#for plot
from nomad.datamodel.data import (
    Schema,
    UseCaseElnCategory,
)
from nomad.datamodel.metainfo.plot import (
    PlotlyFigure,
    PlotSection,
)
from nomad.metainfo import (
    SchemaPackage,
    Section,
    SubSection,
)

from .schema_sections import (
    Capture,
    Charge,
    Components,
    DefectSearchProjection,
    Energy,
    Ref,
)
from .utils import (
    plot_defect_level,
    plot_table,
)

m_package = SchemaPackage()


class SiCDefect(Schema, PlotSection):

    m_def = Section(
        label='SiC Defect',
        a_eln=dict(lane_width='800px'),
        categories=[UseCaseElnCategory],
    )
    
    components = SubSection(section_def=Components)
    energy = SubSection(section_def=Energy)
    charge = SubSection(section_def=Charge)
    capture = SubSection(section_def=Capture)
    ref = SubSection(section_def=Ref)

    #just for search purposes right at the moment, not to be filled in by the user
    results_search = SubSection(section_def=DefectSearchProjection)


    def normalize(self, archive, logger):
        super().normalize(archive, logger)

        #plot table with defect properties
        if archive.results.properties.defect is not None:
            fig = plot_table(archive)

            self.figures = [
                PlotlyFigure(
                label='Defect Properties',
                figure=fig.to_plotly_json()
             )
            ]

        #plot defect level in bandstructure
        if archive.results.properties.defect.energy_level is not None:
            fig2 = plot_defect_level(
                archive, 
                archive.results.properties.defect.energy_level
                )
        

            self.figures.append(
                PlotlyFigure(
                label='Defect Level',
                figure=fig2.to_plotly_json()
             )
            )
        


        #mirror results (only needed now, because of search issues, can be removed later)
        if self.results_search is None:
            self.results_search = DefectSearchProjection()

        defect = archive.results.properties.defect

        for attr in [
            "energy_level",
            "capture_mechanism",
            "initial_charge_state",
            "charge_transition",
            "microscopic_defect",
            "intrinsic_components",
            "extrinsic_elements",
            "name",
            "electrical_capture_cross_section",
            "defect_type",
        ]:
            value = getattr(defect, attr)
            if value is not None:
                setattr(self.results_search, attr, value)





m_package.__init_metainfo__()
