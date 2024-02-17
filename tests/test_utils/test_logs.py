
import pytest
import freezegun
from pathlib import Path
from glyphify.utils.logs import generate_log_path


class TestGenerateLogPath:
    @freezegun.freeze_time("2024-01-01 12:00:00")
    def test_generate_log_path_default_format(self):
        expected_path = Path("/application/logs") / "log_20240101_120000.log"
        result = generate_log_path(Path("/application"))
        assert result == expected_path

    @freezegun.freeze_time("2024-01-01 12:00:00")
    def test_generate_log_path_custom_format(self):
        expected_path = Path("/application/logs") / "log_2024-01-01_12-00-00.log"
        result = generate_log_path(Path("/application"), timestamp_format="%Y-%m-%d_%H-%M-%S")
        assert result == expected_path