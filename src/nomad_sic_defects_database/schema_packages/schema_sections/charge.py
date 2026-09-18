"""contains the schema for charge related quantities of defects

*initial charge state, charge transition*
"""

from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import Quantity

from ..utils import add_defect_results


class Charge(ArchiveSection):
    initial_charge_state = Quantity(
        type=str,
        shape=[],
        description="""
        THIS IS ALWAYS THE "SMALLER" CHARGE STATE, e.g., for a charge transition of -3/0, the initial charge state is -3.
        Initial charge state of the defect (possible values: '---' (3-), '--' (2-), '-', '0', '+', '++', '+++', 
        often also given as eg (-3/0). Here, initial charge state is -3, final charge state is 0, and the charge transition is 3).
        Sometimes, '=' is used as '--'
        """,
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(
                suggestions=[
                    '---',
                    '--',
                    '-',
                    '0',
                    '+',
                    '++',
                    '+++',
                ]
            ),
        ),
    )

    charge_transition = Quantity(
        type=int,
        shape=[],
        description="""
        Charge transition level of the defect (Delta of initial and final charge states, e.g., 1 for single transition, 2 for double transition), not an energy value.
        """,
        a_eln=dict(
            component='NumberEditQuantity',
        ),
    )

    @staticmethod
    def normalize_charge_state(value):
        if value is None:
            return None

        value = str(value).strip()

        # Bereits korrekt: "+", "++", "-", "---", ...
        if all(c in "+-" for c in value):
            return value

        # "2+" -> "++", "3-" -> "---"
        if value[:-1].isdigit() and value[-1] in "+-":
            return value[-1] * int(value[:-1])

        # z.B. "0"
        return value

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        add_defect_results(archive)
        if self.initial_charge_state is not None:
            #normalize charge state
            self.initial_charge_state = self.normalize_charge_state(self.initial_charge_state)
            archive.results.properties.defect.initial_charge_state = (
                self.initial_charge_state
            )
        if self.charge_transition is not None:
            archive.results.properties.defect.charge_transition = self.charge_transition
        if (
            archive.results.properties.defect.charge_transition is not None
            and archive.results.properties.defect.initial_charge_state is not None
        ):
            double = 2
            factor = 'double ' if self.charge_transition == double else ''
            typ = (
                'donor' if self.initial_charge_state in ['0', '+', '++'] else 'acceptor'
            )
            archive.results.properties.defect.defect_type = f'{factor}{typ}-like'
