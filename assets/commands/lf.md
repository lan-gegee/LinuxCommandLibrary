# TAGLINE

终端文件管理器

# TLDR

**启动文件管理器**

```lf```

**打开指定目录**

```lf [/path/to/dir]```

**启动时执行命令**

```lf -command "[set hidden]"```

**打印选中的文件**

```lf -print-selection```

**使用指定的配置文件**

```lf -config [config.lf]```

# SYNOPSIS

**lf** [_options_] [_path_]

# PARAMETERS

_PATH_
> 启动时进入的目录。

**-command** _CMD_
> 启动时执行命令。

**-config** _FILE_
> 配置文件路径。

**-print-selection**
> 退出时打印选中项。

**--help**
> 显示帮助信息。

# DESCRIPTION

**lf** 是一个终端文件管理器。它凭借类 vim 的按键绑定提供快速导航。

该工具用 Go 编写以保证可移植性。它支持预览、批量操作和脚本化扩展。

# CAVEATS

基于终端。采用 vim 按键绑定。通过 lfrc 进行配置。

# HISTORY

lf 受 **ranger** 启发而创建，用 Go 编写，追求更好的性能与简洁性。

# INSTALL

```apt: sudo apt install lf```

```pacman: sudo pacman -S lf```

```apk: sudo apk add lf```

```zypper: sudo zypper install lf```

```brew: brew install lf```

```nix: nix profile install nixpkgs#lf```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ranger](/man/ranger)(1), [nnn](/man/nnn)(1), [mc](/man/mc)(1)
