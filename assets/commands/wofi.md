# TAGLINE

Wayland 应用启动器

# TLDR

显示**应用**列表

```wofi -S drun```

显示**所有**命令

```wofi -S run```

从标准输入进入 **Dmenu** 模式

```printf "Choice1\nChoice2\nChoice3" | wofi -d```

# SYNOPSIS

**wofi** [_OPTIONS_]

# PARAMETERS

**-S, --show** _MODE_
> 显示模式：drun（应用）、run（命令）、dmenu

**-d, --dmenu**
> 以 dmenu 模式运行（从标准输入读取）

**--style** _FILE_
> 自定义 CSS 样式表

**--conf** _FILE_
> 配置文件

# DESCRIPTION

**wofi** 是面向基于 wlroots 的 Wayland 合成器的应用启动器。它的功能与 rofi 和 dmenu 类似，提供一个可搜索的菜单，用于启动应用程序或选择条目。

drun 模式显示桌面应用程序，而 run 模式显示 PATH 中的所有可执行文件。

# CAVEATS

仅支持 Wayland（基于 wlroots 的合成器）。样式使用 CSS 定义。某些 rofi 功能可能不可用。

# INSTALL

```apt: sudo apt install wofi```

```dnf: sudo dnf install wofi```

```pacman: sudo pacman -S wofi```

```apk: sudo apk add wofi```

```zypper: sudo zypper install wofi```

```nix: nix profile install nixpkgs#wofi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rofi](/man/rofi)(1), [dmenu](/man/dmenu)(1), [fuzzel](/man/fuzzel)(1)
