# Digital Image Processing

This repository contains Python scripts for various digital image processing tasks, including filtering, transformations, color manipulations, and histogram analysis.

## Directory Structure

```
.
├── array_histogram.py
├── array_neg_image.py
├── color_image_histogram.py
├── convolution.py
├── gamma_transformation.py
├── green_red_blue_pixel.py
├── image_90_degree_rotation.py
├── image_neg_image_curve.py
├── image_pixel_range.py
├── image_resize.py
├── log_transformation.py
├── separate_green_red_blue.py
├── smoothing_gaussian.py
├── smoothing_meanfilter.py
├── smoothing_weighted_averaging.py
├── test.py
├── images/
│   ├── face grayscale.jpg
│   ├── RGB_image.jpg
│   └── WhatsApp Image 2025-08-26 at 10.18.59_33b78b87.jpg
```

## Scripts Overview

- **array_histogram.py**: Manual histogram calculation for grayscale images.
- **array_neg_image.py**: Negative transformation on a grayscale array.
- **color_image_histogram.py**: Histogram for each color channel in an RGB image.
- **convolution.py**: Manual and built-in convolution on a sample array.
- **gamma_transformation.py**: Gamma correction with various gamma values.
- **green_red_blue_pixel.py**: Filtering image pixels by color range.
- **image_90_degree_rotation.py**: Manual 90-degree rotation (clockwise/anticlockwise) of an image.
- **image_neg_image_curve.py**: Negative transformation and its curve.
- **image_pixel_range.py**: Filtering pixels within a specific color range.
- **image_resize.py**: Manual resizing of an image using nearest-neighbor interpolation.
- **log_transformation.py**: Logarithmic transformation and its curve.
- **separate_green_red_blue.py**: Separates and displays red, green, and blue channels.
- **smoothing_gaussian.py**: Gaussian smoothing (manual and built-in).
- **smoothing_meanfilter.py**: Mean filter smoothing (manual and built-in).
- **smoothing_weighted_averaging.py**: Weighted averaging filter (manual and built-in).

## Requirements

- Python 3.x
- numpy
- matplotlib
- Pillow
- opencv-python

Install dependencies with:
```sh
pip install numpy matplotlib pillow opencv-python
```

## Usage

Each script can be run independently. For example:
```sh
python color_image_histogram.py
```

## Images

Sample images are located in the `images/` directory. Update the image paths in scripts if needed.

---

**Author:**  
*Tamima Azad*  
**Course Code:** CSE-3216  
**Course Title:** Digital Image Processing Sessional
