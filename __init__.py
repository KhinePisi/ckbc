# -*- coding: utf-8 -*-

"""Get triples from the Ckbc dataset."""

import pathlib

from docdata import parse_docdata

from ..base import PathDataset
from ..literal_base import NumericPathDataset
from ...triples import TriplesNumericLiteralsFactory

__all__ = [
    "CKBC_TRAIN_PATH",
    "CKBC_TEST_PATH",
    "CKBC_VALIDATE_PATH",
    "CKBC_LITERALS_PATH",
    "CKBC",
    "CKBC",
]

HERE = pathlib.Path(__file__).resolve().parent

CKBC_TRAIN_PATH = HERE.joinpath("train.txt")
CKBC_TEST_PATH = HERE.joinpath("test.txt")
CKBC_VALIDATE_PATH = HERE.joinpath("valid.txt")
CKBC_LITERALS_PATH = HERE.joinpath("literals.txt")


@parse_docdata
class Ckbc(PathDataset):
    """The CKBC dataset.

    ---
    name: Ckbc
    statistics:
        entities: 14
        relations: 55
        training: 1592
        testing: 201
        validation: 199
        triples: 1992
    citation:
        author: Zhenfeng Lei
        year: 2017
        github: ZhenfengLei/KGDatasets
    """

    def __init__(self, create_inverse_triples: bool = False, **kwargs):
        """Initialize the Nations dataset.

        :param create_inverse_triples: Should inverse triples be created? Defaults to false.
        :param kwargs: keyword arguments passed to :class:`pykeen.datasets.base.PathDataset`.
        """
        super().__init__(
            training_path=CKBC_TRAIN_PATH,
            testing_path=CKBC_TEST_PATH,
            validation_path=CKBC_VALIDATE_PATH,
            create_inverse_triples=create_inverse_triples,
            **kwargs,
        )


class CkbcLiteral(NumericPathDataset):
    """The Nations dataset with literals."""

    training: TriplesNumericLiteralsFactory

    def __init__(self, create_inverse_triples: bool = False, **kwargs):
        """Initialize the Nations dataset with literals.

        :param create_inverse_triples: Should inverse triples be created? Defaults to false.
        :param kwargs: keyword arguments passed to :class:`pykeen.datasets.base.PathDataset`.
        """
        super().__init__(
            training_path=CKBC_TRAIN_PATH,
            testing_path=CKBC_TEST_PATH,
            validation_path=CKBC_VALIDATE_PATH,
            literals_path=CKBC_LITERALS_PATH,
            create_inverse_triples=create_inverse_triples,
            **kwargs,
        )


if __name__ == "__main__":
    Ckbc().summarize()
