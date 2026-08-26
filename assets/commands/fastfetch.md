# TAGLINE

快速、可定制的系统信息显示工具

# TLDR

**显示系统信息**

```fastfetch```

**使用指定的配置预设**

```fastfetch --config [paleofetch]```

**只显示指定模块**

```fastfetch --structure "Title:Separator:OS:Host:Kernel:Uptime"```

**隐藏徽标**

```fastfetch --logo none```

**使用指定徽标**

```fastfetch --logo [arch]```

**使用小徽标**

```fastfetch --logo-type small```

**列出可用预设**

```fastfetch --list-presets```

**生成配置文件**

```fastfetch --gen-config```

# SYNOPSIS

**fastfetch** [_options_]

# DESCRIPTION

**fastfetch** 是一款用 C 编写的快速、高度可定制的系统信息工具。它以美观的格式配合 ASCII 艺术徽标，显示你的操作系统、软件和硬件信息。

该工具被设计为 neofetch、screenfetch 及类似系统信息工具的更快速替代品。它可通过 JSON 配置文件和命令行选项进行深度定制，支持自定义模块顺序、颜色和徽标。

fastfetch 可检测并显示 OS、内核、DE/WM、终端、Shell、CPU、GPU、内存、磁盘、电池等众多系统属性。它支持多个平台，包括 Linux、macOS、Windows 和 FreeBSD。

# PARAMETERS

**--config** _file_
> 使用指定的配置文件。

**--structure** _modules_
> 指定要显示的模块。

**--logo** _name_
> 要显示的徽标（或 "none"）。

**--logo-type** _type_
> 徽标类型（normal、small、builtin）。

**--color** _colors_
> 设置输出颜色。

**--separator** _string_
> 标签与值之间的字符串。

**--gen-config** [_file_]
> 生成配置文件。

**--list-presets**
> 列出可用的配置预设。

**--list-logos**
> 列出可用的徽标。

**--list-modules**
> 列出可用的模块。

**--help**
> 显示帮助信息。

**--version**
> 显示版本信息。

# CONFIGURATION

**~/.config/fastfetch/config.jsonc**
> 用户配置文件，用于自定义模块、显示格式和外观。

# CAVEATS

部分模块需要特定的系统支持或库。GPU 检测可能需要正确的驱动程序。自定义徽标需要终端字体支持。配置文件格式在不同版本间有过变更。

# HISTORY

**fastfetch** 由 **Linus Dierheimer**（LinusDierheimer）于 **2021 年**创建，作为 neofetch 的更快速替代品。它用 C 编写以追求性能，回应了人们对 neofetch 的 bash 实现速度慢的抱怨。该项目凭借速度和丰富的自定义选项迅速走红。

# INSTALL

```apt: sudo apt install fastfetch```

```dnf: sudo dnf install fastfetch```

```pacman: sudo pacman -S fastfetch```

```apk: sudo apk add fastfetch```

```zypper: sudo zypper install fastfetch```

```brew: brew install fastfetch```

```nix: nix profile install nixpkgs#fastfetch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neofetch](/man/neofetch)(1), [screenfetch](/man/screenfetch)(1), [inxi](/man/inxi)(1), [hwinfo](/man/hwinfo)(1)

# RESOURCES

```[Source code](https://github.com/fastfetch-cli/fastfetch)```

<!-- verified: 2026-07-15 -->
