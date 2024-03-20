"""
    A Meltano stream class to interact with the Grafana OnCall Shifts API.

    This class provides methods to fetch oncall shifts from the Grafana OnCall
    system through its Alerts HTTP API. It is designed to handle operation to 
    retrieving alert details.

    References:
        Grafana OnCall Alerts API Documentation: https://grafana.com/docs/oncall/latest/oncall-api-reference/on_call_shifts/
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


class OnCallShiftsStream(GrafanaRestStream):
    """
    Meltano stream class to get oncall shifts from the Grafana OnCall system.
    """

    name = "oncall_shifts"
    path = f"/api/{API_VERSION}/on_call_shifts"
    primary_keys = ["id"]
    replication_key = None

    oncall_shifts_schema = th.ObjectType(
        th.Property(
            "id",
            th.StringType,
            description="The unique identifier for the on-call shift",
        ),
        th.Property(
            "team_id",
            th.StringType,
            description="ID of the team",
        ),
        th.Property(
            "schedule",
            th.StringType,
            description="Schedule identifier",
        ),
        th.Property(
            "name",
            th.StringType,
            description="Name of the on-call shift",
        ),
        th.Property(
            "type",
            th.StringType,
            description="Type of the on-call shift, e.g., single_event, recurrent_event, rolling_users",
        ),
        th.Property(
            "time_zone",
            th.StringType,
            description="Optional: On-call shift time zone",
        ),
        th.Property(
            "level",
            th.IntegerType,
            description="Priority level of the on-call shift",
        ),
        th.Property(
            "start",
            th.DateTimeType,
            description="Start time of the on-call shift",
        ),
        th.Property(
            "duration",
            th.IntegerType,
            description="Duration of the on-call shift in seconds",
        ),
        th.Property(
            "rotation_start",
            th.DateTimeType,
            description="Start time of the rotation for rolling_users type",
        ),
        th.Property(
            "frequency",
            th.StringType,
            description="Frequency of the on-call shift if type is recurrent_event or rolling_users",
        ),
        th.Property(
            "interval",
            th.IntegerType,
            description="Interval for the recurrence rule",
        ),
        th.Property(
            "until",
            th.DateTimeType,
            description="End time of the recurrence rule",
        ),
        th.Property(
            "week_start",
            th.StringType,
            description="Start day of the week in iCal format",
        ),
        th.Property(
            "by_day",
            th.ArrayType(th.StringType),
            description="List of days in iCal format",
        ),
        th.Property(
            "by_month",
            th.ArrayType(th.IntegerType),
            description="List of months",
        ),
        th.Property(
            "by_monthday",
            th.ArrayType(th.IntegerType),
            description="List of days of the month",
        ),
        th.Property(
            "rolling_users",
            th.ArrayType(th.ArrayType(th.StringType)),
            description="List of lists with on-call users for rolling_users event type",
        ),
        th.Property(
            "users",
            th.ArrayType(th.StringType),
            description="List of on-call users",
        ),
        th.Property(
            "start_rotation_from_user_index",
            th.IntegerType,
            description="Index of the list of users in rolling_users, from which on-call rotation starts",
        ),
    )

    schema = oncall_shifts_schema.to_dict()
