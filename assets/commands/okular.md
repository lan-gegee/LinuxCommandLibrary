# TAGLINE

KDE 的通用文档查看器

# TLDR

**打开文档**

```okular [document.pdf]```

**在特定页打开**

```okular -p [5] [document.pdf]```

**以演示模式打开**

```okular --presentation [document.pdf]```

**使用特定后端打开**

```okular --backend [poppler] [document.pdf]```

**打印文档**

```okular --print [document.pdf]```

**唯一实例**（复用窗口）

```okular --unique [document.pdf]```

**不加载插件启动**

```okular --no-plugins [document.pdf]```

# SYNOPSIS

**okular** [_-p page_] [_--presentation_] [_--unique_] [_options_] _files_

# PARAMETERS

**-p** _PAGE_
> 从指定页码开始。

**--presentation**
> 以演示模式启动。

**--unique**
> 使用单实例。

**--print**
> 打印后退出。

**--backend** _NAME_
> 使用特定的后端。

**--no-plugins**
> 禁用插件。

**--editor-cmd** _CMD_
> 用于源码链接的编辑器命令。

**--find** _TEXT_
> 打开文档时搜索文本。

**--noraise**
> 不将窗口提升到前台。

# DESCRIPTION

**okular** 是 KDE 的通用文档查看器。它通过插件支持 PDF、EPUB、DjVu、PostScript、图片等众多格式。

PDF 查看支持批注、表单填写和数字签名验证。文档可以添加高亮、笔记和手绘等批注。批注可单独保存，也可嵌入文件中。

演示模式提供全屏幻灯片显示。切换效果与笔记支持使其适合用于演示。

文本选择和搜索在所有受支持的格式中均可使用。连续滚动和多栏版式可适应不同的阅读偏好。

编辑器集成功能支持点击 PDF 中的源码位置，从而在 LaTeX 编辑器中打开对应位置。这为 SyncTeX 工作流提供了支持。

打印功能包含小册子打印、页面缩放等高级选项。打印预览可显示确切的输出效果。

# CAVEATS

基于 KDE，会引入 KDE 相关依赖。某些格式支持需要可选的后端。大型文档可能占用较多内存。

# HISTORY

**Okular** 为 **KDE 4** 而创建于 **2007** 年，将多个 KDE 文档查看器（KPDF、KGhostView、KFax）合并为一个统一的应用程序。它成为 KDE 的标准文档查看器，格式支持持续扩展。

# INSTALL

```apt: sudo apt install okular```

```dnf: sudo dnf install okular```

```pacman: sudo pacman -S okular```

```apk: sudo apk add okular```

```zypper: sudo zypper install okular```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[evince](/man/evince)(1), [zathura](/man/zathura)(1), [mupdf](/man/mupdf)(1), [xpdf](/man/xpdf)(1)
