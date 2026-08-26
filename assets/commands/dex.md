# TAGLINE

为 XDG 自启动程序执行 DesktopEntry

# TLDR

执行**自启动文件夹**中的所有程序

```dex -a```

在**指定文件夹**中执行

```dex -a -s [path/to/dir1]:[path/to/dir2]```

预览 **GNOME 特有的**自启动项

```dex -a -e GNOME```

预览**常规自启动**（dry run）

```dex -a -d```

预览**desktop entry 属性**

```dex -p Name [path/to/file.desktop]```

为可执行文件**创建** desktop entry

```dex -c [/usr/bin/program]```

在**指定终端**中执行

```dex --term [terminal] [path/to/file.desktop]```

# SYNOPSIS

**dex** [_options_] [_files_]

# DESCRIPTION

**dex**（DesktopEntry Execution）生成并执行 .desktop 文件。它通常用于运行 XDG 自启动程序，或通过 desktop entry 启动应用。

对于没有内置自启动支持的窗口管理器尤其有用。

# PARAMETERS

**-a, --autostart**
> 运行自启动目录中的程序

**-s, --search-paths** _paths_
> 冒号分隔的搜索路径

**-e, --environment** _env_
> 按桌面环境过滤

**-d, --dry-run**
> 只预览不执行

**-c, --create** _file_
> 创建 desktop entry

**-p, --property** _name_
> 显示属性值

**--term** _terminal_
> 为 Terminal=true 的条目指定使用的终端

# CAVEATS

Desktop entry 必须符合 XDG 规范。某些条目可能需要特定的桌面环境。自启动目录默认为 `~/.config/autostart` 和 `/etc/xdg/autostart`。

# INSTALL

```pacman: sudo pacman -S dex```

```apk: sudo apk add dex```

```zypper: sudo zypper install dex```

```brew: brew install dex```

```nix: nix profile install nixpkgs#dex```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdg-open](/man/xdg-open)(1), [update-desktop-database](/man/update-desktop-database)(1)
