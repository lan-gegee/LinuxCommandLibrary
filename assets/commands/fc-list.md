# TAGLINE

列出可用字体

# TLDR

**列出所有字体**

```fc-list```

**列出匹配模式的字体**

```fc-list : family style | sort```

**查找特定字体**

```fc-list | grep -i "[arial]"```

**列出等宽字体**

```fc-list :spacing=mono family```

**显示字体文件路径**

```fc-list : file family```

**列出具有特定样式的字体**

```fc-list :style=Bold```

**按语言列出字体**

```fc-list :lang=[zh]```

# SYNOPSIS

**fc-list** [_options_] [_pattern_] [_elements_]

# PARAMETERS

**-v**, **--verbose**
> 包含所有属性的详细输出。

**-f** _format_
> 自定义输出格式。

**-q**, **--quiet**
> 抑制常规输出。

**--version**
> 显示版本。

_pattern_
> 字体匹配模式。

_elements_
> 要显示的属性：family、style、file 等。

# DESCRIPTION

**fc-list** 列出使用 fontconfig 的应用可用的字体。它显示字体族名称、样式、文件位置及其他属性。

该命令对于发现已安装的字体、查找字体文件路径和验证字体安装至关重要。它查询缓存了字体信息的 fontconfig 数据库。

# CAVEATS

输出可能很长；可管道到 grep 或 sort。字体名称可能因语言而异。新安装的字体需要执行 `fc-cache -fv`。有些应用会独立缓存字体。

# HISTORY

fc-list 是 **fontconfig** 的一部分，由 **Keith Packard** 于 **2000 年**前后创建，为 X11 及其他系统提供系统级字体配置。它以更灵活的基于文件的方式取代了旧的 X 字体系统。

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

[fc-cache](/man/fc-cache)(1), [fc-match](/man/fc-match)(1), [fc-query](/man/fc-query)(1)
