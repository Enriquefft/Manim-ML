"""Reproducibility tests for data generation.

Verifies that data generation is deterministic and produces
identical outputs across multiple runs (FR-004, SC-007).
"""

from __future__ import annotations

import tempfile
from pathlib import Path

from src.config import (
    DATA_SEED,
    LINEAR_DATA_POINTS,
    LINEAR_SLOPE,
    NEURAL_NETWORK_MIN_NODES,
    NONLINEAR_DATA_POINTS,
)
from src.utils.data_generator import (
    DataPoint,
    ErrorBar,
    RegressionLine,
    create_error_bars,
    fit_linear_regression,
    fit_polynomial_regression,
    generate_linear_data,
    generate_neural_network,
    generate_scurve_data,
    load_data_from_csv,
    save_data_to_csv,
)


class TestDataPointCreation:
    """Test DataPoint dataclass."""

    def test_create_data_point(self) -> None:
        """Verify DataPoint can be created with x, y coordinates."""
        point = DataPoint(x=1.0, y=2.0)
        assert point.x == 1.0
        assert point.y == 2.0

    def test_default_color(self) -> None:
        """Verify DataPoint has default white color."""
        point = DataPoint(x=1.0, y=2.0)
        assert point.color == "#F2F2F2"

    def test_custom_color(self) -> None:
        """Verify DataPoint accepts custom color."""
        point = DataPoint(x=1.0, y=2.0, color="#00F0FF")
        assert point.color == "#00F0FF"


class TestRegressionLine:
    """Test RegressionLine dataclass."""

    def test_linear_equation_str(self) -> None:
        """Verify linear equation string generation."""
        line = RegressionLine(
            line_type="linear",
            coefficients=(1.05, 1.0),
        )
        assert line.equation_str == "y = 1.05x + 1.00"

    def test_linear_predict(self) -> None:
        """Verify linear prediction calculation."""
        line = RegressionLine(
            line_type="linear",
            coefficients=(2.0, 3.0),
        )
        # y = 2*x + 3
        assert line.predict(0) == 3.0
        assert line.predict(1) == 5.0
        assert line.predict(5) == 13.0

    def test_polynomial_predict(self) -> None:
        """Verify polynomial prediction calculation."""
        line = RegressionLine(
            line_type="polynomial",
            coefficients=(1.0, 0.0, 1.0),  # y = 1 + 0*x + 1*x^2 = 1 + x^2
        )
        assert line.predict(0) == 1.0
        assert line.predict(1) == 2.0
        assert line.predict(2) == 5.0


class TestErrorBar:
    """Test ErrorBar dataclass."""

    def test_residual_calculation(self) -> None:
        """Verify residual is calculated correctly."""
        point = DataPoint(x=1.0, y=5.0)
        error_bar = ErrorBar(data_point=point, predicted_y=4.0)
        assert error_bar.residual == 1.0  # 5.0 - 4.0

    def test_negative_residual(self) -> None:
        """Verify negative residual when point below line."""
        point = DataPoint(x=1.0, y=3.0)
        error_bar = ErrorBar(data_point=point, predicted_y=4.0)
        assert error_bar.residual == -1.0


class TestLinearDataGeneration:
    """Test linear data generation reproducibility."""

    def test_generates_correct_number_of_points(self) -> None:
        """Verify correct number of points generated."""
        data = generate_linear_data()
        assert len(data) == LINEAR_DATA_POINTS

    def test_reproducibility_same_seed(self) -> None:
        """Verify identical output with same seed (FR-004, SC-007)."""
        data1 = generate_linear_data(seed=DATA_SEED)
        data2 = generate_linear_data(seed=DATA_SEED)

        assert len(data1) == len(data2)
        for p1, p2 in zip(data1, data2, strict=True):
            assert p1.x == p2.x
            assert p1.y == p2.y

    def test_different_seed_produces_different_data(self) -> None:
        """Verify different seeds produce different data."""
        data1 = generate_linear_data(seed=42)
        data2 = generate_linear_data(seed=123)

        # At least some points should be different
        different = any(p1.x != p2.x or p1.y != p2.y for p1, p2 in zip(data1, data2, strict=True))
        assert different

    def test_data_follows_linear_trend(self) -> None:
        """Verify data approximately follows y = slope*x + intercept."""
        data = generate_linear_data(noise_std=0)  # No noise for testing

        # Check trend by comparing first and last points
        x_range = data[-1].x - data[0].x
        y_range = data[-1].y - data[0].y
        approx_slope = y_range / x_range

        # Should be close to configured slope
        assert abs(approx_slope - LINEAR_SLOPE) < 0.5


class TestScurveDataGeneration:
    """Test S-curve data generation reproducibility."""

    def test_generates_correct_number_of_points(self) -> None:
        """Verify correct number of points generated."""
        data = generate_scurve_data()
        assert len(data) == NONLINEAR_DATA_POINTS

    def test_reproducibility_same_seed(self) -> None:
        """Verify identical output with same seed (FR-004, SC-007)."""
        data1 = generate_scurve_data(seed=DATA_SEED)
        data2 = generate_scurve_data(seed=DATA_SEED)

        assert len(data1) == len(data2)
        for p1, p2 in zip(data1, data2, strict=True):
            assert p1.x == p2.x
            assert p1.y == p2.y


class TestCsvPersistence:
    """Test CSV save/load functionality."""

    def test_save_and_load_roundtrip(self) -> None:
        """Verify data survives CSV save/load cycle."""
        original = [
            DataPoint(x=1.0, y=2.0),
            DataPoint(x=3.0, y=4.0),
            DataPoint(x=5.0, y=6.0),
        ]

        with tempfile.TemporaryDirectory() as tmpdir:
            filepath = Path(tmpdir) / "test_data.csv"
            save_data_to_csv(original, filepath)
            loaded = load_data_from_csv(filepath)

        assert len(loaded) == len(original)
        for orig, load in zip(original, loaded, strict=True):
            assert abs(orig.x - load.x) < 1e-10
            assert abs(orig.y - load.y) < 1e-10

    def test_load_existing_data_files(self) -> None:
        """Verify pre-generated data files can be loaded."""
        linear_path = Path("videos/assets/data/linear_data.csv")
        nonlinear_path = Path("videos/assets/data/nonlinear_data.csv")

        if linear_path.exists():
            linear_data = load_data_from_csv(linear_path)
            assert len(linear_data) == LINEAR_DATA_POINTS

        if nonlinear_path.exists():
            nonlinear_data = load_data_from_csv(nonlinear_path)
            assert len(nonlinear_data) >= NONLINEAR_DATA_POINTS


class TestRegressionFitting:
    """Test regression fitting functions."""

    def test_fit_linear_regression(self) -> None:
        """Verify linear regression fitting."""
        # Perfect linear data
        points = [
            DataPoint(x=1.0, y=3.0),
            DataPoint(x=2.0, y=5.0),
            DataPoint(x=3.0, y=7.0),
        ]
        regression = fit_linear_regression(points)

        assert regression.line_type == "linear"
        assert len(regression.coefficients) == 2
        # y = 2x + 1
        assert abs(regression.coefficients[0] - 2.0) < 0.01
        assert abs(regression.coefficients[1] - 1.0) < 0.01

    def test_fit_polynomial_regression(self) -> None:
        """Verify polynomial regression fitting."""
        points = [
            DataPoint(x=0.0, y=1.0),
            DataPoint(x=1.0, y=2.0),
            DataPoint(x=2.0, y=5.0),
        ]
        regression = fit_polynomial_regression(points, degree=2)

        assert regression.line_type == "polynomial"
        assert len(regression.coefficients) == 3


class TestErrorBarCreation:
    """Test error bar creation."""

    def test_create_error_bars(self) -> None:
        """Verify error bars are created for all points."""
        points = [
            DataPoint(x=1.0, y=3.0),
            DataPoint(x=2.0, y=5.0),
        ]
        regression = RegressionLine(
            line_type="linear",
            coefficients=(2.0, 1.0),  # y = 2x + 1
        )

        error_bars = create_error_bars(points, regression)

        assert len(error_bars) == 2
        # First point: actual y=3, predicted y=2*1+1=3, residual=0
        assert abs(error_bars[0].residual) < 0.01
        # Second point: actual y=5, predicted y=2*2+1=5, residual=0
        assert abs(error_bars[1].residual) < 0.01


class TestNeuralNetworkGeneration:
    """Test neural network structure generation."""

    def test_generates_minimum_nodes(self) -> None:
        """Verify network has at least 1000 nodes (FR-010)."""
        network = generate_neural_network()
        assert network.node_count >= NEURAL_NETWORK_MIN_NODES

    def test_custom_layer_sizes(self) -> None:
        """Verify custom layer sizes work."""
        layer_sizes = [10, 20, 30, 20, 10]
        network = generate_neural_network(layer_sizes=layer_sizes, min_nodes=0)
        assert network.node_count == sum(layer_sizes)

    def test_connections_between_layers(self) -> None:
        """Verify connections exist between adjacent layers."""
        network = generate_neural_network(layer_sizes=[5, 10, 5], min_nodes=0)
        assert len(network.connections) > 0

    def test_layer_sizes_stored(self) -> None:
        """Verify layer sizes are stored in network."""
        layer_sizes = [10, 20, 10]
        network = generate_neural_network(layer_sizes=layer_sizes, min_nodes=0)
        assert network.layer_sizes == layer_sizes
