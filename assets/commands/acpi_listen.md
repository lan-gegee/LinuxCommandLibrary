# TAGLINE

ACPI 事件监视器

# TLDR

在守护进程运行时**监听**任意 ACPI 事件

```acpi_listen```

# SYNOPSIS

**acpi_listen** [_-h_]

# DESCRIPTION

**acpi_listen** 实时监视并显示来自内核的 ACPI（Advanced Configuration and Power Interface）事件。事件包括电源键按下、笔记本盖开合、交流适配器接入、电池状态变化以及温度事件。

该工具连接 **acpid** 守护进程的套接字来接收事件。每个事件发生时都会被打印到标准输出。

# PARAMETERS

**-h, --help**
> 显示帮助信息

# CAVEATS

需要 **acpid** 守护进程正在运行。如果 acpid 未运行，或用户没有访问 ACPI 套接字的权限，将无法接收事件。

# HISTORY

属于 **acpid**（ACPI 守护进程）软件包，该软件包为 Linux 系统处理 ACPI 事件提供了框架。

# INSTALL

```apt: sudo apt install acpid```

```dnf: sudo dnf install acpid```

```pacman: sudo pacman -S acpid```

```apk: sudo apk add acpid```

```zypper: sudo zypper install acpid```

```nix: nix profile install nixpkgs#acpid```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[acpi](/man/acpi)(1), [acpid](/man/acpid)(8), [acpi_available](/man/acpi_available)(1)

# RESOURCES

```[Source code](https://sourceforge.net/projects/acpid2/)```

<!-- verified: 2026-06-10 -->
