import numpy as np


def give_bmi(
    height: list[int | float], weight: list[int | float]
) -> list[int | float]:
    height_array = np.array(height, dtype=float)
    weight_array = np.array(weight, dtype=float)

    if height_array.shape[0] != weight_array.shape[0]:
        raise ValueError("Height and weight lists must have the same length.")

    bmi_values = np.where(
        height_array != 0, weight_array / (height_array**2), float("inf")
    )

    return bmi_values.tolist()


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi_array = np.array(bmi, dtype=float)

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer")

    return (bmi_array > limit).tolist()
