"""Data generation utilities for regression scene visualizations.

Provides reproducible data generation using seeded random number generation.
All data is generated with seed=42 to ensure identical outputs across renders,
satisfying FR-004 reproducibility requirement.
"""

from __future__ import annotations

import csv
from dataclasses import dataclass
from pathlib import Path
from typing import TYPE_CHECKING

import numpy as np

from src.config import (
    DATA_SEED,
    LINEAR_DATA_POINTS,
    LINEAR_INTERCEPT,
    LINEAR_NOISE_STD,
    LINEAR_SLOPE,
    NONLINEAR_DATA_POINTS,
)

if TYPE_CHECKING:
    from numpy.random import Generator


@dataclass(frozen=True)
class DataPoint:
    """Represents a single observation on the regression graph.

    Attributes:
        x: X-coordinate (input variable)
        y: Y-coordinate (output variable)
        color: Visual color as hex string (default: white)

    """

    x: float
    y: float
    color: str = "#F2F2F2"


@dataclass(frozen=True)
class RegressionLine:
    """Mathematical model fitted to data.

    Attributes:
        line_type: Model type ("linear" or "polynomial")
        coefficients: Model parameters (slope, intercept for linear;
                     coefficients for polynomial in ascending degree order)
        color: Visual color as hex string (default: cyan)

    """

    line_type: str
    coefficients: tuple[float, ...]
    color: str = "#00F0FF"

    @property
    def equation_str(self) -> str:
        """Generate LaTeX representation of the equation.

        Returns:
            LaTeX string for the regression equation

        """
        if self.line_type == "linear" and len(self.coefficients) == 2:
            slope, intercept = self.coefficients
            return f"y = {slope:.2f}x + {intercept:.2f}"
        if self.line_type == "polynomial":
            terms = []
            for i, coef in enumerate(self.coefficients):
                if i == 0:
                    terms.append(f"{coef:.2f}")
                elif i == 1:
                    terms.append(f"{coef:.2f}x")
                else:
                    terms.append(f"{coef:.2f}x^{i}")
            return "y = " + " + ".join(terms)
        return "y = f(x)"

    def predict(self, x: float) -> float:
        """Calculate y for a given x value.

        Args:
            x: Input x value

        Returns:
            Predicted y value from the model

        """
        if self.line_type == "linear" and len(self.coefficients) == 2:
            slope, intercept = self.coefficients
            return slope * x + intercept
        if self.line_type == "polynomial":
            return float(
                sum(coef * (x**i) for i, coef in enumerate(self.coefficients)),
            )
        return 0.0


@dataclass(frozen=True)
class ErrorBar:
    """Residual visualization connecting data point to regression line.

    Attributes:
        data_point: Source observation
        predicted_y: Y-value on regression line at data_point.x
        color: Visual color as hex string (default: red)

    """

    data_point: DataPoint
    predicted_y: float
    color: str = "#FF2A2A"

    @property
    def residual(self) -> float:
        """Calculate the residual (actual - predicted).

        Returns:
            The vertical distance from data point to regression line

        """
        return self.data_point.y - self.predicted_y


@dataclass(frozen=True)
class NetworkNode:
    """Single neuron in the neural network visualization.

    Attributes:
        x: X position on screen
        y: Y position on screen
        layer: Network layer index (0-based)
        color: Visual color as hex string (default: cyan)
        radius: Node size (default: 0.02)

    """

    x: float
    y: float
    layer: int
    color: str = "#00F0FF"
    radius: float = 0.02


@dataclass(frozen=True)
class NetworkConnection:
    """Edge between two network nodes.

    Attributes:
        source: Origin node
        target: Destination node
        opacity: Visual transparency (0.0-1.0)
        color: Line color as hex string (default: cyan)

    """

    source: NetworkNode
    target: NetworkNode
    opacity: float = 0.1
    color: str = "#00F0FF"


@dataclass
class NeuralNetwork:
    """Complete network structure for Section 5 visualization.

    Attributes:
        nodes: All neurons in the network
        connections: All edges between neurons
        layer_sizes: Number of nodes per layer

    """

    nodes: list[NetworkNode]
    connections: list[NetworkConnection]
    layer_sizes: list[int]

    @property
    def node_count(self) -> int:
        """Get total number of nodes in the network."""
        return len(self.nodes)


def _get_rng(seed: int | None = None) -> Generator:
    """Create a reproducible random number generator.

    Args:
        seed: Random seed (defaults to DATA_SEED from config)

    Returns:
        NumPy Generator instance

    """
    return np.random.default_rng(seed if seed is not None else DATA_SEED)


def generate_linear_data(
    n_points: int = LINEAR_DATA_POINTS,
    slope: float = LINEAR_SLOPE,
    intercept: float = LINEAR_INTERCEPT,
    noise_std: float = LINEAR_NOISE_STD,
    seed: int = DATA_SEED,
) -> list[DataPoint]:
    """Generate linear trend data with noise.

    Creates data points following y = slope * x + intercept + noise,
    where noise is drawn from a normal distribution.

    Args:
        n_points: Number of data points to generate
        slope: True slope of the linear relationship
        intercept: True y-intercept
        noise_std: Standard deviation of Gaussian noise
        seed: Random seed for reproducibility

    Returns:
        List of DataPoint objects with generated coordinates

    """
    rng = _get_rng(seed)

    # Generate evenly spaced x values from 1 to 10
    x_values = np.linspace(1.0, 10.0, n_points)

    # Add some jitter to x positions for natural look
    x_jitter = rng.normal(0, 0.1, n_points)
    x_values = x_values + x_jitter

    # Generate y values with noise
    noise = rng.normal(0, noise_std, n_points)
    y_values = slope * x_values + intercept + noise

    return [DataPoint(x=float(x), y=float(y)) for x, y in zip(x_values, y_values, strict=True)]


def generate_scurve_data(
    n_points: int = NONLINEAR_DATA_POINTS,
    seed: int = DATA_SEED,
) -> list[DataPoint]:
    """Generate S-curve pattern data (rise, plateau, crash).

    Creates data points following a sigmoid-like pattern that
    demonstrates non-linear behavior unsuitable for linear regression.

    Args:
        n_points: Number of data points to generate
        seed: Random seed for reproducibility

    Returns:
        List of DataPoint objects with S-curve coordinates

    """
    rng = _get_rng(seed)

    # Generate x values across the curve
    x_values = np.linspace(0.0, 10.0, n_points)

    # S-curve function: steep rise, plateau, then crash
    # Using a combination of tanh and polynomial
    y_base = np.zeros(n_points)

    for i, x in enumerate(x_values):
        if x < 3:
            # Initial rise phase
            y_base[i] = 0.5 + 0.5 * np.tanh((x - 1.5) * 1.5)
        elif x < 7:
            # Plateau phase with slight wobble
            y_base[i] = 1.0 + 0.1 * np.sin(x * 2)
        else:
            # Crash phase
            y_base[i] = 1.0 - 0.3 * (x - 7) ** 2

    # Scale to reasonable y range
    y_values = y_base * 5 + 2

    # Add noise
    noise = rng.normal(0, 0.2, n_points)
    y_values = y_values + noise

    return [DataPoint(x=float(x), y=float(y)) for x, y in zip(x_values, y_values, strict=True)]


def save_data_to_csv(points: list[DataPoint], filepath: str | Path) -> None:
    """Save data points to CSV file.

    Args:
        points: List of DataPoint objects to save
        filepath: Output file path

    """
    filepath = Path(filepath)
    filepath.parent.mkdir(parents=True, exist_ok=True)

    with filepath.open("w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["x", "y"])
        for point in points:
            writer.writerow([point.x, point.y])


def load_data_from_csv(filepath: str | Path) -> list[DataPoint]:
    """Load data points from CSV file.

    Args:
        filepath: Input file path

    Returns:
        List of DataPoint objects loaded from file

    Raises:
        FileNotFoundError: If the file does not exist

    """
    filepath = Path(filepath)

    points: list[DataPoint] = []
    with filepath.open() as f:
        reader = csv.DictReader(f)
        for row in reader:
            points.append(DataPoint(x=float(row["x"]), y=float(row["y"])))

    return points


def fit_linear_regression(points: list[DataPoint]) -> RegressionLine:
    """Fit a linear regression model to data points.

    Uses least squares to find the best-fit line y = mx + b.

    Args:
        points: List of data points to fit

    Returns:
        RegressionLine with fitted slope and intercept

    """
    x_values = np.array([p.x for p in points])
    y_values = np.array([p.y for p in points])

    # Least squares: y = mx + b
    # Using numpy polyfit for degree 1
    coefficients = np.polyfit(x_values, y_values, 1)
    slope = float(coefficients[0])
    intercept = float(coefficients[1])

    return RegressionLine(
        line_type="linear",
        coefficients=(slope, intercept),
    )


def fit_polynomial_regression(
    points: list[DataPoint],
    degree: int = 3,
) -> RegressionLine:
    """Fit a polynomial regression model to data points.

    Args:
        points: List of data points to fit
        degree: Polynomial degree (default: 3 for cubic)

    Returns:
        RegressionLine with fitted polynomial coefficients

    """
    x_values = np.array([p.x for p in points])
    y_values = np.array([p.y for p in points])

    # Fit polynomial
    coefficients = np.polyfit(x_values, y_values, degree)

    # Reverse to get ascending degree order
    coefficients = tuple(reversed(coefficients.tolist()))

    return RegressionLine(
        line_type="polynomial",
        coefficients=coefficients,
    )


def create_error_bars(
    points: list[DataPoint],
    regression: RegressionLine,
) -> list[ErrorBar]:
    """Create error bar visualizations for data points.

    Args:
        points: List of data points
        regression: Fitted regression model

    Returns:
        List of ErrorBar objects for each data point

    """
    return [
        ErrorBar(
            data_point=point,
            predicted_y=regression.predict(point.x),
        )
        for point in points
    ]


def generate_neural_network(
    layer_sizes: list[int] | None = None,
    min_nodes: int = 1000,
) -> NeuralNetwork:
    """Generate a neural network structure for visualization.

    Creates a layered network with specified layer sizes. If layer_sizes
    is not provided, generates a network with at least min_nodes nodes.

    Args:
        layer_sizes: List of node counts per layer
        min_nodes: Minimum total node count (FR-010 requires >= 1000)

    Returns:
        NeuralNetwork with nodes and connections

    """
    if layer_sizes is None:
        # Default structure to meet 1000+ node requirement
        # 5 layers: 50 -> 200 -> 400 -> 250 -> 100 = 1000 nodes
        layer_sizes = [50, 200, 400, 250, 100]

    total_nodes = sum(layer_sizes)
    if total_nodes < min_nodes:
        # Scale up to meet minimum
        scale_factor = (min_nodes // total_nodes) + 1
        layer_sizes = [size * scale_factor for size in layer_sizes]

    nodes: list[NetworkNode] = []
    connections: list[NetworkConnection] = []

    # Calculate positions for each layer
    num_layers = len(layer_sizes)
    layer_spacing = 14.0 / (num_layers + 1)  # Spread across screen width

    for layer_idx, layer_size in enumerate(layer_sizes):
        x_pos = -7.0 + (layer_idx + 1) * layer_spacing
        node_spacing = 8.0 / (layer_size + 1) if layer_size > 1 else 0

        for node_idx in range(layer_size):
            y_pos = -4.0 + (node_idx + 1) * node_spacing
            nodes.append(
                NetworkNode(
                    x=x_pos,
                    y=y_pos,
                    layer=layer_idx,
                ),
            )

    # Create connections between adjacent layers
    node_offset = 0
    for layer_idx in range(num_layers - 1):
        current_layer_size = layer_sizes[layer_idx]
        next_layer_size = layer_sizes[layer_idx + 1]

        # Connect each node to a subset of next layer (for performance)
        max_connections_per_node = min(10, next_layer_size)

        for i in range(current_layer_size):
            source_node = nodes[node_offset + i]

            # Connect to evenly distributed nodes in next layer
            step = max(1, next_layer_size // max_connections_per_node)
            for j in range(0, next_layer_size, step):
                target_node = nodes[node_offset + current_layer_size + j]
                connections.append(
                    NetworkConnection(
                        source=source_node,
                        target=target_node,
                        opacity=0.05,  # Very low opacity for many connections
                    ),
                )

        node_offset += current_layer_size

    return NeuralNetwork(
        nodes=nodes,
        connections=connections,
        layer_sizes=layer_sizes,
    )
