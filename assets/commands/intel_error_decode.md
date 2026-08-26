# TAGLINE

解码内核日志中的 Intel GPU 错误状态

# TLDR

**从 dmesg 解码 GPU 错误**

```dmesg | intel_error_decode```

**解码错误文件**

```intel_error_decode < [error_state.txt]```

**附带着色器信息解码**

```intel_error_decode -s [shader.bin]```

# SYNOPSIS

**intel_error_decode** [_options_]

# PARAMETERS

**-s** _FILE_
> 提供上下文的着色器二进制文件。

**-c**
> 彩色输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**intel_error_decode** 从内核日志中解码 Intel GPU 的错误状态。它将硬件寄存器转储转换为人类可读的信息。

该工具解析 GPU 挂起（hang）信息，以定位出错的批处理和指令。它是调试图形驱动问题的重要工具。

# CAVEATS

仅适用于 Intel 显卡。需要来自 dmesg 的错误状态。属于 intel-gpu-tools 的一部分。

# HISTORY

intel_error_decode 是 **intel-gpu-tools** 的一部分，为调试 Intel 显卡硬件上的 GPU 挂起问题而创建。

# INSTALL

```apt: sudo apt install intel-gpu-tools```

```pacman: sudo pacman -S intel-gpu-tools```

```zypper: sudo zypper install intel-gpu-tools```

```nix: nix profile install nixpkgs#intel-gpu-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[intel_bios_reader](/man/intel_bios_reader)(1), [dmesg](/man/dmesg)(1)
