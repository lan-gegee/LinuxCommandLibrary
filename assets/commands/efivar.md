# TAGLINE

UEFI 变量管理工具

# TLDR

**列出**所有 UEFI 变量

```efivar -l```

**打印**变量内容

```efivar -n [guid-name] -p```

**导出**变量到文件

```efivar -n [guid-name] -e [path/to/output_file]```

**列出**已知的 GUID 名称

```efivar -L```

# SYNOPSIS

**efivar** [_OPTION_...]

# DESCRIPTION

**efivar** 管理存储在 NVRAM 中的 UEFI 变量。它可以列出、读取、写入和删除 EFI 变量。这些变量包含启动配置、安全启动设置和其他固件数据。

可用于调试 UEFI 启动问题和检查固件配置。

# PARAMETERS

**-l, --list**
> 列出当前的 EFI 变量

**-n, --name** _guid-name_
> 要操作的变量，格式为 8be4df61-93ca-11d2-aa0d-00e098032b8c-BootOrder

**-p, --print**
> 打印 --name 指定的变量

**-d, --print-decimal**
> 以十进制格式打印 --name 指定的变量的值

**-a, --append**
> 追加到 --name 指定的变量

**-A, --attributes** _attributes_
> 追加时使用的属性

**-w, --write**
> 写入 --name 指定的变量

**-f, --datafile** _file_
> 从文件加载或保存变量内容

**-e, --export** _file_
> 导出变量到文件

**-i, --import** _file_
> 从文件导入变量

**-L, --list-guids**
> 显示内部 GUID 列表

**-D, --dmpstore**
> 导出时使用 DMPSTORE 格式

# CAVEATS

写操作需要 root 权限。错误地修改 EFI 变量可能导致系统无法启动。某些变量受安全启动（Secure Boot）保护。

# INSTALL

```apt: sudo apt install efivar```

```dnf: sudo dnf install efivar```

```pacman: sudo pacman -S efivar```

```apk: sudo apk add efivar```

```zypper: sudo zypper install efivar```

```nix: nix profile install nixpkgs#efivar```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[efibootmgr](/man/efibootmgr)(8), [mokutil](/man/mokutil)(1)
