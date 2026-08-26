# TAGLINE

GNOME 的 PDF 与 PostScript 文档查看器

# TLDR

**打开** PDF 文件

```evince [path/to/file.pdf]```

打开**多个**文档

```evince [file1.pdf] [file2.pdf]```

以**全屏**模式打开

```evince [-f|--fullscreen] [path/to/file.pdf]```

以**演示**模式打开

```evince [-s|--presentation] [path/to/file.pdf]```

打开指定的**页码**

```evince [-i|--page-index] [5] [path/to/file.pdf]```

# SYNOPSIS

**evince** [_options_] [_files_]

# PARAMETERS

**-f, --fullscreen**
> 以全屏模式打开

**-s, --presentation**
> 以演示模式打开

**-i, --page-index** _page_
> 打开到指定页码

**-l, --page-label** _label_
> 打开到具有指定标签的页面

**-w, --preview**
> 以预览模式运行

# DESCRIPTION

**evince** 是 GNOME 的文档查看器，支持 PDF、PostScript、DjVu、TIFF 等格式。它提供注释支持、表单填写和演示模式功能。

它与 GNOME 桌面的打印和文件管理服务集成。

# CAVEATS

GNOME 桌面应用。部分功能依赖 poppler 库。大文档可能占用较多内存。

# INSTALL

```apt: sudo apt install evince```

```dnf: sudo dnf install evince```

```pacman: sudo pacman -S evince```

```apk: sudo apk add evince```

```zypper: sudo zypper install evince```

```brew: brew install evince```

```nix: nix profile install nixpkgs#evince```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[okular](/man/okular)(1), [zathura](/man/zathura)(1), [xdg-open](/man/xdg-open)(1)

# RESOURCES

```[Source code](https://gitlab.gnome.org/GNOME/evince)```

```[Homepage](https://apps.gnome.org/Evince/)```

<!-- verified: 2026-07-15 -->
