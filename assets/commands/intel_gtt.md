# TAGLINE

显示 Intel GPU 的图形地址重映射表（GTT）

# TLDR

**显示 GTT 状态**

```sudo intel_gtt```

**转储 GTT 条目**

```sudo intel_gtt -d```

**显示指定范围**

```sudo intel_gtt -r [0x0-0x1000]```

# SYNOPSIS

**intel_gtt** [_options_]

# PARAMETERS

**-d**
> 转储 GTT 条目。

**-r** _RANGE_
> 显示指定的地址范围。

**--help**
> 显示帮助信息。

# DESCRIPTION

**intel_gtt** 显示 Intel GPU 的图形地址重映射表（Graphics Translation Table）。GTT 将图形内存地址映射到物理内存。

该工具显示孔径使用情况和内存映射。可用于调试内存分配和 GPU 内存问题。

# CAVEATS

仅适用于 Intel 显卡。需要 root 权限。属于 intel-gpu-tools 的一部分。

# HISTORY

intel_gtt 是 **intel-gpu-tools** 的一部分，为 Intel 集成显卡的底层调试而开发。

# INSTALL

```apt: sudo apt install intel-gpu-tools```

```pacman: sudo pacman -S intel-gpu-tools```

```zypper: sudo zypper install intel-gpu-tools```

```nix: nix profile install nixpkgs#intel-gpu-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[intel_reg_read](/man/intel_reg_read)(1), [intel_error_decode](/man/intel_error_decode)(1)
