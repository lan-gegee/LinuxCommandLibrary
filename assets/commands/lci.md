# TAGLINE

LOLCODE 解释器，LOLCODE 是一种受 lolcat 启发的深奥编程语言

# TLDR

**运行** LOLCODE 文件

```lci [path/to/file.lol]```

显示**帮助**

```lci -h```

显示**版本**

```lci -v```

# SYNOPSIS

**lci** [_options_] _file_

# PARAMETERS

**-h**, **--help**
> 显示帮助信息

**-v**, **--version**
> 显示版本信息

# DESCRIPTION

**lci** 是 LOLCODE 的解释器。LOLCODE 是一种受 lolcat 梗图和网络幽默启发的深奥编程语言，使用 lol 语体风格的语法来编写程序。

LOLCODE 示例：
```
HAI 1.2
  VISIBLE "HAI WORLD!"
KTHXBYE
```

# CAVEATS

LOLCODE 是一种玩笑性质的语言，并非为严肃开发而设计。其规范并不正式，不同实现之间可能存在差异。主要用于娱乐和教育目的。

# HISTORY

LOLCODE 由 Adam Lindsay 于 **2007 年**在兰卡斯特大学创造，是一种幽默编程语言。lci 解释器由 Justin Meza 开发，提供了基于 C 的实现。

# INSTALL

```brew: brew install lci```

```nix: nix profile install nixpkgs#lci```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[python](/man/python)(1), [perl](/man/perl)(1), [ruby](/man/ruby)(1)
