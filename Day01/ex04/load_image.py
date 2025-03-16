from PIL import Image
import numpy as np


def load_image(path: str) -> np.ndarray | None:
    """Load an image from the given path and return it as a NumPy array."""
    try:
        with Image.open(path) as image:
            image_array = np.array(image)
            print(f'The shape of the image is: {image_array.shape}')
            print(image_array)
            return image_array
    except Exception as e:
        print(f'Error loading image: {e}')
        return None
