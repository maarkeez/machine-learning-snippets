import algorithm_evaluation
import base_models
import column_conversion
import csv_loader
import evaluation_metrics
import linear_regression
import mean
import minmax
import multivariante_linear_regresion
import normalize
import split_dataset
import standard_deviations
import variance
from src.main.custom_library import logistic_regresion


def load_csv(filename):
    return csv_loader.load_csv(filename)


def load_dataset_pima():
    return csv_loader.load_dataset_pima()


def load_dataset_iris():
    return csv_loader.load_dataset_iris()


def load_dataset_swedish_insurance():
    return csv_loader.load_dataset_swedish_insurance()


def load_dataset_wine_quality():
    return csv_loader.load_dataset_wine_quality()


def str_column_to_float(dataset, column):
    column_conversion.str_column_to_float(dataset, column)


def str_column_to_int(dataset, column):
    return column_conversion.str_column_to_int(dataset, column)


def dataset_minmax(dataset):
    return minmax.dataset_minmax(dataset)


def normalize_dataset(dataset, minmax):
    return normalize.normalize_dataset(dataset, minmax)


def column_means(dataset):
    return mean.column_means(dataset)


def mean_of_list(value_list):
    return mean.mean_of_list(value_list)


def variance_of_list(value_list):
    return variance.variance_of_list(value_list)


def covariance_of_lists(x, y):
    return variance.covariance_of_lists(x, y)


def column_stdevs(dataset, means):
    return standard_deviations.column_stdevs(dataset, means)


def standardize_dataset(dataset, means, stdevs):
    return standard_deviations.standardize_dataset(dataset, means, stdevs)


def split_with_train_test(dataset, split=0.6):
    return split_dataset.train_test_split(dataset, split)


def split_with_cross_validation(dataset, folds=3):
    return split_dataset.cross_validation_split(dataset, folds)


def evaluate_accuracy(actual, predicted):
    return evaluation_metrics.accuracy(actual, predicted)


def evaluate_confusion_matrix(actual, predicted):
    return evaluation_metrics.confusion_matrix(actual, predicted)


def evaluate_mean_absolute_error(actual, predicted):
    return evaluation_metrics.mean_absolute_error(actual, predicted)


def evaluate_root_mean_squared_error(actual, predicted):
    return evaluation_metrics.root_mean_squared_error(actual, predicted)


def algorithm_random(train, test):
    return base_models.random_algorithm(train, test)


def algorithm_classification_zero_rule(train, test):
    return base_models.algorithm_classification_zero_rule(train, test)


def algorithm_regression_zero_rule(train, test):
    return base_models.algorithm_regression_zero_rule(train, test)


def algorithm_regression_simple_linear(train_set, test_set):
    return linear_regression.algorithm_regression_simple_linear(train_set, test_set)


def algorithm_regression_linear_stochastic_gradient_descent(train_set, test_set, learning_rate, n_epoch):
    return multivariante_linear_regresion.algorithm_stochastic_gradient_descent(
        train_set, test_set, learning_rate, n_epoch)


def algorithm_regression_logistic(train_set, test_set, learning_rate, n_epoch):
    return logistic_regresion.logistic_regression(train_set, test_set, learning_rate, n_epoch)


def algorithm_evaluation_classification_with_train_test_split(dataset, algorithm, split, *args):
    return algorithm_evaluation.classification_with_train_test_split(dataset, algorithm, split, *args)


def algorithm_evaluation_classification_with_cross_validation(dataset, algorithm, n_folds, *args):
    return algorithm_evaluation.classification_with_cross_validation(dataset, algorithm, n_folds, *args)


def algorithm_evaluation_regression_with_cross_validation(dataset, algorithm, n_folds, *args):
    return algorithm_evaluation.regression_with_cross_validation(dataset, algorithm, n_folds, *args)


def algorithm_evaluation_regression_with_simple_linear(data_set, algorithm, split, *args):
    return algorithm_evaluation.regression_with_simple_linear(data_set, algorithm, split, *args)


def estimate_coefficients(data_set):
    return linear_regression.estimate_coefficients(data_set)
