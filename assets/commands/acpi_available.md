# TAGLINE

检测系统是否支持 ACPI

# TLDR

**检查**系统上 ACPI 是否可用

```acpi_available && echo "ACPI supported"```

检查退出状态以便用于**脚本**

```if acpi_available; then echo "ACPI available"; fi```

# SYNOPSIS

**acpi_available**

# DESCRIPTION

**acpi_available** 是一个简单的实用工具，用于测试当前系统是否支持 ACPI（Advanced Configuration and Power Interface）。若支持则返回退出状态 0，否则返回 1，因此非常适合在 shell 脚本中做条件判断。

ACPI 提供有关电源管理、温区、电池和硬件配置的信息。该工具可帮助脚本判断能否使用依赖 ACPI 的功能，如电池监控或挂起/休眠。

# CAVEATS

该工具只检查基本的 ACPI 可用性，不判断特定的 ACPI 功能（如电池或温度）是否受支持。它是 acpid 的一部分，并非所有系统都默认安装。

# HISTORY

**acpi_available** 属于 **acpid**（ACPI 守护进程）软件包。自 **21 世纪初**以来，acpid 一直是 Linux 电源管理的标准组件。开发该工具是为了帮助脚本和应用检测 ACPI 支持。

# SEE ALSO

[acpi](/man/acpi)(1), [acpid](/man/acpid)(8), [acpi_listen](/man/acpi_listen)(8), [apm_available](/man/apm_available)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/acpid2/)```

<!-- verified: 2026-06-10 -->
