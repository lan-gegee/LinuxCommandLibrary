# TAGLINE

支持模糊搜索的 Wayland 应用启动器

# TLDR

**运行**应用

```fuzzel```

以 **dmenu 模式**运行 fuzzel

```fuzzel -d```

把某个命令的输出显示为**菜单**

```ls | fuzzel -d```

显示以换行分隔的**自定义选项**菜单

```echo -e "red\ngreen\nblue" | fuzzel -d```

让用户在选项中选择并**保存**所选项目

```echo -e "red\ngreen\nblue" | fuzzel -d > color.txt```

**重置**应用使用计数

```rm -v $HOME/.cache/fuzzel```

在**指定显示器**上启动 fuzzel

```fuzzel -o "DP-1"```

用 fuzzel 进行**在线搜索**

```fuzzel -d -l 0 --placeholder "Type your search" | xargs firefox --search```

# SYNOPSIS

**fuzzel** [_options_]

# PARAMETERS

**-d**, **--dmenu**
> 以 dmenu 模式运行，从 stdin 读取条目

**-o**, **--output** _OUTPUT_
> 在指定的 Wayland output（显示器）上显示

**-l**, **--lines** _N_
> 最大显示行数（0 表示单行）

**-w**, **--width** _N_
> 窗口宽度（字符数）

**-f**, **--font** _FONT_
> 字体规格

**-b**, **--background** _COLOR_
> 背景颜色，RRGGBBAA 格式

**-t**, **--text-color** _COLOR_
> 文本颜色，RRGGBBAA 格式

**-p**, **--prompt** _TEXT_
> 设置提示符文本

**--placeholder** _TEXT_
> 输入为空时的占位文本

**-i**, **--icon-theme** _THEME_
> 图标主题名称

**-T**, **--terminal** _CMD_
> 启动终端应用所用的终端命令

# CONFIGURATION

**~/.config/fuzzel/fuzzel.ini**
> 外观、行为、按键绑定及默认选项。

**~/.cache/fuzzel**
> 记录使用频率，用于应用排序。

# DESCRIPTION

**fuzzel** 是一款 Wayland 原生的应用启动器，支持模糊匹配，灵感来自 rofi 和 dmenu。它会扫描 XDG 应用目录，并列出已安装应用的可搜索清单。

在 dmenu 模式（**-d**）下，fuzzel 从 stdin 读取条目并将选中的条目输出到 stdout，非常适合脚本编写和构建交互式菜单。其模糊匹配算法优先匹配词边界和字符串开头的命中。

配置保存在 **~/.config/fuzzel/fuzzel.ini**，可为外观、行为和按键绑定提供大量自定义选项。

# CAVEATS

仅支持 Wayland，不能在 X11 上运行。应用图标需要已安装图标主题。缓存文件 **~/.cache/fuzzel** 记录使用频率用于排序，删除即可重置。

# HISTORY

fuzzel 由 Daniel Eklof（foot 终端的同一开发者）创建，首次发布于 **2020 年**前后。它是专为 Wayland 合成器设计的 rofi 轻量替代品，而 rofi 主要面向 X11。

# INSTALL

```apt: sudo apt install fuzzel```

```dnf: sudo dnf install fuzzel```

```pacman: sudo pacman -S fuzzel```

```apk: sudo apk add fuzzel```

```zypper: sudo zypper install fuzzel```

```nix: nix profile install nixpkgs#fuzzel```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rofi](/man/rofi)(1), [dmenu](/man/dmenu)(1), [wofi](/man/wofi)(1), [bemenu](/man/bemenu)(1)

# RESOURCES

```[Source code](https://codeberg.org/dnkl/fuzzel)```

<!-- verified: 2026-07-15 -->
