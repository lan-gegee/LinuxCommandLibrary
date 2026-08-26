# TAGLINE

启动 JupyterLab，一个交互式开发环境

# TLDR

**启动 JupyterLab 服务器**

```jupyter lab```

**在指定端口启动**

```jupyter lab --port [8888]```

**启动时不打开浏览器**

```jupyter lab --no-browser```

**在指定目录中启动**

```jupyter lab --notebook-dir=[path]```

**以指定的 IP 绑定启动**

```jupyter lab --ip=[0.0.0.0]```

# SYNOPSIS

**jupyter** **lab** [_options_]

# PARAMETERS

**--port** _number_
> 服务器运行端口。默认：8888。

**--no-browser**
> 不自动打开浏览器。

**--notebook-dir** _path_
> 提供 notebook 服务的目录。

**--ip** _address_
> 绑定的 IP 地址。默认：localhost。

**--allow-root**
> 允许以 root 用户身份运行。

**--core-mode**
> 以核心模式启动，不启用任何扩展。

**--dev-mode**
> 使用本地 JavaScript 包以开发模式启动。

**--app-dir** _path_
> 以特定的一组扩展启动。

**--certfile** _path_
> 用于 HTTPS 的 SSL/TLS 证书文件。

**--help**
> 显示简要的命令行选项。

**--help-all**
> 显示所有可用选项，包括详细说明。

# DESCRIPTION

**jupyter lab** 启动 JupyterLab，一个用于处理笔记本、代码和数据的交互式开发环境。它为数据科学、科学计算和机器学习工作流提供了灵活的界面，并支持多种编程语言。

JupyterLab 是 Project Jupyter 的下一代 Web 界面，提供带标签页的工作区，将文件浏览器、终端、文本编辑器和笔记本支持集成在同一环境中。

# INSTALL

```dnf: sudo dnf install jupyterlab```

```pacman: sudo pacman -S jupyterlab```

```brew: brew install jupyterlab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jupyter](/man/jupyter)(1), [python](/man/python)(1), [pip](/man/pip)(1)
