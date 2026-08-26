# TAGLINE

用于创建或编辑漫画分格框的浏览器界面

# TLDR

**在浏览器中编辑**漫画的分格框

```cbxy-editor [path/to/book.cbz]```

**绑定**到指定的主机和端口

```cbxy-editor [path/to/book.cbz] --host [127.0.0.1] --port [8766]```

**不自动打开**浏览器窗口

```cbxy-editor [path/to/book.cbz] --no-open```

**安装** cbxy 工具

```pip install cbxy```

# SYNOPSIS

**cbxy-editor** [_options_] _comic_

# DESCRIPTION

**cbxy-editor** 启动一个本地 Web 界面，用于创建或修正分格矩形，并在漫画旁保存 **.cbxy** 伴随文件。可在用 **cbxy-detect** 完成自动检测之后使用，也可以用来从头编写分格几何信息。坐标以归一化的页面比例存储在 **.cbxy** ZIP 内按页组织的 JSON 中。

输入可以是 **.cbz**、**.cbr**、图片文件夹或单页图片。默认绑定地址为端口 **8766** 上的 **127.0.0.1**（与 **cbxy-reader** 默认的 **8765** 不同）。属于 **cbxy** Python 软件包的一部分。

# PARAMETERS

_comic_
> **.cbz**、**.cbr**、图片文件夹或单页图片的路径。

**--host** _address_
> 绑定地址（默认：**127.0.0.1**）。

**--port** _port_
> 监听端口（默认：**8766**）。

**--no-open**
> 不自动打开浏览器窗口。

# CAVEATS

该编辑器是本地浏览器界面，不是无头批处理工具——自动化流水线请使用 **cbxy-detect**。绑定到回环地址之外会将编辑器暴露在网络中。保存的 **.cbxy** 文件应始终与对应的漫画归档配对存放，以便 **cbxy-reader** 的引导模式使用。

# HISTORY

**cbxy** 是由 **ngafar** 编写的漫画分格几何伴随格式的 Python 参考实现，以 MIT 许可证发布，包含 **cbxy-detect**、**cbxy-reader** 和 **cbxy-editor**。

# SEE ALSO

[cbxy-detect](/man/cbxy-detect)(1), [cbxy-reader](/man/cbxy-reader)(1), [pip](/man/pip)(1), [uv](/man/uv)(1)

# RESOURCES

```[Source code](https://github.com/ngafar/cbxy)```

```[Documentation](https://github.com/ngafar/cbxy#cbxy-editor)```

<!-- verified: 2026-07-21 -->
