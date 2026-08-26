# TAGLINE

控制台键盘转换表导出工具

# TLDR

**导出当前键盘映射**

```dumpkeys```

**以完整格式导出**

```dumpkeys --full-table```

**只显示按键定义**

```dumpkeys --keys-only```

**导出功能键字符串**

```dumpkeys --funcs-only```

**以数字（十六进制）形式输出动作码**

```dumpkeys -n```

**将键盘映射保存到文件**

```dumpkeys > [keymap.map]```

# SYNOPSIS

**dumpkeys** [_options_]

# PARAMETERS

**-f**, **--full-table**
> 以规范形式输出所有按键绑定（keymaps 行加上所有修饰键组合对应的行）。

**-1**, **--separate-lines**
> 每个（修饰键, 键码）对占一行；普通键码加 "plain" 前缀。

**-S** _shape_, **--shape**=_shape_
> 选择输出格式：2（默认）、4（每个键码一行）、8（每个修饰键-键码一行）或 16（遇到第一个空缺即停止）。

**-n**, **--numeric**
> 以十六进制而非符号记法输出动作码。

**-t**, **--funcs-only**
> 只输出功能键字符串定义。

**-k**, **--keys-only**
> 只输出按键绑定，不包括功能键字符串。

**-d**, **--compose-only**
> 只输出组合键序列（需要内核组合键支持）。

**-c** _charset_, **--charset**=_charset_
> 使用给定字符集解释字符编码（iso-8859-1..iso-8859-9）。

**-C** _dev_, **--console**=_dev_
> 针对指定的控制台设备。

**-i**, **--short-info**
> 显示键盘驱动特征（键码范围、可绑定的动作、功能键数量）。

**-l**, **-s**, **--long-info**
> 显示长格式信息：短格式信息外加动作符号及取值列表。

**-v**, **--verbose**
> 启用详细输出。

**-V**, **--version**
> 打印版本信息并退出。

# DESCRIPTION

**dumpkeys** 输出 Linux 控制台当前使用的键盘转换表。其输出格式与 **loadkeys** 兼容，因此键盘映射可以被保存、修改和恢复。

该命令读取内核键盘驱动的数据，生成一个键映射文件，展示每个按键及修饰键组合所绑定的动作。它用于控制台键盘的自定义。

# OUTPUT FORMAT

```
keycode  28 = Return
keycode  57 = space
keycode  14 = Delete BackSpace
shift keycode  14 = Delete
```

# CAVEATS

只能在 Linux 控制台上工作，不适用于 X11 或 Wayland。需要访问控制台设备。输出格式随选项而异。各虚拟终端共享同一份键盘映射。请使用 loadkeys 恢复或修改键盘映射。

# HISTORY

dumpkeys 是 Linux 控制台键盘工具集 **kbd** 软件包的一部分。自 **20 世纪 90 年代初**起，它便作为 loadkeys 的配套工具被纳入各个 Linux 发行版，提供导出和备份键盘配置的途径。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[loadkeys](/man/loadkeys)(1), [showkey](/man/showkey)(1), [setxkbmap](/man/setxkbmap)(1)
