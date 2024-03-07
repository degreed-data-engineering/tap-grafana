"""Centralized module for importing and managing various stream classes.

This module serves as a central hub for all stream classes, providing a convenient
way to import and manage them. It explicitly imports each stream class from the
`grafana_streams` directory, making it easier to access and use these streams throughout
the application.

A sample stream classe included in this module is given below:

- `OnCallAlertsStream`: Stream represents Grafana OnCall alerts.

Each stream class is designed to handle specific Grafana API endpoints, allowing for
modular and maintainable code organization.

Usage:
    To use a stream class, import the `streams` module and then access the desired class.
    For example, to use `OnCallAlertsStream` in `tap.py` class, you would do the following:

        from . import streams
        
        def discover_streams(self) -> list[client.GrafanaRestStream]:
        '''Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        '''
        return [
            streams.OnCallAlertsStream(self),
        ]

This module ensures that all stream classes are easily accessible and well-organized,
promoting code reusability and maintainability.
"""

from tap_grafana.grafana_streams.oncall_alerts_stream import OnCallAlertsStream
from tap_grafana.grafana_streams.oncall_alert_groups_stream import (
    OnCallAlertGroupsStream,
)
