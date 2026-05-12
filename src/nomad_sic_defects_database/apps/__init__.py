from nomad.config.models.plugins import AppEntryPoint

from nomad_sic_defects_database.apps.sic_defects_database_app import (
    sic_defects_database_app,
)

sic_defects_database = AppEntryPoint(
    name='The SiC Defects Database',
    description='This app allows you to search entries in the SiC Defects Database.',
    app=sic_defects_database_app,
)
