# TAGLINE

显示彩色 ASCII 艺术文字横幅

# TLDR

为文本生成 **ASCII 艺术**

```toilet [input_text]```

使用自定义**字体**

```toilet [input_text] -f [font_filename]```

应用**过滤器**

```toilet [input_text] -F [filter_name]```

**列出**可用过滤器

```toilet -F list```

# SYNOPSIS

**toilet** [_OPTIONS_] [_TEXT_...]

# PARAMETERS

**-f, --font** _NAME_
> 使用指定的字体文件

**-F, --filter** _NAME_
> 对输出应用过滤器

**-w, --width** _N_
> 设置输出宽度

**-t, --term**
> 使用终端宽度

**-d, --directory** _DIR_
> 指定字体目录

# DESCRIPTION

**toilet**（The Other Implementation's letters）使用各种字体和滤镜显示 ASCII 艺术文字横幅。它与 FIGlet 类似，但额外支持彩色滤镜和 Unicode。

该程序从命令行参数或标准输入读取文本，并使用指定字体渲染。多种滤镜可应用颜色渐变、边框和变换等效果。

# CAVEATS

字体可用性取决于安装情况。某些滤镜需要终端颜色支持。宽幅输出在窄终端上可能换行错乱。Unicode 字体需要终端支持 UTF-8。

# HISTORY

**toilet** 由 **Sam Hocevar** 作为 libcaca 项目的一部分创建，提供了 FIGlet 的替代方案，并增加了彩色支持和更多渲染选项等特性。

# INSTALL

```apt: sudo apt install toilet```

```dnf: sudo dnf install toilet```

```pacman: sudo pacman -S toilet```

```zypper: sudo zypper install toilet```

```brew: brew install toilet```

```nix: nix profile install nixpkgs#toilet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[figlet](/man/figlet)(1), [banner](/man/banner)(1)
