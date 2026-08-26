# TAGLINE

类 Vim 的模态文档查看器

# TLDR

**打开**文档

```zathura [path/to/file]```

在指定**页码**处打开文档

```zathura -P [page_number] [path/to/file]```

打开并 **fork 到后台**

```zathura --fork [path/to/file]```

打开**受密码保护的**文档

```zathura --password [password] [path/to/file]```

# SYNOPSIS

**zathura** [_OPTIONS_] [_FILE_...]

# PARAMETERS

**-P**, **--page** _NUM_
> 在给定页码处打开文档（从 1 开始，负数表示从末尾计）。

**--fork**
> fork 到后台运行。

**--password** _PASSWORD_
> 提供文档密码。

**-e** _XID_, **--reparent** _XID_
> 重新挂载到 XID 指定的窗口。

**h/j/k/l 或方向键**
> 向左/上/下/右导航。

**J/K 或 PgDn/PgUp**
> 转到下一页/上一页。

**r**
> 旋转文档。

**Ctrl+r**
> 反转颜色（重新着色模式）。

**/**
> 搜索文本。

**n/N**
> 下一个/上一个搜索结果。

**d**
> 切换双页视图。

**F5**
> 切换到演示模式。

**F11**
> 切换全屏。

**:bmark** _NAME_
> 创建书签。

**:bdelete** _NAME_
> 删除书签。

**:blist**
> 列出书签。

**+, -**
> 放大/缩小。

**a**
> 适应宽度。

**s**
> 适应整页。

# DESCRIPTION

**zathura** 是一款类 Vim 的模态文档查看器。它通过后端支持 PDF、PostScript、DjVu 等格式。

该查看器以键盘驱动的导航、书签和集成的命令行为特色。

# CAVEATS

需要后端插件（PDF 用 poppler 或 mupdf 等）。通过 ~/.config/zathura/zathurarc 配置。Vim 风格的键绑定可能需要一定学习成本。

# INSTALL

```apt: sudo apt install zathura```

```dnf: sudo dnf install zathura```

```pacman: sudo pacman -S zathura```

```apk: sudo apk add zathura```

```zypper: sudo zypper install zathura```

```nix: nix profile install nixpkgs#zathura```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[evince](/man/evince)(1), [okular](/man/okular)(1), [mupdf](/man/mupdf)(1)
