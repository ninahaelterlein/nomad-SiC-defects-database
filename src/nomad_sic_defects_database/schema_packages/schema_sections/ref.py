""" reference paper and data source information for SiC defects
    --> mostly taken from perovskite solar cell database ref.py"""

from nomad.datamodel.data import ArchiveSection
from nomad.metainfo import Datetime, Quantity, Section
from nomad.metainfo.metainfo import SubSection


class Author(ArchiveSection):
    name = Quantity(
        type=str,
        description='The full name of the author, typically a combination of first and last name.',
    )
    first_name = Quantity(
        type=str,
        description='The first name of the author.',
    )
    last_name = Quantity(
        type=str,
        description='The last name of the author.',
    )

    def normalize(self, archive, logger):
        if not self.name and self.first_name and self.last_name:
            self.name = f'{self.first_name} {self.last_name}'
        super().normalize(archive, logger)

class Ref(ArchiveSection):
    """Information about the source of the data. It describes who curated the data,
    the journal in which the data was published,
    the DOI number of the publication, the lead author and the publication date."""

    m_def = Section(a_eln=dict(lane_width='800px'))

    DOI_number = Quantity(
        type=str,
        shape=[],
        description="""
    The DOI number of the publication from which the data was taken.
                    """,
        a_eln=dict(component='StringEditQuantity'),
    )

    journal = Quantity(
        type=str,
        shape=[],
        description="""
    The journal in which the data was published.
                    """,
        a_eln=dict(component='StringEditQuantity'),
    )

    lead_author = Quantity(
        type=str,
        shape=[],
        description="""
    The surname of the first author. If several authors, end with et al. If the DOI number is given correctly, this will be extracted automatically from www.crossref.org
                    """,
        a_eln=dict(component='EnumEditQuantity', props=dict(suggestions=[])),
    )

    authors = SubSection(
        section_def=Author,
        repeats=True,
    )

    publication_date = Quantity(
        type=Datetime,
        shape=[],
        description="""
    Publication date. If the DOI number is given correctly, this will be extracted automatically from www.crossref.org
                    """,
    )

    def normalize(self, archive, logger):

        #here we could add a function to automatically extract the journal, lead author, 
        #authors and publication date from www.crossref.org if the DOI number is given correctly
        #see perovskite ref.py for an example of how to do this

        super().normalize(archive, logger)
