# TAGLINE

类 shell 的命令行文件管理器

# TLDR

**启动文件管理器**

```clifm```

**在指定目录中启动**

```clifm [/path/to/dir]```

**以指定 profile 启动**

```clifm -P [profile_name]```

**以隐身模式启动**

```clifm -S```

**显示隐藏文件**

```clifm -a```

# SYNOPSIS

**clifm** [_options_] [_path_]

# DESCRIPTION

**clifm** 是一个类 shell 的命令行终端文件管理器，与 ranger 或 nnn 等 TUI 文件管理器有根本区别。用户不是在基于面板的界面中导航，而是通过命令提示符进行交互，使用 ELN（Entry List Numbers，条目列表编号）按显示的索引号引用文件。

标准 shell 命令可以直接在 clifm 中使用，内置命令则提供额外的文件管理能力，例如批量重命名、回收站支持、书签和目录跳转。该工具支持多个工作区、自定义 profile 和插件系统。

clifm 可运行于 Linux、BSD、macOS 甚至 VT100 终端，是现有可移植性最高的文件管理器之一。其 CLI 优先的方式特别适合已经习惯 shell 环境的用户。

# PARAMETERS

**-a**, **--show-hidden**
> 显示隐藏文件

**-P** _profile_
> 使用指定的 profile

**-S**, **--stealth-mode**
> 不留下任何痕迹

**-p** _path_
> 设置起始路径

**-c** _cmd_
> 运行命令后退出

**-w** _workspace_
> 在指定工作区中启动

**--no-cd-auto**
> 禁用自动 cd

**--disk-usage**
> 显示磁盘用量

# NAVIGATION

**ELN**
> 输入编号选择文件/目录

**b/f**
> 在历史记录中后退/前进

**j** _pattern_
> 跳转到目录

**/pattern**
> 过滤条目

# COMMANDS

标准 shell 命令均可使用。内置命令：
- **sel/desel**：选中/取消选中文件
- **tr**：将文件移入回收站
- **o/open**：用默认应用打开
- **bulk**：批量重命名

**help** 或 **?**
> 显示帮助

# CONFIGURATION

**~/.config/clifm/profiles/<profile>/clifmrc**
> 主配置文件，控制颜色、别名、提示符和行为设置。

**~/.config/clifm/profiles/<profile>/keybindings.clifm**
> 自定义键盘快捷键和按键绑定。

# CAVEATS

基于 CLI 而非 TUI。shell 命令可直接使用。可通过 profile 高度定制。

# INSTALL

```dnf: sudo dnf install clifm```

```apk: sudo apk add clifm```

```brew: brew install clifm```

```nix: nix profile install nixpkgs#clifm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ranger](/man/ranger)(1), [lf](/man/lf)(1), [nnn](/man/nnn)(1)

# RESOURCES

```[Source code](https://github.com/leo-arch/clifm)```

<!-- verified: 2026-06-22 -->
