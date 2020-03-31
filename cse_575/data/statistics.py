# from pypi
from argparse import Namespace


import attr
import numpy


ImageShape = Namespace(
    width = 0,
    height = 1,
    samples = 2,
)


Axes = Namespace(
    rows = 0,
    columns = 1,
)


@attr.s(auto_attribs=True)
class TheStatistician:
    """calculator of simple statistics
    
    Args:
     data: loaded dict of images to work with
    """
    data: dict
    _pixels: int = None
    _flattened: numpy.array = None
    _samples: int = None
    _means: numpy.array = None
    _variances: numpy.array = None

    @property
    def samples(self) -> int:
        """The number of images in the data"""
        if self._samples is None:
            self._samples = self.data.shape[ImageShape.samples]
        return self._samples

    @property
    def pixels(self) -> int:
        """The total number of pixels in the flattened image"""
        if self._pixels is None:
            shape = self.data.shape
            self._pixels = shape[ImageShape.height] * shape[ImageShape.width]
        return self._pixels

    @property
    def flattened(self) -> numpy.array:
        """a flattened view of the images"""
        if self._flattened is None:
            self._flattened = self.data.copy().flatten().reshape(
                self.pixels, self.samples).T
        return self._flattened

    @property
    def means(self) -> numpy.array:
        """The mean for each image"""
        if self._means is None:
            self._means = self.flattened.mean(axis=Axes.columns)
        return self._means

    @property
    def variances(self) -> numpy.array:
        """The mean row-variance for each image"""
        if self._variances is None:
            self._variances = self.data.var(axis=Axes.columns).mean(axis=Axes.rows)
        return self._variances
