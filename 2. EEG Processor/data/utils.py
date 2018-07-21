# emacs: -*- mode: python-mode; py-indent-offset: 4; tab-width: 4; indent-tabs-mode: nil -*-
# ex: set sts=4 ts=4 sw=4 et:
"""
Utility functions for testing convert-eprime.

"""

from os.path import abspath, dirname, join, pardir, sep

# =============================================================================
# INPUT PATHS
# =============================================================================

def get_input_electrode_path():

    return abspath(join(dirname(__file__), 'input_electrode') + sep)

def get_input_event_path():

    return abspath(join(dirname(__file__), 'input_event') + sep)

def get_input_eprime_path():

    return abspath(join(dirname(__file__), 'input_eprime') + sep)

def get_input_exp_path():

    return abspath(join(dirname(__file__), 'csv_files_zero') + sep)

def get_input_merged_path():

    return abspath(join(dirname(__file__), 'merged_eeg') + sep)

def get_output_eprime_path():

    return abspath(join(dirname(__file__), 'output_eprime') + sep)

def get_output_final_path():

    return abspath(join(dirname(__file__), 'output_final') + sep)

def get_output_eeg_path():

    return abspath(join(dirname(__file__), 'output_eeg') + sep)

def get_in_data_path():

    return abspath(dirname(__file__) + sep)

def get_config_path():
    """
    Returns the path to test datasets, terminated with separator.

    Based on function by Yaroslav Halchenko used in Neurosynth Python package.
    """
    return abspath(join(dirname(__file__), pardir, pardir, 'config_files') + sep)

def remove_unicode(string):
    """
    Removes unicode characters in string.

    Parameters
    ----------
    string : str
        String from which to remove unicode characters.

    Returns
    -------
    str
        Input string, minus unicode characters.
    """
    return ''.join([val for val in string if 31 < ord(val) < 127])
