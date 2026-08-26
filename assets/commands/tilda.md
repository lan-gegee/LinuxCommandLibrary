# TAGLINE

下拉式终端模拟器

# TLDR

**启动 Tilda 终端**

```tilda```

在 Wayland 上**以 D-Bus 支持启动**

```tilda --dbus```

**切换特定 Tilda 实例**

```tilda -T [0]```

**隐藏启动**

```tilda --hidden```

**使用指定配置文件**

```tilda -c [~/.config/tilda/config_0]```

**显示版本**

```tilda --version```

**显示帮助**

```tilda --help```

# SYNOPSIS

**tilda** [_options_]

# PARAMETERS

**--dbus**
> 启用 D-Bus 接口，用于切换窗口。

**-T**, **--toggle** _n_
> 切换实例 n 的可见性。

**--hidden**
> 以隐藏窗口方式启动。

**-c**, **--config** _file_
> 使用指定的配置文件。

**-C**
> 打开配置向导（已废弃，请使用右键菜单）。

**--version**
> 显示版本信息。

**-h**, **--help**
> 显示帮助信息。

# KEYBOARD SHORTCUTS

**F1**：下拉/收回终端（默认热键）

**Shift+Ctrl+T**：打开新标签页

**Shift+Ctrl+W**：关闭当前标签页

**Shift+Ctrl+PageUp**：将标签页左移

**Shift+Ctrl+PageDown**：将标签页右移

**Shift+Ctrl+C**：复制选中文本

**Shift+Ctrl+V**：粘贴剪贴板内容

**Shift+Ctrl+F**：搜索

**F11**：切换全屏

**F12**：切换透明度

**Shift+Ctrl+Q**：退出 Tilda

# DESCRIPTION

**Tilda** 是一款基于 GTK 的 Linux 下拉式终端模拟器。按下热键时，它会从屏幕顶部滑下，类似于 Quake 风格游戏中的控制台。

该终端支持标签页、透明度和自定义外观，还可以配置为失去焦点时自动隐藏。配置通过右键点击终端窗口打开的首选项对话框完成。

多个 Tilda 实例可以同时运行，每个实例使用自己的配置文件（config_0、config_1 等），存放在 ~/.config/tilda/ 目录中。D-Bus 接口支持与桌面环境集成以实现全局热键，这在 Wayland 上尤其有用。

# CAVEATS

在 Wayland 上需要 --dbus 标志并配置桌面环境热键。第一个实例使用 config_0。全局热键可能与其他应用冲突。部分透明特性需要支持合成的窗口管理器。

# HISTORY

**Tilda** 的灵感来自 Quake 等第一人称射击游戏中的下拉控制台。它的设计目标是无需管理独立窗口即可快速访问终端。该项目仍在持续维护，已支持 Wayland 兼容等现代特性。

# INSTALL

```apt: sudo apt install tilda```

```dnf: sudo dnf install tilda```

```pacman: sudo pacman -S tilda```

```apk: sudo apk add tilda```

```zypper: sudo zypper install tilda```

```nix: nix profile install nixpkgs#tilda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[guake](/man/guake)(1), [yakuake](/man/yakuake)(1), [gnome-terminal](/man/gnome-terminal)(1), [xterm](/man/xterm)(1)
