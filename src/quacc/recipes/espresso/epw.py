"""
This module, 'epw.py', contains recipes for performing electron-phonon coupling
calculations using the epw.x binary from Quantum ESPRESSO via the quacc library.
"""

from __future__ import annotations

from typing import TYPE_CHECKING

from quacc import job
from quacc.calculators.espresso.espresso import EspressoTemplate
from quacc.recipes.espresso._base import run_and_summarize

if TYPE_CHECKING:
    from typing import Any

    from quacc.types import (
        Filenames,
        RunSchema,
        SourceDirectory,
    )

@job
def epw_job(
    copy_files: (
        SourceDirectory | list[SourceDirectory] | dict[SourceDirectory, Filenames]
    ),
    additional_fields: dict[str, Any] | None = None,
    **calc_kwargs,
) -> RunSchema:
    """
    Function to carry out a basic `epw.x` calculation. It should allow you to use
    all the features of the [epw.x binary](https://docs.epw-code.org/)

    This program calculates properties related to the electron-phonon interaction.

    Parameters
    ----------
    copy_files
        Source directory or directories to copy files from. If a `SourceDirectory` or a
        list of `SourceDirectory` is provided, this interface will automatically guess
        which files have to be copied over by looking at the binary and `input_data`.
        If a dict is provided, the mode is manual, keys are source directories and values
        are relative path to files or directories to copy. Glob patterns are supported.
    additional_fields
        Additional fields to add to the results dictionary.
    **calc_kwargs
        Additional keyword arguments to pass to the Espresso calculator. Set a value to
        `quacc.Remove` to remove a pre-existing key entirely. See the docstring of
        [quacc.calculators.espresso.espresso.Espresso][] for more information.

    Returns
    -------
    RunSchema
        Dictionary of results from [quacc.schemas.ase.Summarize.run][].
        See the type-hint for the data structure.
    """
    return run_and_summarize(
        template=EspressoTemplate("epw"),
        calc_defaults={},
        calc_swaps=calc_kwargs,
        additional_fields={"name": "epw.x Electron-Phonon"} | (additional_fields or {}),
        copy_files=copy_files,
    )