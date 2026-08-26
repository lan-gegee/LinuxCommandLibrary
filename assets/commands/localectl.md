# TAGLINE

查询和更改系统的 locale 与键盘布局设置

# TLDR

显示当前的 **locale 和键位映射**设置

```localectl```

列出可用的 **locale**

```localectl list-locales```

设置**系统 locale** 变量

```localectl set-locale LANG=en_US.UTF-8```

列出可用的**键位映射**

```localectl list-keymaps```

设置系统**键盘映射**

```localectl set-keymap us```

设置 **X11 键盘布局**

```localectl set-x11-keymap us pc105```

# SYNOPSIS

**localectl** [_OPTIONS_] [_COMMAND_]

# DESCRIPTION

**localectl** 查询和更改系统的 locale 与键盘布局设置。它通过 systemd-localed 同时控制控制台和 X11 的键盘映射。

# COMMANDS

**status**
> 显示当前 locale 和键位映射设置

**set-locale LOCALE...**
> 设置系统 locale 变量（LANG、LC_* 等）

**list-locales**
> 列出可用的 locale

**set-keymap MAP [TOGGLEMAP]**
> 设置控制台键盘映射

**list-keymaps**
> 列出可用的控制台键位映射

**set-x11-keymap LAYOUT [MODEL [VARIANT [OPTIONS]]]**
> 设置 X11 键盘映射

**list-x11-keymap-models**
> 列出 X11 键盘型号

**list-x11-keymap-layouts**
> 列出 X11 键盘布局

**list-x11-keymap-variants [LAYOUT]**
> 列出 X11 键盘变体

**list-x11-keymap-options**
> 列出 X11 键盘选项

# PARAMETERS

**--no-ask-password**
> 不提示输入密码

**--no-convert**
> 不在控制台键位映射与 X11 之间互相转换

**-H, --host**
> 在远程主机上执行操作

**-M, --machine**
> 在容器中执行操作

# COMMON LOCALE VARIABLES

**LANG**: 所有类别的默认 locale
**LC_COLLATE**: 字符串排序规则
**LC_CTYPE**: 字符分类
**LC_MESSAGES**: 消息语言
**LC_NUMERIC**: 数字格式
**LC_TIME**: 日期和时间格式

# CAVEATS

使用 set-keymap 设置控制台键位映射时会自动更新 X11 键位映射，除非使用了 **--no-convert**。更改对新会话立即生效。

# HISTORY

**localectl** 是 **systemd** 的组成部分，通过 systemd-localed 提供统一的 locale 和键位映射管理。

# INSTALL

```apt: sudo apt install systemd```

```dnf: sudo dnf install systemd```

```pacman: sudo pacman -S systemd```

```zypper: sudo zypper install systemd```

```brew: brew install systemd```

```nix: nix profile install nixpkgs#systemd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[locale](/man/locale)(1), [loadkeys](/man/loadkeys)(1)
