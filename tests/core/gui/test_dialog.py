# Parsec Cloud (https://parsec.cloud) Copyright (c) AGPLv3 2016-2021 Scille SAS

import pytest
import multiprocessing
from parsec.core.gui.custom_dialogs import QDialogInProcess


@pytest.fixture
def close_process_pool():
    if multiprocessing.get_start_method(allow_none=True) is None:
        multiprocessing.set_start_method("spawn")
    assert multiprocessing.get_start_method() == "spawn"
    yield
    QDialogInProcess.pool.terminate()
    QDialogInProcess.pool.join()


@pytest.mark.gui
@pytest.mark.trio
async def test_file_dialog_in_process(gui, close_process_pool):
    assert QDialogInProcess.getOpenFileName(gui, "title", dir="dir", testing=True) == (
        "getOpenFileName",
        ("title",),
        {"dir": "dir"},
    )
    assert QDialogInProcess.getOpenFileNames(gui, "title", dir="dir", testing=True) == (
        "getOpenFileNames",
        ("title",),
        {"dir": "dir"},
    )
    assert QDialogInProcess.getSaveFileName(gui, "title", dir="dir", testing=True) == (
        "getSaveFileName",
        ("title",),
        {"dir": "dir"},
    )
    assert QDialogInProcess.getExistingDirectory(gui, "title", dir="dir", testing=True) == (
        "getExistingDirectory",
        ("title",),
        {"dir": "dir"},
    )

    with pytest.raises(TypeError) as ctx:
        QDialogInProcess.getOpenFileName(gui, i_dont_exist=42)
    assert "'i_dont_exist' is not a valid keyword argument" in str(ctx.value)
