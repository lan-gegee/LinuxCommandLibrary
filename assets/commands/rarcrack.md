# TAGLINE

针对归档的暴力破解密码恢复工具

# TLDR

**破解 RAR 密码**

```rarcrack [archive.rar]```

**破解 ZIP 密码**

```rarcrack [archive.zip] --type zip```

**破解 7z 密码**

```rarcrack [archive.7z] --type 7z```

**设置线程数**

```rarcrack [archive.rar] --threads [4]```

**设置字符集**

```rarcrack [archive.rar] --charset [abc123]```

**继续破解**

```rarcrack [archive.rar]```

# SYNOPSIS

**rarcrack** _archive_ [_--type_ _format_] [_--threads_ _n_] [_--charset_ _chars_]

# PARAMETERS

**--type** _FORMAT_
> 归档类型（rar、zip、7z）。未指定时根据文件扩展名自动检测。

**--threads** _N_
> 并行测试密码的线程数。

**--charset** _CHARS_
> 暴力破解尝试使用的字符。缩小该集合能显著减少搜索空间。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**rarcrack** 通过暴力尝试所有可能的字符组合，从加密的 RAR、ZIP 和 7Z 归档中恢复密码。它会按长度递增的顺序系统地尝试来自可配置字符集的密码，归档类型可根据文件扩展名自动检测，也可显式指定。

该工具会自动将进度保存到归档旁边的 XML 状态文件中，中断的会话可以从上次测试的位置恢复，而不必从头开始。多线程功能将密码测试分配到可用的 CPU 核心以提升吞吐量。当密码构成部分已知时，用 **--charset** 缩小字符集可以显著减少搜索空间。

# CAVEATS

对于较长的密码，暴力破解非常缓慢。仅限经授权的恢复用途。强密码可能不切实际。

# HISTORY

**rarcrack** 为从加密归档中恢复密码而生。它为 RAR、ZIP 和 7Z 文件提供了一个简单的暴力破解工具。

# INSTALL

```apt: sudo apt install rarcrack```

```pacman: sudo pacman -S rarcrack```

```nix: nix profile install nixpkgs#rarcrack```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[john](/man/john)(1), [hashcat](/man/hashcat)(1), [zip2john](/man/zip2john)(1), [rar2john](/man/rar2john)(1)
