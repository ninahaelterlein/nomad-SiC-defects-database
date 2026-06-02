"""
here, the results section will be defined/worked on,
Plots will also be defined here
"""

#for plot
import plotly.graph_objects as go
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
        type=str,
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

    Eg = 3.23         # 4H-SiC bandgap in eV @RT
    Ev = 0.0
    Ec = Eg

    # Example defect level
    # defect_level = 1.45

    # Valence band edge
    fig.add_trace(
        go.Scatter(
            x=[0.05, 1],
            y=[Ev, Ev],
            mode='lines',
            line=dict(color='grey', width=8),
            showlegend=False,
        )
    )

    # Conduction band edge
    fig.add_trace(
        go.Scatter(
            x=[0.05, 1],
            y=[Ec, Ec],
            mode='lines',
            line=dict(color='grey', width=8),
            showlegend=False,
        )
    )

    # Defect level
    fig.add_trace(
        go.Scatter(
            x=[0.4, 0.6],
            y=[defect_level, defect_level],
            mode='lines',
            line=dict(color='red', width=6),
            showlegend=False,
        )
    )

    # Labels / annotations
    fig.add_annotation(
        x=0,
        y=Ec,
        text="CB",
        showarrow=False,
        font=dict(size=14),
        xanchor="left",
    )

    fig.add_annotation(
        x=0,
        y=Ev,
        text="VB",
        showarrow=False,
        font=dict(size=14),
        xanchor="left",
    )

    fig.add_annotation(
        x=0.62,
        y=defect_level,
        text=f"{defect_level:.2f}",
        showarrow=False,
        font=dict(size=14, color="red"),
        xanchor="left",
    )

    fig.add_annotation(
        x=1.02,
        y=Ec,
        text=f"{Ec:.2f}",
        showarrow=False,
        font=dict(size=14),
        xanchor="left",
    )

    fig.add_annotation(
        x=1.02,
        y=Ev,
        text=f"{Ev:.0f}",
        showarrow=False,
        font=dict(size=14),
        xanchor="left",
    )

    fig.update_layout(
        width=220,
        height=400,
        title='Defect Level',
        showlegend=False,

        xaxis=dict(
            range=[0, 1.2],
            visible=False,
        ),

        yaxis=dict(
            range=[-0.2, 3.5],
            visible=False,
        ),

        plot_bgcolor='white',
    )

    return fig

def plot_table(archive):

    #define parameters
    defect = archive.results.properties.defect
    eccs = f"{defect.electrical_capture_cross_section:.2f}" if defect.electrical_capture_cross_section else "unavailable"
    capture_mechanism = defect.capture_mechanism if defect.capture_mechanism else "unavailable"
    microscopic_defect = defect.microscopic_defect if defect.microscopic_defect else "unavailable"
    intrinsic_components = defect.intrinsic_components if defect.intrinsic_components else "unavailable"
    charge_transition = defect.charge_transition if defect.charge_transition else "unavailable"
    initial_charge_state = defect.initial_charge_state if defect.initial_charge_state else "unavailable"

    # -----------------------------
    # Helper function
    # -----------------------------

    def make_cell(label, value):

        #make italic unavailable
        if value == "unavailable":
            return (
                f"<span style='color:#7a7a7a;font-size:11px;line-height:12px;font-family:Helvetica;margin-bottom:14px'>"
                f"{label}</span><br><br>"
                f"<span style='color:#000000;font-size:16px;line-height:28px;font-style:italic;font-family:Helvetica'>"
                f"{value}</span>"
            )

        else:
            return (
                f"<span style='color:#7a7a7a;font-size:11px;line-height:12px;font-family:Helvetica;margin-bottom:14px'>"
                f"{label}</span><br><br>"
                f"<span style='color:#000000;font-size:16px;line-height:28px;font-family:Helvetica'>"
                f"{value}</span>"
            )

    # -----------------------------
    # Table content
    # -----------------------------

    c1 = make_cell("intrinsic components", intrinsic_components)
    c2 = make_cell("microscopic defect", microscopic_defect)
    c3 = make_cell("initial charge state", initial_charge_state)

    c4 = make_cell("charge transition (Δ)", charge_transition)
    c5 = make_cell("electrical capture cross section", eccs)
    c6 = make_cell("capture mechanism", capture_mechanism)

    # -----------------------------
    # Plotly table
    # -----------------------------

    fig = go.Figure(
        data=[
            go.Table(
                columnwidth=[1.5,1.5,1.5],

                header=dict(
                    values=["", "", ""],   # kein Text
                    fill_color="white",    # oder "#ffffff"
                    line_color="white",    # versteckt Rahmen
                    height=0,
                ),
                cells=dict(
                    values=[
                        [c1, c4],
                        [c2, c5],
                        [c3, c6],
                    ],

                    align=["left", "left", "left"],

                    fill_color="white",
                    line_color="#dcdcdc",

                    height=60,
                )
            )
        ]
    )

    fig.update_layout(
        width=1000,
        height=220,

        margin=dict(
            l=0,
            r=0,
            t=0,
            b=0,
        ),

        font=dict(family="Helvetica"),
        paper_bgcolor="white",
    )
    return fig