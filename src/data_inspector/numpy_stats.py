import numpy as np


def calculate_mean(data: list[float]) -> float:
    return float(np.mean(data))


def calculate_median(data: list[float]) -> float:
    return float(np.median(data))


def calculate_variance(data: list[float]) -> float:
    return float(np.var(data))


def calculate_stdv(data: list[float]) -> float:
    return float(np.std(data))


def calculate_quantile(data: list[float], q: float) -> float:
    return float(np.quantile(data, q))


def calculate_min_max_scale(data: list[float]) -> list[float]:
    array = np.array(data)
    scaled_array = (array - np.min(array))/(np.max(array)-np.min(array))
    return scaled_array.tolist()


def standardize(data: list[float]) -> list[float]:
    array = np.array(data)
    standardized_array = (array - np.mean(array)) / np.std(array)
    return standardized_array.tolist()


def train_test_split(data: list[float], test_ratio: float = 0.2, seed: int = None) -> tuple[list[float], list[float]]:
    array = np.array(data)

    if seed is not None:
        np.random.seed(seed)

    np.random.shuffle(array)

    split_index = int(len(array) * (1-test_ratio))

    train = array[:split_index].tolist()
    test = array[split_index:].tolist()

    return train, test
