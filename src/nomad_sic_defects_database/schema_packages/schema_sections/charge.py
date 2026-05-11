"""contains the schema for charge related quantities of defects

*initial charge state, charge transition*
"""

from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import Quantity

from ..utils import add_defect_results


class Charge(ArchiveSection):

    initial_charge_state = Quantity(
        type=int,
        shape=[],
        description="""
        Initial charge state of the defect
        """,
        a_eln=dict(
            component = 'NumberEditQuantity',
        ),
    )

    charge_transition = Quantity(
        type=int,
        shape=[],
        description="""
        Charge transition level of the defect (Delta)
        """,
        a_eln=dict(
            component = 'NumberEditQuantity',
        ),
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        add_defect_results(archive)
        if self.initial_charge_state is not None:
            archive.results.properties.defect.initial_charge_state = self.initial_charge_state
        if self.charge_transition is not None:
            archive.results.properties.defect.charge_transition = self.charge_transition