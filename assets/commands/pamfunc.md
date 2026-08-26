# TAGLINE

应用数学函数变换像素

# TLDR

**乘以像素值**

```pamfunc -multiplier=[1.5] [input.pam] > [output.pam]```

**加到像素值上**

```pamfunc -adder=[50] [input.pam] > [output.pam]```

**应用幂函数**

```pamfunc -power=[2.2] [input.pam] > [output.pam]```

# SYNOPSIS

**pamfunc** [_options_] [_file_]

# PARAMETERS

_FILE_
> 输入的 PAM/PNM 文件。

**-multiplier** _FACTOR_
> 将像素值乘以系数。

**-adder** _VALUE_
> 将像素值加上数值。

**-power** _EXPONENT_
> 应用幂函数。

**-divisor** _VALUE_
> 将像素值除以数值。

# DESCRIPTION

**pamfunc** 应用数学函数，对像素值进行变换。

该工具对图像执行算术运算。属于 Netpbm 工具集。

# CAVEATS

属于 Netpbm 工具集。计算结果会被钳制到有效范围内。

# HISTORY

pamfunc 是 **Netpbm** 中用于数学图像变换的工具。

# INSTALL

```apt: sudo apt install netpbm```

```dnf: sudo dnf install netpbm```

```pacman: sudo pacman -S netpbm```

```apk: sudo apk add netpbm```

```zypper: sudo zypper install netpbm```

```brew: brew install netpbm```

```nix: nix profile install nixpkgs#netpbm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pamarith](/man/pamarith)(1), [pnmgamma](/man/pnmgamma)(1), [netpbm](/man/netpbm)(1)
