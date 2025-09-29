# tests/test_main.py

import pytest
from src.main import can_Play_VP9
from src.crash_guard import CrashGuard

def test_can_play_vp9_success(mocker):
    mocker.patch('src.main.create_Decoder', return_value='decoder')
    mocker.patch('src.main.prefs', {"media.wmf.vp9.enabled": True})
    assert can_Play_VP9() is True

def test_can_play_vp9_failure_no_decoder(mocker):
    mocker.patch('src.main.create_Decoder', return_value=None)
    mocker.patch('src.main.prefs', {"media.wmf.vp9.enabled": True})
    assert can_Play_VP9() is False

def test_can_play_vp9_crash_handling(mocker):
    crash_guard = CrashGuard("WMFVPXVideo")
    mocker.patch('src.main.crash_Guard', return_value=crash_guard)
    mocker.patch('src.main.create_Decoder', side_effect=Exception("Crash"))
    mocker.patch('src.main.prefs', {"media.wmf.vp9.enabled": True})

    # Simulate a crash
    crash_guard.markAsCrashed()
    assert can_Play_VP9() is False
    assert crash_guard.hasCrashedBefore() is True

def test_can_play_vp9_disabled(mocker):
    mocker.patch('src.main.prefs', {"media.wmf.vp9.enabled": False})
    assert can_Play_VP9() is False