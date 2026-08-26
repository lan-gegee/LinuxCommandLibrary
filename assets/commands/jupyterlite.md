# TAGLINE

构建完全依靠浏览器运行的静态 JupyterLab 站点

# TLDR

**构建 JupyterLite 站点**

```jupyter lite build```

**以指定内容构建**

```jupyter lite build --contents [notebooks/]```

**本地运行构建好的站点**

```jupyter lite serve```

**附带额外软件包构建**

```jupyter lite build --piplite-wheels [package.whl]```

**清理构建产物**

```jupyter lite clean```

**检查配置**

```jupyter lite status```

**以自定义输出目录构建**

```jupyter lite build --output-dir [dist/]```

**初始化配置**

```jupyter lite init```

# SYNOPSIS

**jupyter lite** _command_ [_options_]

# COMMANDS

**build**
> 构建 JupyterLite 静态站点。

**serve**
> 本地运行构建好的站点。

**init**
> 初始化配置文件。

**status**
> 显示构建配置状态。

**clean**
> 移除构建产物。

**archive**
> 为构建好的站点创建归档。

**list**
> 列出 addon 及其状态。

# PARAMETERS

**--contents** _path_
> notebook 内容目录的路径。

**--output-dir** _path_
> 构建站点的输出目录。默认：_output。

**--piplite-wheels** _path_
> 包含供 piplite 使用的 pip wheel 文件。

**--pyodide** _url_
> 自定义 Pyodide 发行版 URL。

**--port** _port_
> serve 命令使用的端口。默认：8000。

**--lite-dir** _path_
> JupyterLite 文件的源目录。

**--settings-overrides** _file_
> 包含设置覆盖项的 JSON 文件。

**--no-sourcemaps**
> 在构建中禁用 source map。

# DESCRIPTION

**jupyter lite** 构建完全在浏览器中借助 WebAssembly 运行的静态 JupyterLab 站点。无需服务器——可部署到任何静态托管服务上。

**build** 会在输出目录中生成 HTML、JavaScript 和资源文件。使用 **--contents** 包含 notebook，以便预填充文件浏览器。生成的站点运行带有 Pyodide 内核的 JupyterLab。

Pyodide 内核在 WebAssembly 中执行 Python。可用 **--piplite-wheels** 预装软件包，或在运行时通过 piplite 安装。许多科学计算类 Python 软件包均可用。

**serve** 会启动一个本地 HTTP 服务器供测试。构建产物可以部署到 GitHub Pages、Netlify 或任何静态托管服务，无需后端基础设施。

通过 **jupyter_lite_config.json** 可以自定义设置、扩展和构建行为。**init** 会创建模板文件。

# CAVEATS

并非所有 Python 软件包都能在 Pyodide 中运行（没有 WASM 构建就无法使用原生扩展）。性能比原生 Python 慢。大型笔记本可能触及浏览器内存上限。部分 JupyterLab 扩展不兼容。

# HISTORY

JupyterLite 由 **Project Jupyter** 团队于 **2021 年**发布，利用 Pyodide 实现浏览器端 Python。它让交互式笔记本可以在没有服务器基础设施的情况下分享。该项目源自 WebAssembly Python 解释器的实验。JupyterLite 可用于教学内容、文档和轻量级演示。开发工作仍在持续，与 JupyterLab 的改进同步推进。

# INSTALL

```nix: nix profile install nixpkgs#jupyterlite```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jupyter-lab](/man/jupyter-lab)(1), [jupyter](/man/jupyter)(1)
