from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    try:
        with Image.open(path) as image:
            image_array = np.array(image)
            print(f'The shape of the image is: {image_array.shape}')
            return image_array
    except Exception as e:
        print(f'Error: {e}')
        return None
