# TAGLINE

解码并显示 BIOS 数据结构

# TLDR

**显示所有 BIOS 信息**

```sudo biosdecode```

**从二进制转储文件读取 BIOS 数据**

```sudo biosdecode --dev-mem [bios.bin]```

**显示版本信息**

```biosdecode --version```

# SYNOPSIS

**biosdecode** [_options_]

# DESCRIPTION

**biosdecode** 解析 BIOS 内存，并打印它所识别的所有结构的信息，包括 SMBIOS（System Management BIOS）、DMI（Desktop Management Interface）、ACPI、PNP（即插即用）、BIOS32、PIR（PCI IRQ Routing）以及厂商专属结构（Compaq、IBM、Fujitsu、Sony）。

如需更详细的 SMBIOS/DMI 输出，请改用 **dmidecode**。

# PARAMETERS

**-d**, **--dev-mem** _FILE_
> 从设备文件 FILE 读取内存，而不是默认的 /dev/mem

**-V**, **--version**
> 显示版本信息并退出

**-h**, **--help**
> 显示帮助信息

# CAVEATS

需要 root 权限才能访问存储 BIOS 数据的 /dev/mem。在现代 Linux 系统上，更推荐使用 **dmidecode**，因为它提供更全面详细的输出。某些限制内存访问的系统可能无法让 biosdecode 正常工作。

# HISTORY

biosdecode 是 **dmidecode** 软件包的一部分，最初由 **Alan Cox** 编写并由 **Jean Delvare** 维护。它的诞生是为了提供一个在 Linux 系统上提取 BIOS 信息的简单工具，比功能更丰富的 dmidecode 更早出现。

# INSTALL

```apt: sudo apt install dmidecode```

```dnf: sudo dnf install dmidecode```

```pacman: sudo pacman -S dmidecode```

```apk: sudo apk add dmidecode```

```zypper: sudo zypper install dmidecode```

```nix: nix profile install nixpkgs#dmidecode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmidecode](/man/dmidecode)(1), [lshw](/man/lshw)(1), [hwinfo](/man/hwinfo)(1)
