# TAGLINE

将 Jupyter 笔记本转换为文本格式

# TLDR

**将笔记本转换为 Python percent 脚本**

```jupytext --to py:percent [notebook.ipynb]```

**将 Python 脚本转换回笔记本**

```jupytext --to ipynb [script.py]```

**将笔记本转换为 Markdown 并写入指定输出文件**

```jupytext --to md --output [output.md] [notebook.ipynb]```

**将笔记本与 Python percent 脚本配对以便版本控制**

```jupytext --set-formats ipynb,py:percent [notebook.ipynb]```

**同步所有配对的表示形式，更新其中过时的文件**

```jupytext --sync [notebook.ipynb]```

**将文本表示通过 black 管道处理后就地重新格式化**

```jupytext --pipe black [notebook.ipynb]```

**将 Markdown 笔记本转换为 ipynb 并执行**

```jupytext --to notebook --execute [notebook.md]```

# SYNOPSIS

**jupytext** [_options_] _notebook_ [_notebook_ ...]

# PARAMETERS

**--to** _FORMAT_
> 目标格式。常见值：`py`、`py:percent`、`py:light`、`ipynb`、`md`、`md:myst`、`Rmd`。`:` 之后的部分选择子格式。

**--from** _FORMAT_
> 显式指定源格式，从 stdin 读取时必须提供。

**-o** _FILE_, **--output** _FILE_
> 输出文件路径。用 `-` 表示写入 stdout。

**--sync**
> 根据文件时间戳同步笔记本的所有配对表示形式，更新其中过时的副本。

**--set-formats** _FORMATS_
> 将笔记本与一种或多种其他格式配对（如 `ipynb,py:percent`）。配对元数据会写入笔记本中。

**--update**
> 转换为已存在的 `.ipynb` 文件时，保留已有的输出和元数据，只更新输入单元格。

**--pipe** _CMD_
> 将笔记本的文本表示通过外部命令处理（如 `black` 或 `isort`）。当命令不接受 stdin 时，用 `{}` 作为临时文件的占位符。

**--pipe-fmt** _FORMAT_
> 管道处理时使用的格式（默认：`py:percent`）。

**--check** _CMD_
> 对文本表示运行命令，返回非零退出码则判定失败。用 `{}` 作为临时文件的占位符。

**--execute**
> 转换后执行笔记本单元格（需要 `nbconvert`）。

**--set-kernel** _NAME_
> 设置笔记本 YAML 头部中的内核。用 `-` 表示使用与当前 Python 可执行文件匹配的内核。

**--update-metadata** _JSON_
> 用提供的 JSON 字符串更新笔记本级元数据（如 `'{"kernelspec":{"name":"python3"}}'`）。

**--opt** _KEY=VALUE_
> 设置某个 jupytext 选项，如 `comment_magics=false`。

**--test**
> 测试往返转换（notebook -> text -> notebook）是否无损。

**--test-strict**
> 与 `--test` 类似，但对两个笔记本执行严格的逐字节比较。

**--help**
> 显示帮助信息。

# DESCRIPTION

**Jupytext** 将 Jupyter 笔记本转换为纯文本格式（如 Python 脚本和 Markdown 文件），也能转换回来。这让笔记本适合纳入版本控制、进行代码评审，以及在标准 IDE 中编辑。

最常见的工作流是用 `--set-formats` 将 `.ipynb` 笔记本与 `.py` 或 `.md` 文件配对。配对完成后，运行 `--sync` 即可保持两个文件同步更新：配对的文本文件干净地记录输入内容以便版本控制，而 `.ipynb` 则保留单元格输出。

`percent` 格式（`py:percent`）是推荐的脚本格式。单元格以 `# %%` 标记分隔，文件本身是合法的 Python 代码。`light` 格式使用最少的标记。基于 Markdown 的格式包括普通 `md`、`md:myst`（MyST Markdown，兼容 Jupyter Book）以及 `Rmd`（R Markdown）。

Jupytext 还可作为扩展集成到 JupyterLab 中：文本笔记本会显示笔记本图标，可以直接启动。它也能配合 pre-commit 钩子实现自动化格式化。

# CAVEATS

单元格输出（图片、表格、富媒体内容）不会保存在文本格式中，除非配对了 `.ipynb` 文件，否则转换时会丢失。`.ipynb` 文件必须存在，或通过执行笔记本来重新生成输出。

# HISTORY

Jupytext 由 **Marc Wouts** 开发，旨在解决 Jupyter 笔记本的版本控制难题。它最初是一个 JupyterLab 扩展，后来加入了完整的命令行界面。

# INSTALL

```brew: brew install jupytext```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jupyter](/man/jupyter)(1), [jupyter-lab](/man/jupyter-lab)(1), [black](/man/black)(1), [isort](/man/isort)(1)
