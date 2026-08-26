# TAGLINE

为控制台加载键盘翻译表

# TLDR

加载**键盘布局**

```sudo loadkeys [en|de|dvorak]```

加载**默认**键位映射

```sudo loadkeys --default```

为**特定控制台**加载键位映射

```sudo loadkeys -C /dev/ttyN [layout]```

从**文件**加载

```sudo loadkeys -C /dev/ttyN [path/to/keymap]```

创建**二进制**键位映射

```loadkeys --bkeymap > [output.bmap]```

仅**解析**键位映射而不加载

```loadkeys --parse [keymap]```

# SYNOPSIS

**loadkeys** [_options_] [_keymap_...]

# DESCRIPTION

**loadkeys** 读取键位映射文件并将键盘翻译表加载到内核中，从而更改虚拟控制台的键盘布局。

# PARAMETERS

**-d, --default**
> 加载默认键位映射

**-C, --console DEVICE**
> 指定目标控制台设备

**-m, --mktable**
> 输出内核源码格式的表格

**-b, --bkeymap**
> 输出二进制键位映射

**-p, --parse**
> 仅解析键位映射而不加载

**-q, --quiet**
> 抑制所有正常输出

**-u, --unicode**
> 强制 Unicode 模式

**-a, --ascii**
> 强制转换为 ASCII

**-s, --clearstrings**
> 清空内核字符串表

**-c, --clearcompose**
> 清空内核重音符号表

**-t, --tkeymap** _[shape]_
> 输出文本键位映射（可选形状：2、4、8、16）

**-V, --version**
> 显示版本号并退出

# CAVEATS

只影响 Linux 虚拟控制台，不影响 X11 或 Wayland。更改会同时应用于所有虚拟控制台并持续到重启。任何对 /dev/console 有读权限的人都可以运行 loadkeys。

# INSTALL

```apt: sudo apt install kbd```

```dnf: sudo dnf install kbd```

```pacman: sudo pacman -S kbd```

```apk: sudo apk add kbd```

```zypper: sudo zypper install kbd```

```nix: nix profile install nixpkgs#kbd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dumpkeys](/man/dumpkeys)(1), [showkey](/man/showkey)(1), [setxkbmap](/man/setxkbmap)(1), [localectl](/man/localectl)(1)
