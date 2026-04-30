"""contains the schema for energy related quantities of defects

*energy level (dep on valence band)*

ToDo: add energy level with respect to conduction band minimum and band gap
"""

from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import Quantity

from ..utils import add_defect_results


class Energy(ArchiveSection):
    """Energy levels of the defect"""

    energy_level_valband = Quantity(
        type=float,
        unit = 'eV',
        shape=[],
        description="""
        Energy level of the defect with respect to the valence band maximum
        """,
        a_eln=dict(
            component = 'NumberEditQuantity',
            default_display_unit = 'eV',
        ),
    )

    energy_level_conband = Quantity(
        type=float,
        unit = 'eV',
        shape=[],
        description="""
        Energy level of the defect with respect to the conduction band minimum
        """,
        a_eln=dict(
            component = 'NumberEditQuantity',
            default_display_unit = 'eV',
        ),
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        add_defect_results(archive)
        if self.energy_level_valband:
            archive.results.properties.defect.energy_level = self.energy_level_valband
#        elif self.energy_level_conband:
#            archive.results.properties.defect.energy_level = bandgap -self.energy_level_conband