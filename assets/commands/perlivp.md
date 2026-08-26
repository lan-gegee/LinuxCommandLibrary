# TAGLINE

验证 Perl 安装是否正确

# TLDR

**运行安装验证**

```perlivp```

**以详细输出运行**

```perlivp -v```

**在运行前打印每项测试的说明**

```perlivp -p```

**同时启用前导说明和详细输出运行**

```perlivp -p -v```

# SYNOPSIS

**perlivp** [_options_]

# PARAMETERS

**-p**
> 在执行每项测试之前先打印对它的说明。

**-v**
> 在每项测试执行完毕后给出更详细的信息。

**-h**
> 打印简短的帮助信息。

# DESCRIPTION

**perlivp**（Perl Installation Verification Procedure，Perl 安装验证程序）测试 Perl 及其函数库是否安装正确。它在 Perl 源码构建时生成，应当在 `make install` 之后运行。

验证成功时会输出类似 `ok 1`、`ok 2` 的内容。

# CAVEATS

属于 Perl。只包含基础测试。请在安装之后运行。

# HISTORY

perlivp 属于 **Perl 核心**，用于安装验证。

# INSTALL

```apt: sudo apt install perl```

```dnf: sudo dnf install perl```

```pacman: sudo pacman -S perl```

```apk: sudo apk add perl-dev```

```zypper: sudo zypper install perl```

```brew: brew install perl```

```nix: nix profile install nixpkgs#perl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[perl](/man/perl)(1), [perldiag](/man/perldiag)(1)
