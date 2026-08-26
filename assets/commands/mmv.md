# TAGLINE

批量移动和重命名文件

# TLDR

**按模式重命名**

```mmv '[*.txt]' '#1.bak'```

**移动文件**

```mmv '[dir1/*.c]' 'dir2/#1.c'```

**将文件名转为小写**

```mmv '[*]' '#l1'```

**预览变更**

```mmv -n '[*.JPG]' '#1.jpg'```

**强制覆盖**

```mmv -o '[*.old]' '#1.new'```

# SYNOPSIS

**mmv** [_options_] _from_ _to_

# PARAMETERS

_FROM_
> 源模式。

_TO_
> 目标模式。

**-n**
> 试运行（不实际执行）。

**-o**
> 覆盖已存在的文件。

**-v**
> 详细输出。

**--help**
> 显示帮助信息。

# DESCRIPTION

**mmv** 使用类 shell 的通配符模式执行批量文件移动、复制、拼接和链接操作。它先用含通配符的 **from** 模式匹配源文件，再用 **to** 模式构造目标名称，其中 **#1**、**#2** 等分别指代源模式中各个通配符匹配到的文本。

目标模式中的特殊替换包括用于小写和大写转换的 **#l** 和 **#u**。该工具会在执行前规划所有操作，检测并解决冲突与循环。

# CAVEATS

其模式语法与标准 shell 通配符不同。执行前务必先用 **-n** 预览。必须给模式加引号，以防止 shell 展开。

# HISTORY

mmv 由 **Vladimir Lanin** 编写，发布于 **1990 年**。它通过模式匹配和替换提供批量文件操作能力。

# INSTALL

```apt: sudo apt install mmv```

```dnf: sudo dnf install mmv```

```zypper: sudo zypper install mmv```

```brew: brew install mmv```

```nix: nix profile install nixpkgs#mmv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rename](/man/rename)(1), [mv](/man/mv)(1), [prename](/man/prename)(1)
