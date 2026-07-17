# Copyright 2026 Waydroid Project
# SPDX-License-Identifier: GPL-3.0-or-later
import os
import socket


def sd_notify(state):
    """sd_notify(3); no-op outside a systemd service (NOTIFY_SOCKET unset)."""
    addr = os.environ.get("NOTIFY_SOCKET")
    if not addr:
        return
    if addr.startswith("@"):
        addr = "\0" + addr[1:]
    try:
        with socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM) as sock:
            sock.connect(addr)
            sock.sendall(state.encode())
    except OSError:
        pass
