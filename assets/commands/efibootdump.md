# TAGLINE

UEFI 启动项解码器

# TLDR

从**文件**转储启动项

```efibootdump -f [/sys/firmware/efi/efivars/Boot0000-8be4df61-93ca-11d2-aa0d-00e098032b8c]```

按**变量名**转储启动项

```efibootdump [Boot0000]```

# SYNOPSIS

**efibootdump** [**-f**|**--file**] _variable_|_file_...

# DESCRIPTION

**efibootdump** 对 Boot0000 或 BootOrder 之类的 EFI 加载选项进行解码，并以人类可读的形式打印：描述、属性以及加载器的设备路径。

它既接受启动变量的名称（从正在运行的固件中读取），也可在给定 **-f** 时接受包含原始变量数据的文件。这使它既可用于检查实时的启动配置，也可用于查看从其他机器转储出来的变量。

# PARAMETERS

_variable_|_file_
> 启动变量名；使用 **-f** 时为文件路径。

**-f**, **--file**
> 将参数视为包含原始变量数据的文件而不是变量名。

# CAVEATS

只能在 UEFI 系统上工作，读取实时变量需要 efivarfs 已挂载到 /sys/firmware/efi/efivars。属于 **efivar** 软件包而非 efibootmgr，因此可能需要单独安装。读取原始变量文件通常需要 root 权限。

# INSTALL

```apt: sudo apt install efibootmgr```

```dnf: sudo dnf install efibootmgr```

```pacman: sudo pacman -S efibootmgr```

```apk: sudo apk add efibootmgr```

```zypper: sudo zypper install efibootmgr```

```nix: nix profile install nixpkgs#efibootmgr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[efibootmgr](/man/efibootmgr)(8), [efivar](/man/efivar)(1)

# RESOURCES

```[Source code](https://github.com/rhboot/efivar)```

<!-- verified: 2026-07-14 -->
