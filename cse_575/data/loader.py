# python
from argparse import Namespace


#pypi
import attr
import numpy
import scipy.io


from .common import Environment


Keys = Namespace(
    images = "target_img",
)


@attr.s(auto_attribs=True)
class RawData:
    """Loads and holds the raw data"""
    _environment: Environment = None
    _zero_train_images: numpy.array = None
    _zero_test_images: numpy.array = None
    _one_train_images: numpy.array = None
    _one_test_images: numpy.array = None

    @property
    def environment(self) -> Environment:
        """The environment paths"""
        if self._environment is None:
            self._environment = Environment()
            return self._environment

    @property
    def zero_train_images(self) -> numpy.array:
        """The training images for the digit zero"""
        if self._zero_train_images is None:
            self._zero_train_images = scipy.io.loadmat(self.environment.zero_train_images)[Keys.images]
        return self._zero_train_images

    @property
    def zero_test_images(self) -> numpy.array:
        """The testing images for the digit zero"""
        if self._zero_test_images is None:
            self._zero_test_images = scipy.io.loadmat(self.environment.zero_test_images)[Keys.images]
        return self._zero_test_images

    @property
    def one_train_images(self) -> numpy.array:
        """The training images for the digit one"""
        if self._one_train_images is None:
            self._one_train_images = scipy.io.loadmat(self.environment.one_train_images)[Keys.images]
        return self._one_train_images

    @property
    def one_test_images(self) -> numpy.array:
        """The testing images for the digit one"""
        if self._one_test_images is None:
            self._one_test_images = scipy.io.loadmat(self.environment.one_test_images)[Keys.images]
        return self._one_test_images
