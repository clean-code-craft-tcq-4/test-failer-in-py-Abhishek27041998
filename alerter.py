from test_alerter import network_alert_stub
alert_failure_count = 0


def network_alert(celcius):
    print(f'ALERT: Temperature is {celcius} celcius')
    # This is the real production code for network_alert
    # Return 200 for ok
    # Return 500 for not-ok
    if celcius < 100:  # Some threshold
        return 200

    return 500


# Passing "network_alert" function to the following makes it
# easy for testing stub along with production code
def alert_in_celcius(farenheit, fun_network_alert):
    celcius = (farenheit - 32) * 5 / 9
    returnCode = fun_network_alert(celcius)
    if returnCode != 200:
        # non-ok response is not an error! Issues happen in life!
        # let us keep a count of failures to report
        # However, this code doesn't count failures!
        # Add a test below to catch this bug. Alter the stub above, if needed.
        global alert_failure_count
        alert_failure_count += 1  # Fixing the implementation


# Passing the stub function for testing

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
