# TAGLINE

为 diff 输出添加彩色语法高亮的包装器

# TLDR

**以彩色输出比较文件**

```colordiff [file1] [file2]```

**统一 diff 格式**

```colordiff -u [file1] [file2]```

**将 diff 输出通过管道交给 colordiff**

```diff -u [file1] [file2] | colordiff```

**并排比较**

```colordiff -y [file1] [file2]```

**比较目录**

```colordiff -r [dir1] [dir2]```

**配合分页器查看**

```colordiff [file1] [file2] | less -R```

# SYNOPSIS

**colordiff** [_diff_options_] _file1_ _file2_

# DESCRIPTION

**colordiff** 是 diff 的一个包装器，输出内容与 diff 相同，但附带彩色语法高亮。在命令行查看差异时，颜色能提升可读性。

除 colordiff 特有选项外，所有选项都会原样传递给 diff。

# PARAMETERS

支持所有 diff 选项，另有：

**--difftype**=_type_
> 指定 diff 类型：diff、diffc、diffu、diffy、wdiff、debdiff

标准 diff 选项：

**-u**
> 统一格式

**-c**
> 上下文格式

**-y**
> 并排显示

**-r**
> 递归比较目录

# CONFIGURATION

**/etc/colordiffrc**
> 系统级配置

**~/.colordiffrc**
> 用户配置

配置文件可为以下元素设置颜色：
- 普通文本
- 新文本（新增）
- 旧文本（删除）
- diff 命令行

# PAGER USAGE

使用 **less -R** 以保留 ANSI 颜色：

```colordiff file1 file2 | less -R```

# ALTERNATIVE

新版 diff（3.4+）支持内置颜色：

```diff --color file1 file2```

# CAVEATS

使用 Perl 编写。需要终端支持 ANSI 颜色（如 xterm 等）。颜色可通过配置文件自定义。

# INSTALL

```dnf: sudo dnf install colordiff```

```pacman: sudo pacman -S colordiff```

```apk: sudo apk add colordiff```

```zypper: sudo zypper install colordiff```

```brew: brew install colordiff```

```nix: nix profile install nixpkgs#colordiff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [git-diff](/man/git-diff)(1), [vimdiff](/man/vimdiff)(1)

# RESOURCES

```[Source code](https://github.com/daveewart/colordiff)```

```[Homepage](https://www.colordiff.org/)```

<!-- verified: 2026-06-22 -->
