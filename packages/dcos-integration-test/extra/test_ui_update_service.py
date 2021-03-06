__maintainer__ = 'Philipp Hinrichsen'
__contact__ = 'frontend@mesosphere.io'


def test_ui_servivce_reset(dcos_api_session):
    """ Test the reset endpoint of the UI Update Service.
    """
    r = dcos_api_session.delete('/dcos-ui-update-service/api/v1/reset/')

    assert r.status_code == 200
