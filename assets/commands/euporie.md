# TAGLINE

在终端中使用 Jupyter 笔记本、控制台和预览

# TLDR

在终端编辑器中**打开笔记本**

```euporie notebook [notebook.ipynb]```

**启动 Jupyter 控制台**并连接到内核

```euporie console --kernel [python3]```

**将笔记本渲染到终端**而不打开它

```euporie preview [notebook.ipynb]```

**将渲染好的预览保存到**文件

```euporie preview --save-as [output.txt] [notebook.ipynb]```

将 euporie 作为多用户 SSH hub 运行

```euporie hub --host [0.0.0.0] --port [8022]```

**选择配色方案**

```euporie notebook --color-scheme [dark] [notebook.ipynb]```

# SYNOPSIS

**euporie** _app_ [_options_] [_notebook_]

**euporie** **notebook** | **console** | **preview** | **hub** [_options_]

# APPS / SUBCOMMANDS

**notebook**
> 交互式笔记本编辑器，采用类似 Jupyter 的按键绑定。

**console**
> 可连接任意 Jupyter 内核的逐行 REPL。

**preview**
> 将笔记本渲染到标准输出、分页器或文件（无需内核）。

**hub**
> 多用户 SSH 服务器 — 每个客户端都拥有自己的笔记本编辑器。

# PARAMETERS

**--kernel** _NAME_
> 要连接的 Jupyter 内核（如 `python3`、`ir`、`julia-1.10`）。

**--no-kernel**
> 打开笔记本但不启动内核。

**--color-scheme** _NAME_
> 配色方案：`default`、`light`、`dark`、`inverse` 或自定义方案。

**--syntax-theme** _NAME_
> 代码单元格使用的 Pygments 主题。

**--tab-size** _N_
> 每个制表符对应的空格数。

**--terminal-graphics** _MODE_
> 图像协议：`sixel`、`iterm`、`kitty` 或 `none`。

**--log-level** _LEVEL_
> 日志详细程度（`debug`、`info`、`warning`、`error`）。

**--log-file** _FILE_
> 日志文件路径。

**--host** _HOST_（hub）
> SSH hub 的绑定地址。

**--port** _PORT_（hub）
> SSH hub 的监听端口。

**--save-as** _FILE_（preview）
> 将渲染输出写入 _FILE_ 而非标准输出。

**--page**（preview）
> 将渲染输出通过管道传给 `$PAGER`。

**-v**, **--version**
> 显示版本并退出。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**euporie** 是一套把 Jupyter 生态系统带入 Shell 的终端应用。每个子命令都是一个独立的应用，共享同一套渲染引擎，可渲染 markdown、LaTeX、语法高亮代码和富文本输出（包括通过 sixel、iTerm2 或 kitty 图形协议显示的内联图像）。

**notebook** 应用是一个完整的编辑器，可以执行单元格、管理内核并保存 `.ipynb` 文件。**console** 应用是任意已安装 Jupyter 内核的 REPL 前端。**preview** 应用是非交互式的，适合 CI 流水线或脚本使用。**hub** 通过 SSH 暴露笔记本编辑器，让多个用户共享服务器的资源。

# CONFIGURATION

每个应用都可以通过以应用名作为前缀的环境变量进行配置，例如 `EUPORIE_NOTEBOOK_COLOR_SCHEME=dark`、`EUPORIE_CONSOLE_KERNEL=python3`。所有应用都会加载 `~/.config/euporie/euporie.toml` 配置文件。

# KEYBINDINGS (notebook)

**Enter / Esc**
> 在当前单元格中切换编辑模式和命令模式。

**a** / **b**
> 在上方 / 下方插入单元格。

**dd**
> 删除当前单元格。

**y** / **m** / **r**
> 将单元格类型更改为 code / markdown / raw。

**Ctrl-Enter** / **Shift-Enter**
> 运行单元格 / 运行并跳到下一个。

**Ctrl-S**
> 保存笔记本。

**Ctrl-Q**
> 退出。

# CAVEATS

富文本输出（图像、图表）需要支持 sixel、iTerm2 或 kitty 图形的终端。基于 JavaScript 的复杂组件（ipywidgets）支持有限。hub 应用需要主机密钥和用户认证 — hub 配置请参阅文档。

# HISTORY

**euporie** 由 **Josiah Outram Halstead**（joouha）开发，用 **Python** 基于 **prompt_toolkit** 编写。它在 PyPI 上以 `euporie` 发行（用 `pip install euporie` 安装）。

# INSTALL

```aur: yay -S euporie```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jupyter](/man/jupyter)(1), [ipython](/man/ipython)(1)
