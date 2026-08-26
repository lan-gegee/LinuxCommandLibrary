# TAGLINE

将 Pygame 游戏打包为网页版

# TLDR

**为网页打包游戏**

```pygbag [path/to/game]```

**指定输出目录**

```pygbag --build [path/to/game]```

**运行开发服务器**

```pygbag --dev [path/to/game]```

**自定义归档名称**

```pygbag --archive [name] [path/to/game]```

**为开发服务器指定端口**

```pygbag --port [8000] [path/to/game]```

**指定模板**

```pygbag --template [template.html] [path/to/game]```

# SYNOPSIS

**pygbag** [_--build_] [_--dev_] [_options_] _path_

# PARAMETERS

**--build**
> 仅构建，不启动服务器。

**--dev**
> 开发模式。

**--archive** _NAME_
> 归档文件名。

**--template** _FILE_
> 自定义 HTML 模板。

**--port** _PORT_
> 开发服务器端口（默认：8000）。

**--cdn** _URL_
> CDN 基础 URL。

**--title** _TITLE_
> 页面标题。

**--ume_block** _SIZE_
> 设置最大缓存块大小。

# DESCRIPTION

**pygbag** 使用 Emscripten 和 Pyodide 将 Python 代码编译为 WebAssembly，从而把 Pygame 应用打包部署到网页浏览器中。构建产物可直接在现代浏览器中运行且无需插件，让在线分享 Python 游戏和多媒体应用变得简单。

该工具内置开发服务器，可在部署前进行本地测试。游戏必须使用配合 **asyncio** 的异步编程模式，以适应浏览器的事件循环模型。pygbag 负责资源打包、HTML 模板生成和 WebAssembly 编译流水线，从标准 Pygame 项目生成自包含的 Web 应用。

# CAVEATS

并非所有 Python 库都在 WebAssembly 环境中受支持；C 扩展必须针对 Emscripten 专门编译。主游戏循环必须使用 `asyncio` 并配合 `await asyncio.sleep(0)` 以保证浏览器兼容性。入口文件必须命名为 `main.py`。由于包含 Python 运行时，构建产物可能较大。

# HISTORY

**pygbag** 的诞生是为了借助 WebAssembly 和 Pyodide 将 Pygame 游戏带入浏览器。

# SEE ALSO

[pygame](/man/pygame)(1), [python](/man/python)(1), [emcc](/man/emcc)(1)
