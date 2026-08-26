# TAGLINE

DMI/SMBIOS 硬件信息解码工具

# TLDR

**显示全部 DMI 表内容**

```sudo dmidecode```

**显示 BIOS 版本**

```sudo dmidecode -s bios-version```

**显示系统序列号**

```sudo dmidecode -s system-serial-number```

**显示 BIOS 信息**

```sudo dmidecode -t bios```

**显示 CPU 信息**

```sudo dmidecode -t processor```

**显示内存信息**

```sudo dmidecode -t memory```

**显示系统制造商和产品名称**

```sudo dmidecode -t system```

**将 DMI 数据转储到二进制文件**

```sudo dmidecode --dump-bin [output.bin]```

**列出可用的字符串关键字**

```dmidecode --list-strings```

# SYNOPSIS

**dmidecode** [**-s** _keyword_] [**-t** _type_] [**--dump-bin** _file_] [**--from-dump** _file_]

# DESCRIPTION

**dmidecode** 读取 DMI（Desktop Management Interface）表，也称 SMBIOS（System Management BIOS），并以人类可读的格式显示硬件信息。内容涵盖 BIOS、系统、主板、机箱、处理器、内存、缓存、连接器和插槽等细节。

DMI 数据从 /dev/mem 或 sysfs 读取，取决于系统的可用情况。

# PARAMETERS

**-s**, **--string** _keyword_
> 仅显示特定 DMI 字符串的值（如 bios-vendor、bios-version、system-serial-number、system-uuid、processor-version、processor-frequency）。

**--list-strings**
> 列出可与 -s 搭配使用的全部有效字符串关键字。

**-t**, **--type** _type_
> 仅显示指定类型的条目。可以是数字、逗号分隔的列表，或关键字（bios、system、baseboard、chassis、processor、memory、cache、connector、slot）。

**--list-types**
> 列出可与 -t 搭配使用的全部有效类型关键字。

**-H**, **--handle** _handle_
> 仅显示匹配指定 16 位句柄值的条目。

**-q**, **--quiet**
> 减少输出；省略未知、未启用及 OEM 特有的条目。

**-u**, **--dump**
> 以十六进制显示原始 DMI 数据。

**--dump-bin** _file_
> 将 DMI 数据转储到二进制文件，供之后用 --from-dump 读取。

**--from-dump** _file_
> 从先前保存的二进制转储文件读取 DMI 数据。

**--no-quirks**
> 精确解码表内容，不对常见固件 bug 应用规避措施。

**--no-sysfs**
> 不尝试从 sysfs 文件读取 DMI 数据。

**-d**, **--dev-mem** _file_
> 从 /dev/mem 以外的设备文件读取内存。

**--oem-string** _N_
> 显示第 N 条 OEM 字符串，或使用 "count" 显示总数。

**-h**, **--help**
> 显示帮助。

**-V**, **--version**
> 显示版本。

# CAVEATS

需要 root 权限。信息准确性取决于 BIOS/固件的实现。仅适用于带符合 SMBIOS 标准固件的 x86 和 x86_64 系统。选项 **-s**、**-t** 和 **--dump-bin** 互斥。

# HISTORY

**dmidecode** 由 **Alan Cox** 编写，目前由 **Jean Delvare** 维护。它通过 SMBIOS 标准为 x86 和 x86_64 系统提供了访问系统硬件信息的标准化途径。

# INSTALL

```apt: sudo apt install dmidecode```

```dnf: sudo dnf install dmidecode```

```pacman: sudo pacman -S dmidecode```

```apk: sudo apk add dmidecode```

```zypper: sudo zypper install dmidecode```

```nix: nix profile install nixpkgs#dmidecode```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lshw](/man/lshw)(1), [lscpu](/man/lscpu)(1), [hwinfo](/man/hwinfo)(8), [biosdecode](/man/biosdecode)(8), [lspci](/man/lspci)(8)
