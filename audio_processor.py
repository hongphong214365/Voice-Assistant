"""Các phép đo tín hiệu audio độc lập với thiết bị thu âm."""

import numpy as np


def calculate_rms(data: np.ndarray) -> float:
    """Tính RMS theo đơn vị biên độ của mẫu audio đầu vào.

    Chuyển mẫu sang float32 trước khi bình phương để tránh tràn số với int16.
    Mảng rỗng không có RMS xác định nên được báo lỗi rõ ràng.
    """
    samples = np.asarray(data, dtype=np.float32)
    if samples.size == 0:
        raise ValueError("Không thể tính RMS cho audio rỗng")

    return float(np.sqrt(np.mean(np.square(samples), dtype=np.float32)))
