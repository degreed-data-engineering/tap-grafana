"""
    A Meltano stream class to interact with the Grafana OnCall Alerts API.

    This class provides methods to fetch alerts from the Grafana OnCall
    system through its Alerts HTTP API. It is designed to handle operation to 
    retrieving alert details.

    References:
        Grafana OnCall Alerts API Documentation: https://grafana.com/docs/oncall/latest/oncall-api-reference/alerts/
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


class OnCallAlertsStream(GrafanaRestStream):
    """
    Meltano stream class to get alerts from the Grafana OnCall system.
    """

    name = "oncall_alerts"
    path = f"/api/{API_VERSION}/alerts"
    replication_key = None

    alert_org_schema = th.ObjectType(
        th.Property(
            "id",
            th.StringType,
            description="The unique identifier for the organization",
        ),
        th.Property("name", th.StringType, description="The name of the organization"),
    )

    alert_ticket_schema = th.ObjectType(
        th.Property(
            "id",
            th.StringType,
            description="The unique identifier for the ticket",
        ),
        th.Property(
            "url",
            th.StringType,
            description="URL of the ticket",
            nullable=True,
        ),
        th.Property(
            "title",
            th.StringType,
            description="Title of the ticket",
        ),
        th.Property(
            "status",
            th.StringType,
            description="Status of the ticket",
        ),
        th.Property(
            "description",
            th.StringType,
            description="Description of the ticket",
        ),
    )

    alert_oncall_schema = th.ObjectType(
        th.Property(
            "uid",
            th.StringType,
            description="Unique identifier for the alert",
        ),
        th.Property(
            "title",
            th.StringType,
            description="Title of the alert",
        ),
        th.Property(
            "message",
            th.StringType,
            description="Detailed message of the alert",
        ),
        th.Property(
            "permalink",
            th.StringType,
            description="URL to view the alert details",
        ),
        th.Property(
            "author_username",
            th.StringType,
            description="Username of the author of the alert",
        ),
    )

    alert_payload_schema = th.ObjectType(
        th.Property(
            "id",
            th.StringType,
            description="The unique identifier for the payload",
        ),
        th.Property(
            "org",
            alert_org_schema,
        ),
        th.Property(
            "body",
            th.StringType,
            description="The body text of the alert message",
        ),
        th.Property(
            "date",
            th.StringType,
            description="The timestamp of the alert",
        ),
        th.Property(
            "image",
            th.StringType,
            description="A URL to an image associated with the alert",
        ),
        th.Property(
            "Image",
            th.StringType,
            description="A URL to an image associated with the alert",
        ),
        th.Property(
            "title",
            th.StringType,
            description="The title of the alert",
        ),
        th.Property(
            "alert_id",
            th.StringType,
            description="The unique identifier for the alert",
        ),
        th.Property(
            "event_type",
            th.StringType,
            description="The type of event that triggered the alert",
        ),
        th.Property(
            "alert_title",
            th.StringType,
            description="The title of the alert",
        ),
        th.Property(
            "last_updated",
            th.StringType,
            description="The timestamp when the alert was last updated",
        ),
        th.Property(
            "alert_cycle_key",
            th.StringType,
            description="A unique identifier for the alert cycle",
        ),
        th.Property(
            "alert_transition",
            th.StringType,
            description="The state transition of the alert",
        ),
        th.Property(
            "state",
            th.StringType,
            description="The state of the alert",
        ),
        th.Property(
            "ruleId",
            th.IntegerType,
            description="The rule ID of the alert",
        ),
        th.Property(
            "message",
            th.StringType,
            description="The message of the alert",
        ),
        th.Property(
            "ruleUrl",
            th.StringType,
            description="The URL of the rule",
        ),
        th.Property(
            "ruleName",
            th.StringType,
            description="The name of the rule",
        ),
        th.Property(
            "evalMatches",
            th.ArrayType(
                th.ObjectType(
                    th.Property(
                        "tags",
                        th.StringType,
                        description="Tags associated with the match",
                    ),
                    th.Property(
                        "value",
                        th.NumberType,
                        description="The value of the match",
                    ),
                    th.Property(
                        "metric",
                        th.StringType,
                        description="The metric of the match",
                    ),
                ),
            ),
            description="The evaluation matches for the alert",
        ),
        th.Property(
            "ticket",
            alert_ticket_schema,
            description="Ticket details",
        ),
        th.Property(
            "alert_uid",
            th.StringType,
            description="Alert UID",
        ),
        th.Property(
            "oncall",
            alert_oncall_schema,
            description="Contains information about the oncall alert",
        ),
        th.Property(
            "image_url",
            th.StringType,
            description="URL of the image associated with the alert",
        ),
        th.Property(
            "is_amixr_heartbeat",
            th.BooleanType,
            description="Indicator if the amixr heartbeat is active",
        ),
        th.Property(
            "is_oncall_heartbeat",
            th.BooleanType,
            description="Indicator if the on-call heartbeat is active",
        ),
        th.Property(
            "link_to_upstream_details",
            th.StringType,
            description="Link to detailed information about the alert",
        ),
        th.Property(
            "is_amixr_heartbeat_restored",
            th.BooleanType,
            description="Indicator if the amixr heartbeat has been restored",
        ),
        th.Property(
            "is_oncall_heartbeat_restored",
            th.BooleanType,
            description="Indicator if the on-call heartbeat has been restored",
        ),
    )

    alert_schema = th.PropertiesList(
        th.Property(
            "id",
            th.StringType,
            description="The unique identifier for the alert",
        ),
        th.Property(
            "alert_group_id",
            th.StringType,
            description="The identifier for the group of alerts this alert belongs to",
        ),
        th.Property(
            "created_at",
            th.StringType,
            description="The date and time when the alert was created, in ISO 8601 format.",
        ),
        th.Property("payload", alert_payload_schema),
    )

    schema = alert_schema.to_dict()
