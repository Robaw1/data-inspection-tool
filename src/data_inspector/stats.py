import random


def calculate_mean(data: list[float]) -> float:
    # calculate the mean of the list of data
    if not data:
        raise ValueError("can not calculate the mean of an empty list!")
    total_sum = sum(data)
    count = len(data)

    return total_sum/count


def calculate_median(data: list[float]) -> float:
    # calculate the meadian of the list of the data
    if not data:
        raise ValueError("Cannot calculate the median of an empty list.")
    data = sorted(data)
    n = len(data)
    if n % 2 != 0:
        # odd so we take the value at the middle
        return data[n//2]
    if n % 2 == 0:
        # its even so we take the two values at the middle and take their average
        sum_of_medians = data[n//2] + data[(n//2)-1]
        return sum_of_medians/2


def calculate_variance(data: list[float]) -> float:
    if not data:
        raise ValueError("can't calculate variance for empty list!")
    mean_val = calculate_mean(data)
    squared_diffs = [(x-mean_val)**2 for x in data]
    return calculate_mean(squared_diffs)


def calculate_stdv(data: list[float]) -> float:
    variance = calculate_variance(data)
    return variance**0.5


def calculate_quantile(data: list[float], q: float) -> float:
    if not data:
        raise ValueError("can't calculate quantile with empty list")
    if not 0 <= q <= 1:
        raise ValueError("Quantile 'q' must be between 1 and 0")
    data = sorted(data)
    n = len(data)
    exact_index = q * (n-1)

    lower_index = int(exact_index)
    upper_index = lower_index + 1 if lower_index < n-1 else lower_index

    fraction = exact_index - lower_index

    return data[lower_index] + (data[upper_index] - data[lower_index])*fraction

def calculate_z_scores(data: list[float]) -> list[float]:
    if not data:
        raise ValueError("can't calculate z-score of an empty list")
    standard_dev = calculate_stdv(data)
    if standard_dev == 0:
        raise ValueError("Standard deviation is zero; can't calcualte z-score")
    mean_val = calculate_mean(data)
    return [(x-mean_val)/standard_dev for x in data]


def min_max_scale(data: list[float]) -> list[float]:
    if not data:
        raise ValueError("can't scale an empty list")
    min_val = min(data)
    max_val = max(data)
    range = max_val - min_val

    if range == 0:
        raise ValueError(
            "All values are identical; cannot calculate Min-Max scale.")

    return [(x - min_val) / range for x in data]


def standardize(data: list[float]) -> list[float]:
    return calculate_z_scores(data)


def train_test_split(data: list[float], test_ratio: float = 0.2, seed: int = None) -> tuple[list[float], list[float]]:
    if not data:
        raise ValueError("Cannot split an empty list.")
    if not 0.0 < test_ratio < 1.0:
        raise ValueError("Test ratio must be strictly between 0.0 and 1.0.")

    # Copy the data so we don't accidentally shuffle the original list
    shuffled_data = data.copy()

    if seed is not None:
        random.seed(seed)

    random.shuffle(shuffled_data)

    # Calculate exactly where to chop the list
    split_idx = int(len(shuffled_data) * (1 - test_ratio))

    train_data = shuffled_data[:split_idx]
    test_data = shuffled_data[split_idx:]

    return train_data, test_data
