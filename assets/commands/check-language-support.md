# TAGLINE

找出缺失的语言支持软件包

# TLDR

显示**缺失的语言包**

```check-language-support```

列出**特定 locale** 的软件包

```check-language-support -l [en]```

除缺失的外同时显示**已安装的软件包**

```check-language-support --show-installed```

# SYNOPSIS

**check-language-support** [_options_]

# DESCRIPTION

**check-language-support** 在 Ubuntu 系统上找出缺失的语言支持软件包。它会分析已安装的软件和启用的 locale，推荐实现完整语言支持所需的额外软件包。

其中包括翻译、输入法、字体和拼写词典。

# PARAMETERS

**-l, --language** _locale_
> 检查特定语言/locale

**--show-installed**
> 同时显示已经安装的软件包

**-a, --all**
> 检查所有语言

**--package** _pkg_
> 检查特定软件包的语言支持

# CAVEATS

Ubuntu 专用工具；在其他发行版上可能无法使用。建议基于已安装的应用程序生成，可能会提示并非严格必需的软件包。

# SEE ALSO

[apt](/man/apt)(8), [locale](/man/locale)(1), [localectl](/man/localectl)(1)

# RESOURCES

```[Homepage](https://launchpad.net/language-selector)```

<!-- verified: 2026-06-22 -->
