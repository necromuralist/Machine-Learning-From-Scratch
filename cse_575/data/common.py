# from python
from argparse import Namespace
from pathlib import Path

import os

# from pypi
from dotenv import load_dotenv

import attr

Keys = Namespace(
    raw_data = "RAW_DATA",
    zero_train_images = "ZERO_TRAIN_IMAGES",
    zero_test_images = "ZERO_TEST_IMAGES",
    one_test_images = "ONE_TEST_IMAGES",
    one_train_images = "ONE_TRAIN_IMAGES",
)


@attr.s(auto_attribs=True)
class Environment:
    """Loads the environment variables"""
    _raw_data_folder = None
    _zero_train_images = None
    _zero_test_images = None
    _one_train_images = None
    _one_test_images = None
    _environment = None

    @property
    def environment(self) -> dict:
        """The environment dictionary"""
        if self._environment is None:
            load_dotenv(override=True)
            self._environment = os.environ
        return self._environment

    @property
    def raw_data_folder(self) -> Path:
        """The path to the raw data folder"""
        if self._raw_data_folder is None:
            self._raw_data_folder = Path(self.environment[Keys.raw_data]).expanduser()
        return self._raw_data_folder

    @property
    def zero_train_images(self) -> Path:
        """the path to the train images for Zero"""
        if self._zero_train_images is None:
            self._zero_train_images = Path(
                self.environment[Keys.zero_train_images]).expanduser()
        return self._zero_train_images

    @property
    def zero_test_images(self) -> Path:
        """the path to the test images for Zero"""
        if self._zero_test_images is None:
            self._zero_test_images = Path(
                self.environment[Keys.zero_test_images]).expanduser()
        return self._zero_test_images

    @property
    def one_train_images(self) -> Path:
        """the path to the train images for one"""
        if self._one_train_images is None:
            self._one_train_images = Path(
                self.environment[Keys.one_train_images]).expanduser()
        return self._one_train_images

    @property
    def one_test_images(self) -> Path:
        """the path to the test images for one"""
        if self._one_test_images is None:
            self._one_test_images = Path(
                self.environment[Keys.one_test_images]).expanduser()
        return self._one_test_images
