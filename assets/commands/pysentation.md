# TAGLINE

在终端中展示 Python 编写的演示文稿的 CLI

# TLDR

**显示演示文稿文件**

```pysentation [presentation.py]```

**从指定幻灯片开始显示**

```pysentation [presentation.py] -s [3]```

# SYNOPSIS

**pysentation** [_options_] _file_

# PARAMETERS

**-s** _NUMBER_
> 从指定的幻灯片编号开始。

# DESCRIPTION

**pysentation** 是一个 CLI，用于在终端中展示以 Python 文件或 **.pysent** 文件编写的演示文稿。幻灯片通过源文件中特殊的 pysentation 命令定义。当 interpretable 属性启用时，幻灯片内的代码会被 Python 解释器执行，输出显示在单独的框中。

# CAVEATS

演示文稿文件必须遵循 pysentation 的幻灯片定义格式。需要 Python。

# HISTORY

**pysentation** 由 **mimseyedi** 创建，使用 **Python** 编写。

# INSTALL

```nix: nix profile install nixpkgs#pysentation```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[patat](/man/patat)(1), [slides](/man/slides)(1), [presenterm](/man/presenterm)(1)
