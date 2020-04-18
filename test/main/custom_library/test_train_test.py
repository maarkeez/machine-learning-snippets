from random import seed
from unittest import TestCase

from src.main.custom_library import split_dataset


class Test(TestCase):
    dataset = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]

    def test_train_test_split(self):
        # seed: is to ensure the exact same split of the data is made every time the code is executed
        seed(1)

        train, test = split_dataset.train_test_split(self.dataset)

        self.assertEqual(6, len(train))
        self.assertEqual(4, len(test))

    def test_cross_validation_split(self):
        # seed: is to ensure the exact same split of the data is made every time the code is executed
        seed(1)

        folds = split_dataset.cross_validation_split(self.dataset, folds=4)

        self.assertEqual(4, len(folds))
        self.assertEqual(2, len(folds[0]))
        self.assertEqual(2, len(folds[1]))
        self.assertEqual(2, len(folds[2]))
        self.assertEqual(2, len(folds[3]))
