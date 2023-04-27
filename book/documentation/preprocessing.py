"""
Preprocessing Classes
"""

import numpy as np

class RandomScaler:
    """
    Randomly scales the input data by a given factor.

    Parameters
    ----------
    scale_factor : float, optional
        Scaling factor to apply to the input data, by default 1.0

    Attributes
    ----------
    scale_factor : float
        Scaling factor to apply to the input data

    Methods
    -------
    fit_transform(X)
        Scales the input data by a randomly generated factor.

    Returns
    -------
    np.ndarray
        Scaled input data.

    Examples
    --------
    >>> import numpy as np
    >>> from preprocessing import RandomScaler
    >>> X = np.random.rand(10, 5)
    >>> scaler = RandomScaler(scale_factor=2.0)
    >>> X_scaled = scaler.fit_transform(X)
    """
    def __init__(self, scale_factor: float = 1.0) -> None:
        self.scale_factor = scale_factor

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        """
        Scales the input data by a randomly generated factor.

        Parameters
        ----------
        X : np.ndarray
            Input data to be scaled.

        Returns
        -------
        np.ndarray
            Scaled input data.
        """
        scale_factor = np.random.uniform(0.5 * self.scale_factor, 1.5 * self.scale_factor)
        return X * scale_factor

    
class MissingValueImputer:
    """
    Replaces missing values in the input data with a given value.

    Parameters
    ----------
    missing_value : float, optional
        Value to replace missing values with, by default 0

    Attributes
    ----------
    missing_value : float
        Value to replace missing values with

    Methods
    -------
    fit_transform(X)
        Replaces missing values in the input data with the specified value.

    Returns
    -------
    np.ndarray
        Input data with missing values replaced.

    Examples
    --------
    >>> import numpy as np
    >>> from preprocessing import MissingValueImputer
    >>> X = np.array([[1, 2, np.nan], [4, np.nan, 6], [7, 8, 9]])
    >>> imputer = MissingValueImputer(missing_value=-1)
    >>> X_imputed = imputer.fit_transform(X)
    """
    def __init__(self, missing_value: float = 0) -> None:
        self.missing_value = missing_value

    def fit_transform(self, X: np.ndarray) -> np.ndarray:
        """
        Replaces missing values in the input data with the specified value.

        Parameters
        ----------
        X : np.ndarray
            Input data with missing values.

        Returns
        -------
        np.ndarray
            Input data with missing values replaced.
        """
        X[np.isnan(X)] = self.missing_value
        return X