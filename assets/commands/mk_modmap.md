# TAGLINE

将 Linux 键表文件转换为 xmodmap 文件

# TLDR

**将 Linux 控制台键映射**转换为 xmodmap 格式

```mk_modmap [keymap_file]```

**将输出保存**到文件

```mk_modmap [keymap_file] > [keymap.xmodmap]```

**以详细输出进行转换**

```mk_modmap -v [keymap_file]```

**转储当前键映射**并转换

```dumpkeys | mk_modmap```

# SYNOPSIS

**mk_modmap** [**-v**] _keymap_file_

# PARAMETERS

**-v**
> 转换过程中输出详细信息。

_keymap_file_
> 一个 Linux 控制台键表文件（由 `dumpkeys` 生成，或位于 `/usr/share/keymaps` 下）。

# DESCRIPTION

**mk_modmap** 将 Linux 控制台键表文件转换为可被 **xmodmap** 解析并在 X11 中使用的文件。转换结果写入标准输出。构建时需要安装 X11 头文件。

该工具属于 **xkeycaps** 软件包。现代 X.Org 版本会从当前活动的 Linux 键映射初始化其键映射，因此在当代系统上很少需要 mk_modmap。

# CAVEATS

X11 专用。输出供 xmodmap 使用。并非所有控制台按键操作都有对应的 xmodmap 等价物。在现代 X.Org 和 Wayland 环境中基本已过时。

# HISTORY

mk_modmap 随 **xkeycaps** 发布，最初由 Jamie Zawinski 编写。它可追溯到 X11/Linux 早期，当时控制台和 X 服务器的键盘布局是分开配置的。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xmodmap](/man/xmodmap)(1), [xev](/man/xev)(1), [setxkbmap](/man/setxkbmap)(1)
