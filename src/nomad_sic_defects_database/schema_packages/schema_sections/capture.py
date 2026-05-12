"""contains the schema for capture related quantities of defects

*electrical capture cross section, capture mechanism*

ToDo:
"""

from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import Quantity

from ..utils import add_defect_results


class Capture(ArchiveSection):

    electrical_capture_cross_section = Quantity(
        type=float,
        unit = 'cm**2',
        shape=[],
        description="""
        Electrical capture cross section of the defect
        """,
        a_eln=dict(
            component = 'NumberEditQuantity',
            default_display_unit = 'cm**2',
        ),
    )

    capture_mechanism = Quantity(
        type=str,
        shape=[],
        description="""
        Capture mechanism of the defect
        """,
        a_eln=dict(
            component = 'EnumEditQuantity',
            props = dict(
                suggestions=[
                    'multi-phonon capture',
                    'cascade capture',
                    'other',
                ]
            )
        ),
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        add_defect_results(archive)
        if self.electrical_capture_cross_section is not None:
            archive.results.properties.defect.electrical_capture_cross_section = self.electrical_capture_cross_section
        if self.capture_mechanism:
            archive.results.properties.defect.capture_mechanism = self.capture_mechanism