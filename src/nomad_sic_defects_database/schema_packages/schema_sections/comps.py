"""contains the schema for component related quantities of defects

*name, extrinsic elements, intrinsic components and microscopic defects*

ToDo: 
add more suggestions to the intrinsic components list,
"""

from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import Quantity

from ..utils import add_defect_results


class Comps(ArchiveSection):

    extrinsic_elements = Quantity(
        type=str,
        shape=['*'],
        description="""
        Extrinsic elements involved in the defect (one per entry, eg 'N', 'Al', 'B', ...)
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
            props = dict(
                suggestions=[
                    'V_Si',
                    'V_C',
                    'Si_i',
                    'C_i',
                ]
            )
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
        if self.extrinsic_elements:
            archive.results.properties.defect.extrinsic_elements = self.extrinsic_elements
        if self.intrinsic_components:
            archive.results.properties.defect.intrinsic_components = self.intrinsic_components