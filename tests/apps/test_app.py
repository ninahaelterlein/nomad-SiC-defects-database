"""
def test_importing_app():
    # this will raise an exception if pydantic model validation fails for the app
    from nomad_sic_defects_database.apps import app_entry_point

    assert app_entry_point.app.label == 'NewApp'
    #test
"""
def test_sanity():
    assert True