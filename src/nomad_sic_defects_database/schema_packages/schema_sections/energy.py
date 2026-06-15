"""contains the schema for energy related quantities of defects

*energy level (dep on valence band)*

ToDo: add energy level with respect to conduction band minimum and band gap
"""

from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import Quantity, SubSection

from ..utils import add_defect_results


class energy_uncertainty(ArchiveSection):
    energy_level_uncertainty = Quantity(
        type=float,
        unit='eV',
        shape=[],
        description="""
        Uncertainty of the energy level (if known)
        """,
        a_eln=dict(
            component='NumberEditQuantity',
        ),
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)


class Energy(ArchiveSection):
    energy_level_valband = Quantity(
        type=float,
        unit='eV',
        shape=[],
        description="""
        Energy level of the defect with respect to the valence band maximum (mean value)
        """,
        a_eln=dict(
            component='NumberEditQuantity',
        ),
    )

    energy_level_conband = Quantity(
        type=float,
        unit='eV',
        shape=[],
        description="""
        Energy level of the defect with respect to the conduction band minimum (mean value)
        """,
        a_eln=dict(
            component='NumberEditQuantity',
        ),
    )

    energy_uncertainty = SubSection(
        section_def=energy_uncertainty.m_def,
        repeats=False,
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)

        bandgap = 3.23

        add_defect_results(archive)
        if self.energy_level_valband is not None:
            archive.results.properties.defect.energy_level = self.energy_level_valband
        elif self.energy_level_conband is not None:
            archive.results.properties.defect.energy_level = (
                bandgap - self.energy_level_conband.magnitude
            )

