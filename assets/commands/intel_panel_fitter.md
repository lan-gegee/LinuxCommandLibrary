# TAGLINE

控制 Intel GPU 的硬件缩放器

# TLDR

**显示面板缩放器状态**

```sudo intel_panel_fitter```

**显示指定管道的状态**

```sudo intel_panel_fitter -p [0]```

**启用面板缩放**

```sudo intel_panel_fitter -e```

**禁用面板缩放**

```sudo intel_panel_fitter -d```

# SYNOPSIS

**intel_panel_fitter** [_options_]

# PARAMETERS

**-p** _PIPE_
> 显示管道编号。

**-e**
> 启用面板缩放器。

**-d**
> 禁用面板缩放器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**intel_panel_fitter** 控制 Intel GPU 的硬件缩放器。面板缩放器将内容缩放到与显示器分辨率匹配。

该工具显示当前的缩放设置，并允许启用/禁用硬件缩放。可用于调试分辨率不匹配问题。

# CAVEATS

仅适用于 Intel 显卡。可能影响显示。属于 intel-gpu-tools 的一部分。需要 root 权限。

# HISTORY

intel_panel_fitter 是 **intel-gpu-tools** 的一部分，为测试 Intel 显示硬件的缩放功能而开发。

# INSTALL

```apt: sudo apt install intel-gpu-tools```

```pacman: sudo pacman -S intel-gpu-tools```

```zypper: sudo zypper install intel-gpu-tools```

```nix: nix profile install nixpkgs#intel-gpu-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[intel_infoframes](/man/intel_infoframes)(1), [xrandr](/man/xrandr)(1), [intel_reg_read](/man/intel_reg_read)(1)
