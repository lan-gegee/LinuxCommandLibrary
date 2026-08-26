# TAGLINE

从命令行查询、编译和测试 XKB 键盘映射

# TLDR

**列出**所有可用的 XKB 规则、型号、布局、变体和选项

```xkbcli list```

**编译**当前活动的系统键盘映射并转储到 stdout

```xkbcli compile-keymap```

**使用指定的布局/变体编译键盘映射**

```xkbcli compile-keymap --layout [us] --variant [dvorak]```

**显示如何输入**特定 Unicode 码点

```xkbcli how-to-type [0x00e9]```

在 **Wayland** 下交互式调试 XKB 键盘映射

```xkbcli interactive-wayland```

在 **X11** 下交互式调试 XKB 键盘映射

```xkbcli interactive-x11```

从 **evdev** 读取并交互式调试 XKB 键盘映射（需要 root 权限）

```sudo xkbcli interactive-evdev```

**打印** libxkbcommon 的版本

```xkbcli --version```

# SYNOPSIS

**xkbcli** _command_ [_arguments_]

**xkbcli** [**--help** | **--version**]

# PARAMETERS

**--help**
> 显示用法并退出。

**--version**
> 打印 libxkbcommon 版本并退出。

# SUBCOMMANDS

**compile-keymap**
> 将 RMLVO（rules + model + layout + variant + options）键盘映射源编译为键映射文本格式并打印。接受 **--rules**、**--model**、**--layout**、**--variant**、**--options** 和 **--keymap**。

**compile-compose**
> 编译 Compose 文件并打印生成的 Compose 表。

**how-to-type** _codepoint_
> 显示产生给定 Unicode 码点的所有按键组合（十进制或 **0x** 十六进制）。

**interactive-evdev**
> 交互式 XKB 调试器，从 **/dev/input/eventN** 读取原始事件；通常需要 root 权限或加入 **input** 组。

**interactive-x11**
> 使用实时 X11 键盘映射的交互式 XKB 调试器。

**interactive-wayland**
> 使用实时 Wayland 键盘映射的交互式 XKB 调试器。

**list**
> 打印 libxkbcommon 已知的所有规则、型号、布局、变体和选项。可选择用 **--ruleset** 过滤。

# DESCRIPTION

**xkbcli** 是 **libxkbcommon** 附带的面向用户的前端。libxkbcommon 是 Wayland 合成器、X.Org 服务器（自 1.20 起）、GTK、Qt、EFL 以及大多数现代工具包使用的键盘映射库。它把该库的编译、查找和检查 API 封装为一个带有子命令的单一多路复用二进制文件。

它最常见的用法有三种。第一，**xkbcli list** 回答"我的系统认识哪些布局/变体？"——与图形化键盘选择器显示的数据相同，但以机器可解析的形式呈现。第二，**xkbcli compile-keymap** 可以完全复现合成器或 X server 编译键盘映射时所做的操作，这在诊断自定义布局为何未生效时非常宝贵。第三，**interactive-*** 子命令会打印每次按键产生的实时键符号（keysym）、修饰键状态、分组和 Unicode 码点，使 **xkbcli** 成为 libxkbcommon 时代的 **xev**(1) 等价物。

该工具依赖系统的 **xkeyboard-config** 数据文件（通常位于 **/usr/share/X11/xkb** 下），因此其输出反映了任何基于 libxkbcommon 的程序所看到的键盘映射。

# CAVEATS

**interactive-evdev** 读取内核原始输入事件，因此需要对 **/dev/input/event\*** 的读权限；在大多数发行版上这意味着 **root** 或 **input** 组成员身份。**interactive-wayland** 和 **interactive-x11** 仅在编译时其对应头文件可用的情况下才会构建，因此在精简安装上可能缺失。**list** 子命令显示的是系统附带的配置，而非当前生效的配置——后者请查看合成器或 **setxkbmap -query**。

# HISTORY

**libxkbcommon** 于 **2012** 年由 **Daniel Stone** 和 **Ran Benita** 从 **libxkbfile**/**xkbcomp** 分叉而来，旨在提供一个不依赖 X server 的现代 XKB 实现，供 Wayland 合成器使用。**xkbcli** 总控工具是后来添加的，作为这一系列调试工具的统一入口（取代了各自独立的 **xkbcompose**、**xkbgetkeymap** 等）。如今每个主要 Linux 发行版都以 **libxkbcommon-tools** / **libxkbcommon-utils** 软件包的形式分发它。

# INSTALL

```apt: sudo apt install libxkbcommon-tools```

```apk: sudo apk add xkbcli```

```zypper: sudo zypper install libxkbcommon-tools```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xkbcomp](/man/xkbcomp)(1), [setxkbmap](/man/setxkbmap)(1), [xev](/man/xev)(1), [localectl](/man/localectl)(1)
