# TAGLINE

检查交流电源连接状态

# TLDR

检查**交流电源**状态

```systemd-ac-power```

以**详细输出**方式检查

```systemd-ac-power -v```

# SYNOPSIS

**systemd-ac-power** [_OPTIONS_]

# PARAMETERS

**-v, --verbose**
> 除退出码外，还向 stdout 打印 "yes" 或 "no"

**-h, --help**
> 显示帮助

# DESCRIPTION

**systemd-ac-power** 报告计算机是否连接了外部电源（市电）。使用交流电源时返回退出码 0，使用电池时返回非零值。

这在脚本和 systemd 单元条件中很有用，可以根据电源状态改变行为。

# EXIT STATUS

**0** - 正在使用交流电源

**非零值** - 正在使用电池或无法判断

# CAVEATS

需要内核正确检测电源。某些没有电池的台式机系统总是报告为使用交流电源。虚拟机可能报告错误的电源状态。

# HISTORY

**systemd-ac-power** 为电源状态提供了一个简单、可脚本化的接口，使 systemd 单元和 Shell 脚本能够感知电源状态。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[systemctl](/man/systemctl)(1), [upower](/man/upower)(1)
