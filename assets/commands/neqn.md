# TAGLINE

为 nroff 格式化数学公式

# TLDR

**为 nroff 格式化公式**

```neqn [input.eqn] | nroff```

**配合 groff 处理**

```neqn [file] | groff -Tascii```

**仅检查语法**

```neqn -C [file]```

# SYNOPSIS

**neqn** [_options_] [_files_]

# PARAMETERS

_FILES_
> 含公式的输入文件。

**-C**
> 启用兼容模式。

**-N**
> 不允许在定界符中出现换行。

**--help**
> 显示帮助信息。

# DESCRIPTION

**neqn** 为 nroff 格式化数学公式。它是 eqn 的 ASCII 版本。

该工具处理公式标记。输出基于文本的数学排版。

# CAVEATS

属于 groff 的一部分。仅支持 ASCII 输出。需要排版输出请使用 eqn。

# HISTORY

neqn 是 **troff/nroff** 系统的一部分，源自最初的 Unix 公式格式化工具。

# INSTALL

```apt: sudo apt install groff-base```

```dnf: sudo dnf install groff-base```

```pacman: sudo pacman -S groff```

```apk: sudo apk add groff```

```zypper: sudo zypper install groff```

```brew: brew install groff```

```nix: nix profile install nixpkgs#groff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[eqn](/man/eqn)(1), [nroff](/man/nroff)(1), [groff](/man/groff)(1)
