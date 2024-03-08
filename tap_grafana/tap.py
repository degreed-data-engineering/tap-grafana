"""
Entry point for a Meltano tap that interacts with the Grafana REST API using Tap for argument parsing.

This script serves as the main entry point for the Meltano tap, leveraging the Tap library to
parse command-line arguments. It initializes a `GrafanaRestStream` instance, configured with
the necessary API URL and headers, and uses it to fetch and manage data from the Grafana REST API.
"""

from __future__ import annotations

from singer_sdk import Tap
from singer_sdk import typing as th  # JSON schema typing helpers

from . import streams, client


class TapGrafana(Tap):
    """Grafana tap class."""

    name = "tap-grafana"

    # TODO: Update this section with the actual config values you expect:
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            secret=True,  # Flag config as protected.
            description="The token to authenticate against the API service",
        ),
        th.Property(
            "start_date",
            th.DateTimeType,
            description="The earliest record date to sync",
        ),
        th.Property(
            "api_url",
            th.StringType,
            default="https://oncall-prod-us-central-0.grafana.net/oncall",
            description="Base url for the Grafana API service",
        ),
    ).to_dict()

    def discover_streams(self) -> list[client.GrafanaRestStream]:
        """Return a list of discovered streams.

        Returns:
            A list of discovered streams.
        """
        return [
            streams.OnCallAlertsStream(self),
            streams.OnCallAlertGroupsStream(self),
            streams.OnCallShiftsStream(self),
            streams.OnCallResolutionNotesStream(self),
        ]


if __name__ == "__main__":
    TapGrafana.cli()
