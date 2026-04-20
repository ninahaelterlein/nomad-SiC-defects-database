from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class DefectSchemaPackageEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from nomad_sic_defects_database.schema_packages.defect_schema import m_package

        return m_package


defect = DefectSchemaPackageEntryPoint(
    name='DefectSchemaPackage',
    description='Defect schema package entry point configuration.',
)
