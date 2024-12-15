
from setuptools import setup, find_packages

setup(
    name="car-sickness-detection",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "opencv-python",
        "mediapipe",
        "numpy",
        "scipy",
        "tensorflow",
    ],
)
