"""here, the results section will be defined/worked on"""

from nomad.datamodel.results import Properties
from nomad.metainfo import (
    MSection,
    Quantity,
    Section,
    SubSection,
)
from nomad.metainfo.elasticsearch_extension import (
    Elasticsearch,
    material_entry_type,
)


class Defect(MSection):
    """base class for defect related quantities"""
    m_def = Section(
        description="""
        Properties of defects.
        """
    )
    name = Quantity(
        type=str,
        shape=[],
        description="""
        Name of the defect (if known)
        """,
        a_elasticsearch=Elasticsearch(material_entry_type),
    )
    extrinsic_elements = Quantity(
        type=str,
        shape=['*'],
        description="""
        Extrinsic elements involved in the defect
        """,
        a_elasticsearch=Elasticsearch(material_entry_type),
    )
    intrinsic_components = Quantity(
        type=str,
        shape=['*'],
        description="""
        Intrinsic components involved in the defect
        """,
        a_elasticsearch=Elasticsearch(material_entry_type),
    )
    microscopic_defect = Quantity(  
        type=str,
        shape=[],
        description="""
        Microscopic defect structure
        """,
        a_elasticsearch=Elasticsearch(material_entry_type),
    )
    initial_charge_state = Quantity(
        type=int,
        shape=[],
        description="""
        Initial charge state of the defect
        """,
        a_elasticsearch=Elasticsearch(material_entry_type),
    )
    charge_transition = Quantity(
        type=int,
        shape=[],
        description="""
        Charge transition level of the defect (Delta)
        """,
        a_elasticsearch=Elasticsearch(material_entry_type),
    )
    energy_level = Quantity(
        type=float,
        shape=[],
        description="""
        Energy level of the defect (relative to valence band maximum)
        """,
        a_elasticsearch=Elasticsearch(material_entry_type),
    )
    electrical_capture_cross_section = Quantity(
        type=float,
        shape=[],
        description="""
        Electrical capture cross section of the defect
        """,
        a_elasticsearch=Elasticsearch(material_entry_type),
    )
    capture_mechanism = Quantity(
        type=str,
        shape=[],
        description="""
        Capture mechanism of the defect
        """,
        a_elasticsearch=Elasticsearch(material_entry_type),
    )


class MyProperties(Properties):
    defect = SubSection(
        sub_section=Defect.m_def,
                repeats=False,
    )