# TAGLINE

查看和修改 GPU 发送的 HDMI InfoFrame

# TLDR

**查看 HDMI infoframe**

```sudo intel_infoframes```

**显示带字段说明的帮助**

```intel_infoframes --help```

# SYNOPSIS

**intel_infoframes** [_options_]

# PARAMETERS

**-h**, **--help**
> 显示帮助信息和字段说明。

# DESCRIPTION

**intel_infoframes** 是一款调试工具，用于查看和修改 GPU 发送的 HDMI InfoFrame。InfoFrame 承载关于视频格式、音频和其他显示参数的元数据。

InfoFrame 字段的说明可参考 HDMI 和 CEA-861 规范。并非所有 HDMI 显示器都会遵守发送给它们的 InfoFrame。某些情况下（例如切换显示模式时），内核会撤销本工具所做的更改。

# CAVEATS

仅适用于 Intel 显卡（GEN 4 或更新）。需要有正在工作的显示器。属于 intel-gpu-tools（igt-gpu-tools）的一部分。

# HISTORY

intel_infoframes 是 **intel-gpu-tools** 的一部分，用于调试 Intel 显卡的数字显示连接。

# INSTALL

```apt: sudo apt install intel-gpu-tools```

```pacman: sudo pacman -S intel-gpu-tools```

```zypper: sudo zypper install intel-gpu-tools```

```nix: nix profile install nixpkgs#intel-gpu-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[intel_panel_fitter](/man/intel_panel_fitter)(1), [intel_reg_read](/man/intel_reg_read)(1), [xrandr](/man/xrandr)(1)
