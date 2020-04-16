import column_conversion
import csv_loader
import mean
import minmax
import normalize
import standard_deviations


def load_csv(filename):
    return csv_loader.load_csv(filename)


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


def column_stdevs(dataset, means):
    return standard_deviations.column_stdevs(dataset, means)


def standardize_dataset(dataset, means, stdevs):
    return standard_deviations.standardize_dataset(dataset, means, stdevs)