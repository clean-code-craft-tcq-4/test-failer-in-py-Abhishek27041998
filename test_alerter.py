# This is a network alert stub used for testing
def network_alert_stub(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # Return 200 for ok
    # Return 500 for not-ok
    # stub always succeeds and returns 200
    if celcius < 100:
        return 200

    return 500


def test_alerts():
    from alerter import alert_in_celcius
    alert_failure_count = 0

    # Assert not-ok
    alert_in_celcius(400.5, network_alert_stub)
    alert_in_celcius(303.6, network_alert_stub)
    assert alert_failure_count == 2
    print(f'{alert_failure_count} alerts failed.')

    # Assert ok, but before reset alert_failure_count = 0
    alert_failure_count = 0
    alert_in_celcius(100, network_alert_stub)
    alert_in_celcius(45, network_alert_stub)
    assert alert_failure_count == 0
    print(f'{alert_failure_count} alerts failed.')

    print('All is well (maybe!)')