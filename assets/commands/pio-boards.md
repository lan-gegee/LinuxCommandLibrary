# TAGLINE

列出 PlatformIO 支持的开发板

# TLDR

**列出所有支持的开发板**

```pio boards```

**搜索开发板**

```pio boards [arduino]```

**以 JSON 格式列出开发板**

```pio boards --json-output```

**按已安装的平台过滤**

```pio boards --installed```

# SYNOPSIS

**pio boards** [_options_] [_filter_]

# PARAMETERS

**--installed**
> 只显示已安装的开发板。

**--json-output**
> 以 JSON 格式输出。

_filter_
> 搜索过滤字符串。

# DESCRIPTION

**pio boards** 列出 PlatformIO 支持的开发板。它以格式化的表格显示开发板 ID、MCU 类型、频率、flash 容量、RAM 和板名。在项目设置中可将开发板 ID 与 **pio init** 配合使用。

可选的过滤参数可按平台、MCU 或板名缩小结果范围（如 `pio boards arduino`、`pio boards atmega168`）。

# INSTALL

```aur: yay -S pio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pio](/man/pio)(1), [pio-init](/man/pio-init)(1), [pio-run](/man/pio-run)(1), [pio-platform](/man/pio-platform)(1)
