#!/usr/bin/env python3
"""Regression tests for Cursor → Codex bridge authentication routing."""

from __future__ import annotations

import os
import stat
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
BRIDGE = ROOT / "scene-skill-core/scripts/codex_exec_bridge.py"


def _run(
    path: Path,
    prompt: str = "",
    codex_home: Path | None = None,
    check: bool = False,
) -> subprocess.CompletedProcess[str]:
    env = os.environ.copy()
    env["PATH"] = str(path)
    if codex_home is not None:
        env["CODEX_HOME"] = str(codex_home)
    command = [sys.executable, str(BRIDGE)]
    command.extend(["--check", "--json"] if check else ["--output-dir", str(path / "output")])
    return subprocess.run(
        command,
        input=prompt,
        text=True,
        capture_output=True,
        env=env,
        cwd=ROOT,
        check=False,
    )


def _fake_codex(path: Path, logged_in: bool, probe_path: Path | None = None) -> None:
    script = path / "codex"
    status = "0" if logged_in else "1"
    probe = f'printf "%s" "$CODEX_HOME" > "{probe_path}"' if probe_path else ":"
    script.write_text(
        f"""#!/bin/sh
if [ "$1" = "login" ] && [ "$2" = "status" ]; then
  {probe}
  exit {status}
fi
exit 99
""",
        encoding="utf-8",
    )
    script.chmod(script.stat().st_mode | stat.S_IXUSR)


def main() -> int:
    with tempfile.TemporaryDirectory(prefix="codex-bridge-auth-") as raw:
        base = Path(raw)

        missing = _run(base)
        assert missing.returncode == 2
        assert "codex CLI not found" in missing.stderr
        assert "OPENAI_API_KEY" not in missing.stderr

        not_logged_in_dir = base / "not-logged-in"
        not_logged_in_dir.mkdir()
        _fake_codex(not_logged_in_dir, logged_in=False)
        not_logged_in = _run(not_logged_in_dir)
        assert not_logged_in.returncode == 2
        assert "codex login" in not_logged_in.stderr
        assert "OPENAI_API_KEY" not in not_logged_in.stderr

        capability = _run(not_logged_in_dir, check=True)
        assert capability.returncode == 2
        assert '"authenticated": false' in capability.stdout
        assert '"api_key_required": false' in capability.stdout

        logged_in_dir = base / "logged-in"
        logged_in_dir.mkdir()
        _fake_codex(logged_in_dir, logged_in=True)
        empty_prompt = _run(logged_in_dir)
        assert empty_prompt.returncode == 2
        assert "prompt is empty" in empty_prompt.stderr
        assert "OPENAI_API_KEY" not in empty_prompt.stderr

        alternate_home = base / "alternate-codex-home"
        alternate_dir = base / "alternate-home-cli"
        alternate_dir.mkdir()
        probe_path = base / "codex-home-probe.txt"
        _fake_codex(alternate_dir, logged_in=True, probe_path=probe_path)
        alternate = _run(alternate_dir, codex_home=alternate_home)
        assert alternate.returncode == 2
        assert probe_path.read_text(encoding="utf-8") == str(alternate_home)
        assert "OPENAI_API_KEY" not in alternate.stderr

        capability = _run(alternate_dir, check=True, codex_home=alternate_home)
        assert capability.returncode == 0
        assert '"authenticated": true' in capability.stdout
        assert '"can_generate": true' in capability.stdout

    print("PASS: auth preflight and alternate CODEX_HOME paths")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
