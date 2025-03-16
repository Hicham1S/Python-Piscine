import numpy as np
import matplotlib.pyplot as plt
from load_image import load_image


def zoom_image(image: np.ndarray, zoom_size: int = 400) -> np.ndarray | None:
    """
    Crop the center of the image to create a zoom effect.
    """
    try:
        height, width = image.shape[:2]
        if height < zoom_size or width < zoom_size:
            print("Error: Image is too small for the requested zoom size.")
            return None

        start_x = (width - zoom_size) // 2
        start_y = (height - zoom_size) // 2
        zoomed_image = image[start_y:start_y + zoom_size,
                             start_x:start_x + zoom_size]

        if zoomed_image.ndim == 3 and zoomed_image.shape[2] == 3:
            zoomed_image = zoomed_image[:, :, 0:1]
        print(f'New shape after slicing: {zoomed_image.shape}')
        print(zoomed_image)
        return zoomed_image
    except Exception as e:
        print(f"Error in zooming: {e}")
        return None


def display_image(image: np.ndarray):
    """
    Display the given image with x and y axis scales.

    Args:
        image (np.ndarray): The image to display.
    """
    try:
        image = np.transpose(image, (1, 0, 2))
        image = np.squeeze(image)
        plt.imshow(image, cmap='gray')
        plt.axis('off')
        plt.show()
    except Exception as e:
        print(f"Error displaying image: {e}")


def main():
    """Main function to load, zoom, and display an image."""
    path = "animal.jpeg"
    image = load_image(path)

    if image is not None:
        zoomed_image = zoom_image(image)
        if zoomed_image is not None:
            display_image(zoomed_image)


if __name__ == "__main__":
    main()
