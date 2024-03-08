"""
    A Meltano stream class to interact with the Grafana OnCall Shifts API.

    This class provides methods to fetch oncall resolution notes from the Grafana OnCall
    system through its Alerts HTTP API. It is designed to handle operation to 
    retrieving alert details.

    References:
        Grafana OnCall Alerts API Documentation: https://grafana.com/docs/oncall/latest/oncall-api-reference/resolution_notes/
"""

from __future__ import annotations

import sys
import typing as t

from singer_sdk import typing as th

from tap_grafana.client import GrafanaRestStream

if sys.version_info >= (3, 9):
    import importlib.resources as importlib_resources
else:
    import importlib_resources


API_VERSION = "v1"


class OnCallResolutionNotesStream(GrafanaRestStream):
    """
    Meltano stream class to get oncall resolution notes from the Grafana OnCall system.
    """

    name = "oncall_resolution_notes"
    path = f"/api/{API_VERSION}/resolution_notes"
    replication_key = None

    oncall_resolution_note_schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="Unique identifier for the resolution note",
        ),
        th.Property(
            "alert_group_id",
            th.StringType,
            description="ID of the alert group associated with the resolution note",
        ),
        th.Property(
            "author",
            th.StringType,
            description="Author of the resolution note",
        ),
        th.Property(
            "source",
            th.StringType,
            description="Source of the resolution note, e.g., web, slack",
        ),
        th.Property(
            "created_at",
            th.DateTimeType,
            description="Timestamp when the resolution note was created",
        ),
        th.Property(
            "text",
            th.StringType,
            description="Text content of the resolution note",
        ),
    )

    schema = oncall_resolution_note_schema.to_dict()
