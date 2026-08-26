# TAGLINE

读取 Intel GPU 的硬件寄存器

# TLDR

**按地址读取指定寄存器**

```sudo intel_reg read [0x70000]```

**读取多个寄存器**

```sudo intel_reg read [0x70000] [0x70004]```

**将寄存器位解码为命名字段**

```sudo intel_reg read --decode [0x70000]```

**转储所有已知寄存器**

```sudo intel_reg read --all```

**带解码地转储寄存器**

```sudo intel_reg read --all --decode```

# SYNOPSIS

**intel_reg** **read** [_options_] [_register_...]

# PARAMETERS

_REGISTER_
> 十六进制寄存器地址（如 0x70000）。

**--decode**
> 将寄存器位解码为命名字段。

**--all**
> 转储所有已知寄存器。

**--help**
> 显示帮助信息。

# DESCRIPTION

**intel_reg read** 是 `intel_reg` 的子命令，用于读取 Intel GPU 的硬件寄存器。它直接访问 GPU 配置寄存器，便于调试和开发。

配合 `--decode` 标志使用时，该工具可将寄存器位解码为有意义的命名字段。

# CAVEATS

仅适用于 Intel 显卡。需要 root 权限。可能影响系统稳定性。属于 intel-gpu-tools 的一部分。

# HISTORY

intel_reg_read 是 **intel-gpu-tools** 的一部分，为 Intel 显卡驱动开发与调试而创建。

# SEE ALSO

[intel_gtt](/man/intel_gtt)(1)
