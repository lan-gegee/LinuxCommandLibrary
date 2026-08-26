# TAGLINE

应用程序启动器与窗口切换器

# TLDR

**显示应用程序启动器**

```rofi -show drun```

**显示命令启动器**

```rofi -show run```

**在打开的窗口之间切换**

```rofi -show window```

**用作 dmenu 替代品**

```printf "Choice1\nChoice2\nChoice3" | rofi -dmenu```

**SSH 连接到主机**

```rofi -show ssh```

**使用指定主题**

```rofi -show drun -theme [solarized]```

# SYNOPSIS

**rofi** [**-show** _mode_] [**-dmenu**] [**-theme** _theme_]

# MODES

**drun**
> 桌面应用启动器。

**run**
> 命令启动器。

**window**
> 窗口切换器。

**ssh**
> SSH 连接管理器。

**keys**
> 快捷键查看器。

**combi**
> 组合模式。

# PARAMETERS

**-show _mode_**
> 显示指定模式。

**-dmenu**
> 作为 dmenu 替代品运行。

**-theme _theme_**
> 使用指定主题。

**-modi _modes_**
> 启用指定模式。

**-matching _method_**
> 匹配方法（fuzzy、regex、glob、normal）。

**-i**
> 不区分大小写的匹配。

# DESCRIPTION

**rofi** 是一款多用途的应用程序启动器和窗口切换器。它提供可搜索的界面，用于启动程序、切换窗口、运行命令等。

该工具可通过主题高度定制，并支持通过 dmenu 模式进行脚本扩展。它在平铺式窗口管理器配置中很受欢迎，常作为 dmenu 的替代品。

# CONFIGURATION

**~/.config/rofi/config.rasi**
> rasi 格式的主配置文件，控制模式、快捷键、匹配行为和默认设置。

**~/.config/rofi/themes/**
> 自定义主题文件目录，控制外观、颜色、字体和布局。

**~/.local/share/rofi/themes/**
> 用户安装主题的附加主题搜索路径。

# CAVEATS

默认需要 X11；Wayland 环境请使用 **rofi-wayland** 分支。主题使用 rasi 格式（不是 CSS）。自定义脚本可以通过 `-modi` 选项为 rofi 扩展新模式。dmenu 模式从 stdin 读取内容，并将选中的条目写入 stdout。

# HISTORY

**rofi** 由 **Dave Davenport** 创建，是功能比 dmenu 更丰富的替代品。它已成为许多 Linux 桌面配置中的标准组件。

# INSTALL

```apt: sudo apt install rofi```

```dnf: sudo dnf install rofi```

```pacman: sudo pacman -S rofi```

```apk: sudo apk add rofi-wayland```

```zypper: sudo zypper install rofi```

```brew: brew install rofi```

```nix: nix profile install nixpkgs#rofi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dmenu](/man/dmenu)(1), [wofi](/man/wofi)(1), [fuzzel](/man/fuzzel)(1)
