# TAGLINE

带可选分格引导视图的浏览器漫画阅读器

# TLDR

**在浏览器中打开**一部漫画

```cbxy-reader [path/to/book.cbz]```

**绑定**到指定的主机和端口

```cbxy-reader [path/to/book.cbz] --host [127.0.0.1] --port [8765]```

**不自动打开**浏览器窗口

```cbxy-reader [path/to/book.cbz] --no-open```

**安装** cbxy 工具

```uv tool install cbxy```

# SYNOPSIS

**cbxy-reader** [_options_] _comic_

# DESCRIPTION

**cbxy-reader** 启动一个本地 Web 服务器并在浏览器中打开漫画。如果存在同名的 **.cbxy** 伴随文件（由 **cbxy-detect** 或 **cbxy-editor** 生成的分格几何信息），阅读器支持逐格引导式导航；没有伴随文件时则只显示整页。

输入可以是 **.cbz**、**.cbr**、图片文件夹或单页图片。默认绑定地址为端口 **8765** 上的 **127.0.0.1**。属于 **cbxy** Python 软件包的一部分。

# PARAMETERS

_comic_
> **.cbz**、**.cbr**、图片文件夹或单页图片的路径。

**--host** _address_
> 绑定地址（默认：**127.0.0.1**）。

**--port** _port_
> 监听端口（默认：**8765**）。

**--no-open**
> 不自动打开浏览器窗口。

# CAVEATS

引导式分格视图要求漫画旁有匹配的 **.cbxy** 文件（或符合该工具的查找约定）。绑定到非 localhost 的接口会将阅读器暴露在网络中——除非有意为之，否则请保持默认的回环绑定。阅读期间该进程必须保持运行。

# HISTORY

**cbxy** 是由 **ngafar** 编写的漫画分格几何伴随格式的 Python 参考实现，以 MIT 许可证发布，包含 **cbxy-detect**、**cbxy-reader** 和 **cbxy-editor**。

# SEE ALSO

[cbxy-detect](/man/cbxy-detect)(1), [cbxy-editor](/man/cbxy-editor)(1), [pip](/man/pip)(1), [uv](/man/uv)(1)

# RESOURCES

```[Source code](https://github.com/ngafar/cbxy)```

```[Documentation](https://github.com/ngafar/cbxy#cbxy-reader)```

<!-- verified: 2026-07-21 -->
