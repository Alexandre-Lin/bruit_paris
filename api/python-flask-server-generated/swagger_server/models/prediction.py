# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server import util


class Prediction(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    def __init__(self, source: str=None, rate: float=None):  # noqa: E501
        """Prediction - a model defined in Swagger

        :param source: The source of this Prediction.  # noqa: E501
        :type source: str
        :param rate: The rate of this Prediction.  # noqa: E501
        :type rate: float
        """
        self.swagger_types = {
            'source': str,
            'rate': float
        }

        self.attribute_map = {
            'source': 'source',
            'rate': 'rate'
        }
        self._source = source
        self._rate = rate

    @classmethod
    def from_dict(cls, dikt) -> 'Prediction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Prediction of this Prediction.  # noqa: E501
        :rtype: Prediction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def source(self) -> str:
        """Gets the source of this Prediction.


        :return: The source of this Prediction.
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source: str):
        """Sets the source of this Prediction.


        :param source: The source of this Prediction.
        :type source: str
        """

        self._source = source

    @property
    def rate(self) -> float:
        """Gets the rate of this Prediction.


        :return: The rate of this Prediction.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate: float):
        """Sets the rate of this Prediction.


        :param rate: The rate of this Prediction.
        :type rate: float
        """

        self._rate = rate
