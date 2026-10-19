import pytest
from data_inspector.stats import calculate_mean, calculate_median,calculate_variance,calculate_stdv,calculate_quantile,calculate_z_scores,min_max_scale,standardize,train_test_split 

def test_calculate_mean():
    assert calculate_mean([1.0, 2.0, 3.0, 4.0, 5.0]) == 3.0
    with pytest.raises(ValueError):
        calculate_mean([])


def test_calculate_median():
    assert calculate_median([5.0, 1.0, 3.0]) == 3.0
    assert calculate_median([4.0, 1.0, 2.0, 3.0]) == 2.5

    with pytest.raises(ValueError):
        calculate_median([])
def test_calculate_variance():
    # Mean is 3.0. Squared differences are 4, 1, 0, 1, 4. Average of those is 2.0.
    assert calculate_variance([1.0, 2.0, 3.0, 4.0, 5.0]) == 2.0
    
    with pytest.raises(ValueError):
        calculate_variance([])

def test_calculate_stdv():
    # Square root of 2.0 is roughly 1.41421356
    assert calculate_stdv([1.0, 2.0, 3.0, 4.0, 5.0]) == pytest.approx(1.41421356)
    
    with pytest.raises(ValueError):
        calculate_stdv([])

def test_calculate_quantile():
    data = [10.0, 20.0, 30.0, 40.0]
    
    # 50th percentile (Median)
    assert calculate_quantile(data, 0.5) == 25.0
    
    # 25th percentile
    assert calculate_quantile(data, 0.25) == 17.5
    
    # 100th percentile (Maximum edge case)
    assert calculate_quantile(data, 1.0) == 40.0
    
    # Error checking
    with pytest.raises(ValueError):
        calculate_quantile([], 0.5)
        
    with pytest.raises(ValueError):
        calculate_quantile(data, 1.5)  # Out of bounds


def test_calculate_z_scores():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    z_scores = calculate_z_scores(data)
    
    # The mean is 3.0, so the 3rd item (index 2) should have a z-score of 0.0
    assert z_scores[2] == 0.0
    
    # Z-score of 5.0 is (5.0 - 3.0) / 1.41421356
    assert z_scores[4] == pytest.approx(1.41421356)
    
    with pytest.raises(ValueError):
        calculate_z_scores([])
        
    with pytest.raises(ValueError):
        # A list of identical numbers has a standard deviation of 0
        calculate_z_scores([5.0, 5.0, 5.0])

def test_min_max_scale():
    data = [10.0, 20.0, 30.0, 40.0, 50.0]
    scaled = min_max_scale(data)
    
    # 10.0 becomes 0.0, 50.0 becomes 1.0, and 30.0 is exactly in the middle (0.5)
    assert scaled[0] == 0.0
    assert scaled[2] == 0.5
    assert scaled[4] == 1.0
    
    with pytest.raises(ValueError):
        min_max_scale([])
        
    with pytest.raises(ValueError):
        min_max_scale([5.0, 5.0, 5.0])

def test_standardize():
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    std_data = standardize(data)
    assert std_data[2] == 0.0  # The mean (3.0) should become exactly 0.0

def test_train_test_split():
    data = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]
    
    # Using a seed guarantees the random shuffle is exactly the same every time
    train, test = train_test_split(data, test_ratio=0.2, seed=42)
    
    assert len(train) == 8
    assert len(test) == 2
    
    # Ensure no data was lost or duplicated
    assert set(train).isdisjoint(set(test))
    assert len(set(train).union(set(test))) == 10

