"""Grafana entry point."""

from __future__ import annotations

from tap_grafana.tap import TapGrafana

TapGrafana.cli()
