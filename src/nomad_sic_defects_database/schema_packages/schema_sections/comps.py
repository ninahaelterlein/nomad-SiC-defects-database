"""contains the schema for component related quantities of defects

*name, extrinsic elements, intrinsic components and microscopic defects*

ToDo: 
add extrinsic elements list,
add intrinsic components list,
"""

from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import Quantity

from ..utils import add_defect_results


class Comps(ArchiveSection):
    """components of the defect"""

    extrinsic_elements = Quantity(
        type=str,
        shape=['*'],
        description="""
        Extrinsic elements involved in the defect
        """,
        a_eln=dict(
            component = 'StringEditQuantity',
        ),
    )

    intrinsic_components = Quantity(
        type=str,
        shape=['*'],
        description="""
        Intrinsic components involved in the defect
        """,
        a_eln=dict(
            component = 'StringEditQuantity',
        ),  
    )

    microscopic_defect = Quantity(  
        type=str,
        shape=[],
        description="""
        Microscopic defect structure
        """,
        a_eln=dict(
            component = 'StringEditQuantity',
        ),
    )

    def normalize(self, archive, logger):
        super().normalize(archive, logger)
        add_defect_results(archive)
        if self.microscopic_defect:
            archive.results.properties.defect.microscopic_defect = self.microscopic_defect