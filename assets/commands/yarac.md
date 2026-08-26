# TAGLINE

将 YARA 规则编译为二进制格式

# TLDR

**编译规则**

```yarac [rules.yar] [rules.yarc]```

**编译多个文件**

```yarac [rule1.yar] [rule2.yar] [output.yarc]```

**显示警告**

```yarac -w [rules.yar] [output.yarc]```

# SYNOPSIS

**yarac** [_-w_] [_options_] _rules_ _output_

# PARAMETERS

**-w**
> 显示警告。

**-d** _VAR=VAL_
> 定义变量。

**--help**
> 显示帮助。

# DESCRIPTION

**yarac** 将 YARA 规则源文件编译为优化的二进制格式。预编译的规则加载速度明显快于每次解析源文件，这在扫描大量文件集或在生产系统上运行规则时尤为重要。

多个规则文件可以合并为单个编译输出，将整个规则集整合为一个可部署的二进制文件。可以使用 **-d** 在编译时定义外部变量，从而在不修改源码的情况下参数化规则。

编译后的规则文件不能跨不同的 YARA 版本移植，因此升级 YARA 后必须重新编译规则。**-w** 标志可在编译期间启用警告，在部署前发现规则定义中的潜在问题。

# CAVEATS

需要安装 YARA。规则语法必须有效。编译后的二进制文件不能跨版本移植。

# HISTORY

**yarac** 是 **YARA** 的一部分，YARA 是一款面向恶意软件研究人员的模式匹配工具。

# INSTALL

```apt: sudo apt install yara```

```dnf: sudo dnf install yara```

```pacman: sudo pacman -S yara```

```apk: sudo apk add yara```

```zypper: sudo zypper install yara```

```brew: brew install yara```

```nix: nix profile install nixpkgs#yara```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[yara](/man/yara)(1), [clamav](/man/clamav)(1)
