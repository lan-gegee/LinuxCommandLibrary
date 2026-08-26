# TAGLINE

检查 HDF5 文件的终端 UI

# TLDR

**打开 HDF5 文件进行检查**

```h5tui [path/to/file.h5]```

# SYNOPSIS

**h5tui** [_options_] _file_

# DESCRIPTION

**hdf5_ui**（调用名为 **h5tui**）是一个用于检查 **HDF5** 文件的文本用户界面。它提供基于树的浏览器来浏览 HDF5 文件内的组和数据集，并以条理清晰的布局显示属性和元数据。

该工具内置多个插件，包括以十六进制形式展示数据集内容的 **HexViewer**，以及直接在终端中可视化二维或三维图像数据的 **ImageViewer**。当某个节点被高亮时，它的属性会显示在左下方的面板中。

# CAVEATS

需要 Python 和 h5py 库。通过 `pip install h5ui` 安装。特别大的数据集在终端中渲染可能很慢。ImageViewer 插件要求数据可以转换为 Pillow 图像。自定义插件可以通过 entrypoints 添加。

# HISTORY

**hdf5_ui** 由 **Rik Huygen**（rhuygen）创建，使用 **Python** 编写，基于 **Textual** TUI 框架。它的开发初衷是为 HDFView 等图形化 HDF5 检查工具提供一个便捷的终端替代方案。

# SEE ALSO
