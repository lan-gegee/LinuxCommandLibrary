# TAGLINE

显示和操作逻辑卷管理器的配置信息

# TLDR

显示正在使用的**生效配置**（合并所有配置源之后）

```lvmconfig --typeconfig current --mergedconfig```

只显示**与默认值不同**的设置

```lvmconfig --typeconfig diff```

**列出所有配置键**

```lvmconfig -l```

打印带完整注释和额外空行的**默认配置**

```lvmconfig --typeconfig default --withcomments --withspaces```

**校验**完整的合并配置并报告错误

```lvmconfig --mergedconfig --validate```

将当前生效配置**写入**文件

```lvmconfig --typeconfig current -f [path/to/output.conf]```

# SYNOPSIS

**lvmconfig** [_options_] [_section_]

# PARAMETERS

**--typeconfig _type_**
> 指定配置类型：current、default、diff、full、list、missing、new、profilable 或 profilable-command

**--mergedconfig**
> 显示前先合并所有配置源

**-l, --list**
> 列出所有配置键

**--withcomments**
> 在输出中包含解释性注释

**--withspaces**
> 添加额外的空行以提高可读性

**--validate**
> 检查配置中的错误并报告问题

**-f, --file _path_**
> 将输出写入文件而非标准输出

**--config _string_**
> 从命令行覆盖配置设置

# DESCRIPTION

**lvmconfig** 显示和操作逻辑卷管理器（LVM）的配置信息。它从多个来源（命令行、环境变量、配置文件）读取配置，并可显示合并后的生效配置。

该工具支持不同的配置视图：**current** 显示当前生效的设置，**default** 显示内置默认值，**diff** 只显示非默认值，**full** 显示全部内容。它还可以校验配置文件的语法错误和已弃用的选项。

配置节包括全局设置、设备过滤器、激活选项，以及针对卷组和逻辑卷的分配策略。

# CAVEATS

用 lvmconfig 所做的配置更改不会持久化；要永久更改请直接编辑 **/etc/lvm/lvm.conf**。**--validate** 选项可能无法发现所有配置问题，特别是那些依赖运行时条件的问题。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvm](/man/lvm)(8), [pvcreate](/man/pvcreate)(8), [vgcreate](/man/vgcreate)(8), [lvcreate](/man/lvcreate)(8)
