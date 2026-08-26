# TAGLINE

从 Markdown 创建演示文稿

# TLDR

**转换为 HTML**

```marp [slides.md] -o [slides.html]```

**转换为 PDF**

```marp [slides.md] --pdf -o [slides.pdf]```

**转换为 PPTX**

```marp [slides.md] --pptx -o [slides.pptx]```

**将幻灯片转换为图片**

```marp [slides.md] --images [png] -o [slides/]```

**预览并实时重载**

```marp -p [slides.md]```

**使用自定义主题**

```marp --theme [theme.css] [slides.md] -o [output.html]```

**启动服务器模式**

```marp -s [slides/]```

**监视变化并自动转换**

```marp -w [slides.md] -o [slides.html]```

# SYNOPSIS

**marp** [_options_] _file_

# PARAMETERS

**-o**, **--output** _file_
> 输出文件名或目录。

**--pdf**
> 导出为 PDF。

**--pptx**
> 导出为 PowerPoint。

**--images** [png|jpeg]
> 将幻灯片导出为多个图片文件。

**--image** [png|jpeg]
> 将第一张幻灯片导出为单张图片。

**--notes**
> 将演讲者备注导出为文本文件。

**-p**, **--preview**
> 打开预览窗口。

**-s**, **--server** _dir_
> 启动服务器模式，按需转换。

**--theme** _css_
> 自定义主题 CSS 文件。

**-w**, **--watch**
> 监视文件变化并自动转换。

**--pdf-notes**
> 将演讲者备注添加为 PDF 注释。

**--pdf-outlines**
> 在 PDF 输出中添加书签。

**--allow-local-files**
> 允许在转换过程中访问本地文件。

**--image-scale** _factor_
> 渲染图片的缩放系数（默认：1）。

**-I**, **--input-dir** _dir_
> 输入的基础目录，同时保留输出目录结构。

**-c**, **--config-file** _file_
> 配置文件路径。

**--engine** _module_
> 指定基于 Marpit 的转换引擎。

# DESCRIPTION

**Marp**（Markdown Presentation Ecosystem）从 Markdown 创建演示文稿。它将特殊格式的 Markdown 转换为 HTML、PDF 或 PowerPoint 格式的幻灯片。

幻灯片以 --- 分隔，支持自定义主题、演讲者备注和指令（directive）。

# SLIDE FORMAT

```markdown
---
marp: true
theme: default
---

# Slide 1

Content here

---

# Slide 2

More content
```

# CAVEATS

PDF 和图片导出需要 Chrome、Edge 或 Firefox。部分 CSS 特性在 PPTX 输出中受限。PDF/图片转换中引用本地文件需要 **--allow-local-files**。

# HISTORY

Marp 由 **Yuki Hattori**（yhatt）于 **2016 年**创建，最初是 Marp 桌面应用，后来重写为带 CLI 的 Marp Next 生态系统。

# SEE ALSO

[pandoc](/man/pandoc)(1)
