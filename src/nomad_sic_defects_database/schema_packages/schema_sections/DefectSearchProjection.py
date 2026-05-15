"""
This is just a helper class to be able to show the search results in the app. 
(as long as I cannot use the custom results as search quantities.)
It should not be used to fill in custom data. The quantities defined here are the
same quantities that are defined in the results section. 
"""

from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import Quantity


class DefectSearchProjection(ArchiveSection):

    name = Quantity(
        type=str,
        shape=[],
        description="""
        Name of the defect (if known)
        """,
    )
    
    extrinsic_elements = Quantity(
        type=str,
        shape=['*'],
        description="""
        Extrinsic elements involved in the defect
        """,
    )

    intrinsic_components = Quantity(
        type=str,
        shape=['*'],
        description="""
        Intrinsic components involved in the defect
        """,
    )

    microscopic_defect = Quantity(  
        type=str,
        shape=[],
        description="""
        Microscopic defect structure
        """,
    )

    initial_charge_state = Quantity(
        type=int,
        shape=[],
        description="""
        Initial charge state of the defect
        """,
    )

    charge_transition = Quantity(
        type=float,
        shape=[],
        description="""
        Charge transition level of the defect (Delta)
        """,
    )

    capture_mechanism = Quantity(
        type=str,
        shape=[],
        description="""
        Capture mechanism of the defect (eg multi-phonon, Auger, ...)
        """,
    )

    electrical_capture_cross_section = Quantity(
        type=float,
        shape=[],
        description="""
        Electrical capture cross section of the defect
        """,
    )

    energy_level = Quantity(
        type=float,
        shape=[],
        description="""
        Energy level of the defect (relative to valence band maximum)
        """,
    )



 