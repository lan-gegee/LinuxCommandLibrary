# TAGLINE

流程图与图表编辑器

# TLDR

**打开图表编辑器**

```drawio```

**打开指定文件**

```drawio [diagram.drawio]```

**导出为 PNG**

```drawio --export --format png [diagram.drawio]```

将**所有页面**导出为一个 PDF

```drawio --export --format pdf --all-pages -o [out.pdf] [diagram.drawio]```

**导出单页**（页码从 1 开始）

```drawio --export --page-index [1] [diagram.drawio]```

以透明背景、2 倍缩放**导出 PNG**

```drawio --export --format png --transparent --scale [2] [diagram.drawio]```

**转换整个文件夹**，递归处理子文件夹

```drawio --export --recursive --format svg [path/to/folder]```

在 CI 或容器中**无界面导出**

```xvfb-run -a drawio --no-sandbox --export --format png [diagram.drawio]```

# SYNOPSIS

**drawio** [_options_] [_file_|_folder_]

# DESCRIPTION

**drawio**（前身为 diagrams.net）是一款用于流程图、网络拓扑图、UML、组织结构图等的图表编辑器。桌面应用通过 **Electron** 封装了网页版同一套编辑器，可完全离线工作。

它的核心设计目标是隔离：除更新检查外应用不建立任何网络连接，不发送遥测数据，也从不传输图表数据。正因如此，它才能用在无法使用云端图表工具的环境中。

图表以 XML 格式存储（`.drawio` 或 `.xml`），默认压缩，但可用 **--uncompressed** 以纯文本写出，从而可以在 pull request 中评审。命令行还能**导入**其他格式：`.vsdx`（Visio）、CSV 和 Mermaid `.mmd` 文件都可以作为输入，再导出为图像。

导出模式是 drawio 可脚本化的关键。使用 **--export** 时 UI 永远不会出现：应用渲染完文件即退出，构建管线正是借此让图表与文档保持同步。

# PARAMETERS

**-x**, **--export**
> 导出输入的文件或文件夹，而不是打开编辑器。

**-o**, **--output** _FILE_|_FOLDER_
> 输出路径。若省略，则复用输入名称并加上对应格式的扩展名。

**-f**, **--format** _FORMAT_
> 导出格式：`pdf`（默认）、`png`、`jpg`/`jpeg`、`svg`、`xml` 或 `html`。当 **-o** 已带已知扩展名时被忽略。

**-r**, **--recursive**
> 输入为文件夹时，同时转换子文件夹中的文件。

**-a**, **--all-pages**
> 导出所有页面。适用于 PDF 和 HTML。

**-p**, **--page-index** _N_
> 导出单个页面。**页码从 1 开始。**图像格式默认取第一页。

**-g**, **--page-range** _FROM_**..**_TO_
> 导出一段页面范围，从 1 开始计数。仅限 PDF。

**-l**, **--layers** _INDEXES_
> 要导出的图层索引，以逗号分隔。默认导出所有图层。

**-t**, **--transparent**
> 透明背景。仅限 PNG 和 SVG。

**-s**, **--scale** _N_
> 缩放图表。

**--width** _N_ / **--height** _N_
> 将输出适配到给定宽度或高度，保持纵横比。

**-b**, **--border** _N_
> 图表四周的边框宽度。默认为 0。

**--crop**
> 将 PDF 裁剪到图表尺寸。

**-q**, **--quality** _N_
> JPEG 画质。默认为 90。

**-e**, **--embed-diagram**
> 在输出内嵌一份可编辑的图表副本，使导出的 PNG、SVG 或 PDF 可以重新打开编辑。

**--embed-svg-images** / **--embed-svg-fonts**
> 将图像或字体内联进导出的 SVG。字体默认内嵌。

**-u**, **--uncompressed**
> 写出未压缩的 XML。适用于 XML 和 SVG 输出。

**--layout** _NAME_|_JSON_
> 导出前应用一种布局：`verticalFlow`、`horizontalFlow`、`verticalTree`、`horizontalTree`、`radialTree`、`organic`，或自定义布局 JSON 数组。

**--svg-theme** _THEME_
> 导出 SVG 的主题：`dark`、`light` 或 `auto`（默认）。

**-c**, **--create** / **-k**, **--check**
> 未给出文件时创建新的空文件，或拒绝覆盖已有文件。

**--disable-update**
> 跳过启动时的更新检查。设置环境变量 `DRAWIO_DISABLE_UPDATE=true` 效果相同，集中管理的安装环境适合这样做。

# CAVEATS

命令行中**页码从 1 开始**，尽管底层 XML 的索引从零开始。`--page-index 1` 即第一页。

导出并非真正的无头模式。作为 Electron 应用，它仍需要显示器，因此在构建服务器上必须用 **xvfb-run** 包装；在容器内以 root 运行还需要额外加 **--no-sandbox**。缺了任何一项都会崩溃，而且报错看起来完全不像是缺少显示器。

`vsdx`、`csv` 和 Mermaid 仅是**输入**格式；不能导出为这些格式。可用的导出格式为 pdf、png、jpg、svg、xml 和 html。

另请注意：该项目按政策不接受外部贡献——欢迎提交 bug 报告，但不接受 pull request。

# HISTORY

**draw.io** 由 **JGraph Ltd**（Gaudenz Alder 与 David Benson）于 **2012 年**前后基于该公司更早的 mxGraph JavaScript 库打造。Electron 桌面应用随后问世，服务于那些不能或不愿在与他人云服务相连的浏览器标签页里运行图表编辑器的用户。

其命名经历了一番循环。产品在 **2020 年**更名为 **diagrams.net**，部分原因在于 `.io` 顶级域名与英属印度洋领地的关联变得尴尬；后来又迁回 **drawio.com**，不过几乎所有用户仍把这个应用叫作 draw.io。

# INSTALL

```nix: nix profile install nixpkgs#drawio```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[inkscape](/man/inkscape)(1), [plantuml](/man/plantuml)(1), [dot](/man/dot)(1), [dia](/man/dia)(1), [mermaid](/man/mermaid)(1)

# RESOURCES

```[Source code](https://github.com/jgraph/drawio-desktop)```

```[Homepage](https://www.drawio.com)```

<!-- verified: 2026-07-14 -->
