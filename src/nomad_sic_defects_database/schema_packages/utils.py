"""here, the results section will be defined/worked on

future code # --- SiC parameters ---
            Eg = 3.23         # 4H-SiC bandgap in eV @RT (Ioffe)
            Ev = 0.0
            Ec = Eg

            # Example defect levels
            defect_level = archive.results.properties.defect.energy_level

            fig = go.Figure()

            # -------------------------
            # Band regions
            # -------------------------

            # Valence band
            fig.add_shape(
                type="rect",
                xref="x",
                yref="y",
                x0=0, x1=1,
                y0=-1, y1=Ev,
                fillcolor="royalblue",
                opacity=0.25,
                line_width=0,
            )

            # Conduction band
            fig.add_shape(
                type="rect",
                xref="x",
                yref="y",
                x0=0, x1=1,
                y0=Ec, y1=Ec + 1,
                fillcolor="orange",
                opacity=0.25,
                line_width=0,
            )

            # Band edges
            fig.add_hline(y=Ev, line_width=3, line_color="blue")
            fig.add_hline(y=Ec, line_width=3, line_color="orange")

            # -------------------------
            # Defect levels
            # -------------------------

            fig.add_hline(
                y=defect_level,
                line_width=4,
                line_dash="dash",
                line_color="red",
            )

            fig.add_annotation(
                x=1.02,
                y=defect_level,
                text= "fill name here",
                showarrow=False,
                font=dict(color="black", size=14),
                xref="paper",
            )

            # -------------------------
            # Labels
            # -------------------------

            fig.add_annotation(
                x=0.5,
                y=Ec + 0.2,
                text="Conduction Band",
                showarrow=False,
                font=dict(size=16),
            )

            fig.add_annotation(
                x=0.5,
                y=Ev - 0.2,
                text="Valence Band",
                showarrow=False,
                font=dict(size=16),
            )

            # -------------------------
            # Layout
            # -------------------------

            fig.update_layout(
                width=500,
                height=700,
                template="simple_white",
                showlegend=False,
                xaxis=dict(
                    showticklabels=False,
                    showgrid=False,
                    zeroline=False,
                    range=[0, 1],
                ),
                yaxis=dict(
                    title="Energy (eV)",
                    range=[-0.5, Ec + 0.5],
                ),
                title="Defect Levels in 4H-SiC",
            )

            self.figures = [PlotlyFigure(figure=fig.to_plotly_json())]

"""

from nomad.datamodel.results import (
    Properties,
    Results,
)
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

#for plot
import plotly.graph_objects as go
from nomad.datamodel.metainfo.plot import (
    PlotlyFigure,
    PlotSection,
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


def add_defect_results(archive):
    if archive.results is None:
        archive.results = Results()
    if archive.results.properties is None:
        archive.results.properties = MyProperties()
    if archive.results.properties.defect is None:
        archive.results.properties.defect = Defect()


def plot_defect_level(archive, defect_level):
    fig = go.Figure()

    Eg = 3.23         # 4H-SiC bandgap in eV @RT (Ioffe)
    Ev = 0.0
    Ec = Eg


    # Valence band edge
    fig.add_trace(
        go.Scatter(
            x=[0, 1],
            y=[0, 0],
            mode='lines',
            line=dict(color='grey', width=8),
            name='Valence Band Maximum',
        )
    )

    # Conduction band edge
    fig.add_trace(
        go.Scatter(
            x=[0, 1],
            y=[Ec, Ec],
            mode='lines',
            line=dict(color='grey', width=8),
            name='Conduction Band Minimum',
        )
    )

    # Defect level
    fig.add_trace(
        go.Scatter(
            x=[0.4, 0.6],
            y=[defect_level, defect_level],
            mode='lines',
            line=dict(color='red', width=6),
            name='Defect',
        )
    )

    fig.update_layout(
        width=300,
        height=400,
        title='Defect Level',
        xaxis=dict(
            range=[0, 1],
            visible=False,
        ),
        yaxis=dict(
            title='Energy (eV)',
            range=[-0.2, 3.5],
        ),
        showlegend=True,
    )

    return fig