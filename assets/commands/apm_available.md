# TAGLINE

检查高级电源管理（APM）支持

# TLDR

**检查** APM 是否可用

```apm_available && echo "APM supported"```

在**脚本条件判断**中使用

```if apm_available; then apm -l; fi```

# SYNOPSIS

**apm_available**

# PARAMETERS

此命令不接受任何参数。

# DESCRIPTION

**apm_available** 通过检查 /proc/apm 文件来测试当前系统是否支持高级电源管理（APM）。支持时返回退出状态 0，不支持时返回 1。

该工具适用于需要在 APM 与 ACPI 之间选择电源管理查询方式的脚本。

# CAVEATS

现代系统上 APM 已被弃用，由 ACPI 取代。大多数现代硬件只支持 ACPI。该工具检测的是 APM BIOS 是否存在，而非其功能是否正常。

# HISTORY

**apm_available** 属于 **20 世纪 90 年代**至 **21 世纪初**的 apmd 软件包，那时 APM 还是 PC 的标准电源管理接口。

# SEE ALSO

[apm](/man/apm)(1), [acpi_available](/man/acpi_available)(1), [acpi](/man/acpi)(1)
