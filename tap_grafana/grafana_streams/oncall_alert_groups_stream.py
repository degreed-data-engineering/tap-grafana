"""
    A Meltano stream class to interact with the Grafana OnCall Alert Groups API.

    This class provides methods to fetch alert groups from the Grafana OnCall
    system through its Alerts HTTP API. It is designed to handle operation to 
    retrieving alert details.

    References:
        Grafana OnCall Alerts API Documentation: https://grafana.com/docs/oncall/latest/oncall-api-reference/alertgroups/
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


class OnCallAlertGroupsStream(GrafanaRestStream):
    """
    Meltano stream class to get alert groups from the Grafana OnCall system.
    """

    name = "oncall_alert_groups"
    path = f"/api/{API_VERSION}/alert_groups"
    replication_key = None

    perma_links_schema = th.ObjectType(
        th.Property(
            "slack",
            th.StringType,
            description="URL to view the alert in Slack",
        ),
        th.Property(
            "telegram",
            th.StringType,
            description="URL to view the alert in Telegram",
        ),
        th.Property(
            "web",
            th.StringType,
            description="URL to view the alert in a web browser",
        ),
    )

    alert_groups_schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The unique identifier for the alert group",
        ),
        th.Property(
            "integration_id",
            th.StringType,
            description="The ID of the integration that generated the alert group",
        ),
        th.Property(
            "route_id",
            th.StringType,
            description="The ID of the route that the alert group is associated with",
        ),
        th.Property(
            "alerts_count",
            th.IntegerType,
            description="The number of alerts included in the group",
        ),
        th.Property(
            "state",
            th.StringType,
            description="The current state of the alert group (e.g., 'resolved')",
        ),
        th.Property(
            "created_at",
            th.DateTimeType,
            description="The timestamp when the alert group was created",
        ),
        th.Property(
            "resolved_at",
            th.DateTimeType,
            description="The timestamp when the alert group was resolved",
        ),
        th.Property(
            "acknowledged_at",
            th.DateTimeType,
            nullable=True,
            description="The timestamp when the alert group was acknowledged, if applicable",
        ),
        th.Property(
            "acknowledged_by",
            th.StringType,
            nullable=True,
            description="The ID of the user who acknowledged the alert group, if applicable",
        ),
        th.Property(
            "resolved_by",
            th.StringType,
            description="The ID of the user who resolved the alert group",
        ),
        th.Property(
            "title",
            th.StringType,
            description="The title of the alert group",
        ),
        th.Property(
            "permalinks",
            perma_links_schema,
            description="Links to view the alert group in various platforms",
        ),
    )

    schema = alert_groups_schema.to_dict()
