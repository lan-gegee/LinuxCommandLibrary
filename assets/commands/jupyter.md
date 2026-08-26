# TAGLINE

提供交互式计算环境

# TLDR

**启动 notebook 服务器**

```jupyter notebook```

**启动 JupyterLab**

```jupyter lab```

**在指定端口启动**

```jupyter notebook --port [8888]```

**列出运行中的服务器**

```jupyter notebook list```

**停止服务器**

```jupyter notebook stop [8888]```

**转换笔记本**

```jupyter nbconvert --to [html|pdf|py] [notebook.ipynb]```

# SYNOPSIS

**jupyter** _command_ [_options_]

# PARAMETERS

**notebook**
> 经典 notebook 界面。

**lab**
> JupyterLab 界面。

**nbconvert**
> 转换笔记本。

**--port** _PORT_
> 服务器端口。

**--no-browser**
> 不打开浏览器。

**--ip** _IP_
> 服务器 IP 地址。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Jupyter** 提供交互式计算环境。它运行 notebook 服务器来执行代码并撰写文档。

该平台通过内核支持多种语言。Notebook 将代码、输出和 Markdown 结合在一起。

# CAVEATS

基于 Python。需要浏览器。远程访问时须注意安全问题。

# HISTORY

Jupyter 于 2014 年从 **IPython** 中独立出来，扩展为支持多种语言（Julia、Python、R——故名 Ju-Pyt-eR）。

# INSTALL

```apk: sudo apk add py3-jupyter_core```

```brew: brew install jupyter```

```nix: nix profile install nixpkgs#jupyter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ipython](/man/ipython)(1), [jupytext](/man/jupytext)(1)
