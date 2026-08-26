# TAGLINE

查找最佳匹配的字体

# TLDR

**查找最佳匹配的字体**

```fc-match [pattern]```

**匹配等宽字体**

```fc-match monospace```

**匹配指定字族**

```fc-match "DejaVu Sans"```

**显示详细输出**

```fc-match -v [pattern]```

**显示特定元素**

```fc-match --format "%{family}\n" [pattern]```

**匹配所有字体**

```fc-match -a [pattern]```

# SYNOPSIS

**fc-match** [_options_] [_pattern_]

# PARAMETERS

**-a**, **--all**
> 显示所有匹配的字体。

**-s**, **--sort**
> 按优先级排序输出。

**-v**, **--verbose**
> 详细输出。

**--format** _format_
> 格式化输出字符串。

# DESCRIPTION

**fc-match** 将字体与 fontconfig 模式进行匹配，并显示对于给定请求将使用哪个字体。该工具对调试字体配置、理解为何选中某个字体以及验证字体替换规则至关重要。

当应用请求某个字体时，fontconfig 会使用复杂的匹配算法，综合考虑字族名、样式、字重等属性。fc-match 揭示这一匹配过程的结果，帮助诊断字体相关问题。

# CAVEATS

模式语法可能较复杂。字体匹配规则取决于 fontconfig 配置。在不同字体安装状况的系统上结果可能不同。

# INSTALL

```apt: sudo apt install fontconfig```

```dnf: sudo dnf install fontconfig```

```pacman: sudo pacman -S fontconfig```

```apk: sudo apk add fontconfig```

```zypper: sudo zypper install fontconfig```

```brew: brew install fontconfig```

```nix: nix profile install nixpkgs#fontconfig```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fc-list](/man/fc-list)(1), [fc-cache](/man/fc-cache)(1), [fc-pattern](/man/fc-pattern)(1), [fc-query](/man/fc-query)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/fontconfig/fontconfig)```

```[Homepage](https://www.freedesktop.org/wiki/Software/fontconfig/)```

<!-- verified: 2026-07-15 -->
