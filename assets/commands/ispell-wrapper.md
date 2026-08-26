# TAGLINE

为多种拼写检查器提供统一接口

# TLDR

**用默认检查器检查文件**

```ispell-wrapper [file.txt]```

**强制使用指定检查器**

```ispell-wrapper --ispell=[aspell] [file.txt]```

**列出拼写错误的单词**

```ispell-wrapper -l < [file.txt]```

**使用指定词典**

```ispell-wrapper -d [english] [file.txt]```

# SYNOPSIS

**ispell-wrapper** [_options_] _file_...

# PARAMETERS

**--ispell** _CHECKER_
> 指定拼写检查器（aspell、hunspell、ispell）。

**-d** _DICT_
> 要使用的词典。

**-a**
> 管道模式。

**-l**
> 列表模式。

**--help**
> 显示帮助信息。

# DESCRIPTION

**ispell-wrapper** 为多种拼写检查器提供统一接口。它以一致的选项封装 aspell、hunspell 或 ispell。

该包装器会自动选择最佳可用检查器。无论安装的是哪个检查器，脚本都能正常工作。

# CAVEATS

仅适用于 Debian/Ubuntu。依赖于已安装的检查器。并非所有选项都能透传。

# HISTORY

ispell-wrapper 是为 **Debian** 创建的，用于在不同拼写检查程序之间提供兼容性。

# INSTALL

```apt: sudo apt install ispell```

```pacman: sudo pacman -S ispell```

```apk: sudo apk add aspell-compat```

```zypper: sudo zypper install ispell```

```brew: brew install ispell```

```nix: nix profile install nixpkgs#ispell```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ispell](/man/ispell)(1), [aspell](/man/aspell)(1), [hunspell](/man/hunspell)(1)
