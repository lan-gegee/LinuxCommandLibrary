# TAGLINE

提取并显示 Intel 显卡 BIOS 信息

# TLDR

**从 BIOS 转储文件解析 VBT**

```intel_bios_reader --file=[bios.bin]```

**解析所有平板面板的详细信息**

```intel_bios_reader --file=[bios.bin] --all-panels```

**以十六进制转储 BIOS 块**

```intel_bios_reader --file=[bios.bin] --hexdump```

**转储指定的 BIOS 数据块**

```intel_bios_reader --file=[bios.bin] --block=[N]```

**伪装成指定的 PCI 设备 ID**

```intel_bios_reader --file=[bios.bin] --devid=[DEVID]```

# SYNOPSIS

**intel_bios_reader** [_options_]

# PARAMETERS

**--file=** _FILE_
> 从 FILE 解析 Video BIOS Tables。

**--devid=** _DEVID_
> 伪装成 PCI ID DEVID，以便进行更准确的平台特定解析。

**--panel-type=** _N_
> 解析第 N 个平板面板的详细信息，覆盖 VBT 中的值。

**--all-panels**
> 解析 Video BIOS Tables 中所有平板面板的详细信息。

**--hexdump**
> 以十六进制转储各块。

**--block=** _N_
> 只转储编号为 N 的 BIOS 数据块。

**--help**
> 显示帮助信息。

# DESCRIPTION

**intel_bios_reader** 解析 Intel Video BIOS Tables（VBT），并以人类可读的格式打印信息。二进制 VBT 可以从内核调试接口读取，也可以从之前保存的转储文件读取。

该工具显示面板时序、背光设置和显示连接器信息。它主要用于调试 Intel 集成显卡的显示配置问题。

# CAVEATS

仅适用于 Intel 显卡。需要 VBT 转储文件（由 intel_bios_dumper 生成）或相应的内核调试访问权限。属于 intel-gpu-tools 的一部分。

# HISTORY

intel_bios_reader 是 **intel-gpu-tools**（igt-gpu-tools）的一部分，为调试 Intel 集成显卡硬件而开发。

# SEE ALSO

[intel_error_decode](/man/intel_error_decode)(1), [intel_reg_read](/man/intel_reg_read)(1)
