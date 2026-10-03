# -*- coding: utf-8 -*-
"""Lab 00C — Introduction: Visualizing Results with Plotly.

This lab is a companion to Lab 00. Instead of an image-processing task, the
goal is to get comfortable with the Plotly charting patterns you will reuse
in every later lab: multi-panel image grids, heatmaps, and line charts, all
combined into a single shareable HTML report.
"""
import plotly.graph_objects as go
from plotly.subplots import make_subplots


class ResultsVisualizer:
    """Small helper class for building the Plotly figures used throughout
    this course: image grids, heatmaps, and line charts.
    """

    def image_grid(self, images, titles=None, **kwargs):
        """Arrange images side by side in a single figure."""
        if titles is None:
            titles = [f"Image {i + 1}" for i in range(len(images))]

        suptitle = kwargs.get("suptitle", "")
        height = kwargs.get("height", 350)

        fig = make_subplots(rows=1, cols=len(images), subplot_titles=titles)

        for col, image in enumerate(images, start=1):
            fig.add_trace(go.Image(z=image), row=1, col=col)

        fig.update_layout(title_text=suptitle, height=height)
        return fig

    def heatmap(self, matrix, **kwargs):
        """Display a 2D numeric array as a heatmap."""
        title = kwargs.get("title", "")
        colorscale = kwargs.get("colorscale", "Viridis")

        fig = go.Figure(go.Heatmap(z=matrix, colorscale=colorscale))
        fig.update_layout(title_text=title)
        return fig

    def line_chart(self, x, series, **kwargs):
        """Plot one or more named series against a shared x-axis."""
        title = kwargs.get("title", "")
        xaxis_title = kwargs.get("xaxis_title", "x")
        yaxis_title = kwargs.get("yaxis_title", "y")

        fig = go.Figure()

        for name, y in series.items():
            fig.add_trace(go.Scatter(x=x, y=y, mode="lines", name=name))

        fig.update_layout(
            title_text=title,
            xaxis_title=xaxis_title,
            yaxis_title=yaxis_title,
        )
        return fig