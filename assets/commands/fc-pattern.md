# TAGLINE

解析并显示 fontconfig 模式

# TLDR

**解析字体模式**

```fc-pattern "[pattern]"```

**显示默认模式**

```fc-pattern --default [pattern]```

**应用配置到模式**

```fc-pattern --config [pattern]```

**自定义格式输出**

```fc-pattern --format "%{family}" [pattern]```

# SYNOPSIS

**fc-pattern** [_options_] [_pattern_]

# PARAMETERS

**-d**, **--default**
> 应用默认替换。

**-c**, **--config**
> 应用配置替换。

**-f**, **--format** _format_
> 自定义输出格式。

# DESCRIPTION

**fc-pattern** 解析并显示 fontconfig 模式，展示 fontconfig 如何解释字体匹配请求。该工具可用于调试字体配置和理解模式语法。

Fontconfig 模式指定期望的字体属性，如字族、样式、字重和字号。fc-pattern 揭示这些模式如何被规范化，以及配置应用了哪些替换。

# CAVEATS

模式语法可能较复杂。解读输出格式需要了解 fontconfig 内部机制。主要用于调试而非日常字体管理。

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

[fc-match](/man/fc-match)(1), [fc-list](/man/fc-list)(1), [fc-query](/man/fc-query)(1)

# RESOURCES

```[Source code](https://gitlab.freedesktop.org/fontconfig/fontconfig)```

```[Homepage](https://www.freedesktop.org/wiki/Software/fontconfig/)```

<!-- verified: 2026-07-15 -->
