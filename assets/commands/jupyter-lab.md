# TAGLINE

JupyterLab 的命令行界面，Project Jupyter 的下一代 Web 界面

# TLDR

**启动 JupyterLab**

```jupyter lab```

**在指定端口启动**

```jupyter lab --port [8889]```

**启动时不打开浏览器**

```jupyter lab --no-browser```

**以指定的笔记本目录启动**

```jupyter lab --notebook-dir=[/path/to/notebooks]```

**允许外部连接**

```jupyter lab --ip [0.0.0.0]```

**生成配置文件**

```jupyter lab --generate-config```

**列出运行中的服务器**

```jupyter lab list```

**停止服务器**

```jupyter lab stop [8888]```

# SYNOPSIS

**jupyter lab** [_options_]

**jupyter lab** build|clean|path|paths|workspaces

# COMMANDS

**jupyter lab**
> 启动 JupyterLab 服务器。

**jupyter lab build**
> 构建 JupyterLab 应用。

**jupyter lab clean**
> 移除构建产物。

**jupyter lab list**
> 列出运行中的 JupyterLab 服务器。

**jupyter lab stop** _port_
> 停止指定端口上的服务器。

**jupyter lab path**
> 显示 JupyterLab 的路径。

**jupyter lab workspaces** list|export|import
> 管理工作区。

# PARAMETERS

**--port** _port_
> 服务器端口。默认：8888。

**--ip** _address_
> 绑定的 IP 地址。默认：localhost。

**--no-browser**
> 启动时不打开浏览器。

**--notebook-dir** _path_
> 笔记本的根目录。

**--app-dir** _path_
> JupyterLab 应用目录。

**--generate-config**
> 生成默认配置文件。

**--config** _file_
> 配置文件路径。

**--ContentsManager.allow_hidden** _bool_
> 允许访问隐藏文件。

**--ServerApp.token** _token_
> 身份验证令牌。

**--ServerApp.password** _hash_
> 用于访问的哈希密码。

**--collaborative**
> 启用实时协作。

**--allow-root**
> 允许以 root 用户身份运行服务器。

**--debug**
> 设置调试级别日志。

**--help-all**
> 显示所有可配置选项后退出。

# DESCRIPTION

**jupyter lab** 是 JupyterLab 的命令行界面，后者是 Project Jupyter 的下一代 Web 界面。它为笔记本、代码和数据提供了一个灵活且可扩展的 IDE。

JupyterLab 会运行一个提供 Web 界面的服务器。通过浏览器访问时需使用启动时显示的令牌。支持多个用户连接；协作模式可实现共享编辑。

界面支持笔记本、文本编辑器、终端和扩展。文件浏览器用于浏览 **--notebook-dir** 目录树。多个文档以标签页形式打开，并支持分屏视图。

扩展可以增加功能。使用 **jupyter labextension** 进行管理。扩展变更后需运行 **jupyter lab build** 重新编译资源。

可通过 **jupyter_lab_config.py** 设置默认配置。使用 **--generate-config** 生成配置模板。常见设置包括令牌/密码、允许的来源和内核设置。

# CAVEATS

服务器暴露了 notebook-dir 下的完整文件系统访问权限。生产部署需要妥善的身份验证和 HTTPS。扩展可能需要重新构建。内存占用随内核数量增长。

# HISTORY

JupyterLab 的开发始于 **2016 年**前后，作为 Jupyter Notebook 界面的继任者。经过漫长的 beta 阶段后于 **2019 年**发布 1.0 版本。它由 **Project Jupyter** 开发，该项目源自 IPython。它是更庞大的 Jupyter 生态的一部分，生态中包含众多语言的内核。JupyterLab 4.0（2023 年）带来了性能改进和实时协作功能。

# INSTALL

```dnf: sudo dnf install jupyterlab```

```pacman: sudo pacman -S jupyterlab```

```apk: sudo apk add jupyterlab```

```brew: brew install jupyterlab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jupyter](/man/jupyter)(1), [ipython](/man/ipython)(1), [jupyterlite](/man/jupyterlite)(1)
