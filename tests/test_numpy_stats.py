import pytest
from src.data_inspector.numpy_stats import (
    calculate_mean, calculate_median, calculate_variance,
    calculate_stdv, calculate_quantile, calculate_min_max_scale,
    standardize, train_test_split
)


def test_calculate_mean():
    assert calculate_mean([1.0, 2.0, 3.0]) == 2.0


def test_calculate_median():
    # Median should find the middle value regardless of order
    assert calculate_median([1.0, 100.0, 2.0]) == 2.0


def test_calculate_variance():
    # For [1.0, 5.0], mean is 3.0. Variance is ((1-3)^2 + (5-3)^2)/2 = 4.0
    assert calculate_variance([1.0, 5.0]) == 4.0


def test_calculate_stdv():
    # Std dev is the square root of variance (sqrt of 4.0 is 2.0)
    assert calculate_stdv([1.0, 5.0]) == 2.0


def test_calculate_quantile():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    assert calculate_quantile(data, 0.5) == 3.0  # 50th percentile (median)
    assert calculate_quantile(data, 0.25) == 2.0  # 25th percentile


def test_calculate_min_max_scale():
    result = calculate_min_max_scale([0.0, 5.0, 10.0])
    assert result == [0.0, 0.5, 1.0]


def test_standardize():
    result = standardize([1.0, 2.0, 3.0])
    # The mean is 2.0, so the middle element should become exactly 0.0
    assert round(result[1], 1) == 0.0
    # The first element should be negative since it's below the mean
    assert result[0] < 0.0


def test_train_test_split():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    train, test = train_test_split(data, test_ratio=0.2, seed=42)

    assert len(train) == 4
    assert len(test) == 1

    # Verify the seed actually locks the randomness
    train2, test2 = train_test_split(data, test_ratio=0.2, seed=42)
    assert train == train2

