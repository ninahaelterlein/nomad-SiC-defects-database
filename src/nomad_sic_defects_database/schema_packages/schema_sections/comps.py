"""contains the schema for component related quantities of defects

*name, extrinsic elements, intrinsic components and microscopic defects*

ToDo:
add more suggestions to the intrinsic components list,
"""

from nomad.datamodel.data import ArchiveSection
from nomad.datamodel.results import Material
from nomad.metainfo import Quantity, Section, SubSection

from ..utils import add_defect_results


class CompSpecs(ArchiveSection):
# this should be a ideally hidden subclass to Components, to be able to choose between extrinsic and intrinsic type of defects
# for now, there is no opportunity to hide it, thats why the quantities lattice_site and lattice_site_symmetry are not added here
# but separately in both intrinsic and extrinsic type of defects, as they are relevant for both types 
# (this way, CompSpecs can not be used to define component specs by accident)
    lattice_site = Quantity(
        type=str,
        shape=[],
        description="""
        Lattice site of the defect (if known)
        """,
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(
                suggestions=[
                    'Si',
                    'C',
                    'i',
                ]
            ),
        ),
    )

    lattice_site_symmetry = Quantity(
        type=str,
        shape=[],
        description="""
        Lattice site symmetry of the defect (if known)
        """,
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(
                suggestions=[
                    'hexagonal',
                    'cubic',
                ]
            ),
        ),
    )

class IntrinsicType(CompSpecs):
    m_def = Section(label= "intrinsic type")

    type = Quantity(
        type=str,
        shape=[],
        description="""
        Type of the defect
        """,
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(
                suggestions=[
                    'vacancy',
                    'Si',
                    'C',
                ]
            ),
        ),
    )



class ExtrinsicType(CompSpecs):
    m_def = Section(label= "extrinsic type")

    element = Quantity(
        type=str,
        shape=[],
        description="""
        Extrinsic element of the defect
        """,
        a_eln=dict(
            component='StringEditQuantity',
        ),
    )



class Components(ArchiveSection):
    extrinsic_elements = Quantity(
        type=str,
        shape=['*'],
        description="""
        Extrinsic elements involved in the defect (one per entry, eg 'N', 'Al', 'B', ...)
        """,
        a_eln=dict(
            component='StringEditQuantity',
        ),
    )

    intrinsic_components = Quantity(
        type=str,
        shape=['*'],
        description="""
        Intrinsic components involved in the defect
        """,
        a_eln=dict(
            component='EnumEditQuantity',
            props=dict(
                suggestions=[
                    'V_Si',
                    'V_C',
                    'Si_i',
                    'C_i',
                ]
            ),
        ),
    )

    intrinsic_automatic = Quantity(
        type=str,
        shape=['*'],
        description="""
        Intrinsic components involved in the defect, extracted automatically from the intrinsic subsection
        """,
    )

    extrinsic_automatic = Quantity(
        type=str,
        shape=['*'],
        description="""
        Extrinsic elements involved in the defect, extracted automatically from the extrinsic subsection
        """,
    )

    microscopic_defect = Quantity(
        type=str,
        shape=[],
        description="""
        Microscopic defect structure
        """,
        a_eln=dict(
            component='StringEditQuantity',
        ),
    )

    IntrinsicComponents = SubSection(
        section_def=IntrinsicType.m_def,
        repeats=True,
    )

    ExtrinsicComponents = SubSection(
        section_def=ExtrinsicType.m_def,
        repeats=True,
    )

    def normalize(self, archive, logger): # noqa: PLR0912
        super().normalize(archive, logger)
        add_defect_results(archive)
        if self.microscopic_defect is not None:
            archive.results.properties.defect.microscopic_defect = (
                self.microscopic_defect
            )
        if self.extrinsic_elements is not None:
            if not archive.results.material:
                archive.results.material = Material()
            archive.results.material.elements = self.extrinsic_elements
            archive.results.properties.defect.extrinsic_elements = (
                self.extrinsic_elements
            )
        if self.intrinsic_components is not None:
            if not archive.results.material:
                archive.results.material = Material()
            archive.results.material.functional_type = self.intrinsic_components
            archive.results.properties.defect.intrinsic_components = (
                self.intrinsic_components
            )
        if self.IntrinsicComponents is not None:
            self.intrinsic_automatic = []
            for comp in self.IntrinsicComponents:
                if comp.type is not None and comp.lattice_site is not None:
                    if comp.type == "vacancy":
                        bez = f"V_{comp.lattice_site}"
                    else:
                        bez = f"{comp.type}_{comp.lattice_site}"
                    self.intrinsic_automatic.append(bez)
        if self.ExtrinsicComponents is not None:
            self.extrinsic_automatic = []
            for comp in self.ExtrinsicComponents:
                if comp.element is not None and comp.lattice_site is not None:
                    bez = f"{comp.element}_{comp.lattice_site}"
                    self.extrinsic_automatic.append(bez)