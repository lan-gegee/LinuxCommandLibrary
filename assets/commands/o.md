# TAGLINE

轻快、免配置的终端文本编辑器和小型 IDE（orbiton）

# TLDR

**打开文件**

```o [file]```

**在指定行打开**

```o [file]:[line]```

**在指定行和列打开**

```o [file]:[line]:[column]```

**按子串匹配打开第一个文件**

```o -g [substring]```

**格式化文件**而非编辑

```o -F [file]```

**构建给定文件所在的**项目

```o -b [file]```

**监视文件**变更（类似 tail，只读）

```o -m [file]```

**将剪贴板内容粘贴到**新文件

```o -p [file]```

**列出所有双合键（digraph）**

```o -s```

# SYNOPSIS

**o** [_options_] [_file_[:_line_[:_col_]]]

# PARAMETERS

**-c**, **--copy**
> 将文件复制到剪贴板。

**-p**, **--paste**
> 将剪贴板内容粘贴到指定文件（配合 `-f` 可覆盖）。

**-f**, **--force**
> 打开时忽略文件锁。

**-m**, **--monitor**
> 监视文件变化；以只读方式打开。

**-t**, **--list**
> 带语法高亮打印文件后退出。

**-b**, **--build**
> 构建文件/项目而非编辑。

**-F**, **--format**
> 格式化文件而非编辑。

**-k**, **--create-dir**
> 为新文件按需创建父目录。

**-d**, **--debug**
> 以调试（gdb/dlv）模式启动。

**-r**, **--release**
> 在适用时以 release 模式而非 debug 模式构建。

**-l**, **--last-command**
> 打印最近一次使用的构建/格式化/导出命令并退出。

**-e**, **--clear-locks**
> 清除所有文件锁并关闭 portal。

**-n**, **--no-cache**
> 不写入历史、最高分或最近命令缓存。

**-i**, **--input-file** _FILE_
> 将 _FILE_ 作为通过 Ctrl-Space 启动的程序的 stdin。

**-a**, **--nano**
> 模拟 Pico/Nano 快捷键绑定。

**-o**, **--ollama**
> 启用 Ollama AI 功能（模型来自 `$OLLAMA_MODEL`）。

**-q**, **--quick-help**
> 启动时总是显示快速帮助面板。

**-z**, **--no-quick-help**
> 从不显示快速帮助面板。

**-x**, **--noapprox**
> 禁用近似文件名匹配。

**-g**, **--glob** _SUBSTRING_
> 打开第一个匹配该子串的文件名。

**-s**, **--digraphs**
> 列出所有支持的双合键并退出。

**-v**, **--version**
> 打印版本信息。

**-h**, **--help**
> 显示帮助。

# DESCRIPTION

**o**（即 **orbiton** 的可执行文件名）是一款小巧轻快、无需配置的终端文本编辑器和小型 IDE。它根据文件名检测语言，提供语法高亮、彩虹括号、宏录制、跨会话的剪切/粘贴 "portal"、从编译器输出跳转到错误位置、LSP 支持以及简单的 gdb/dlv 前端。

用 `o` 加文件名即可打开文件；追加 `:line` 或 `:line:col` 可跳转到相应位置。该编辑器刻意不设配置文件：大多数行为由文件类型和环境推断。配套的二进制 `ko` 以浅色主题打开；`lo` 减少色彩数量，适合低带宽终端。

# CAVEATS

与 shell 内建的 `o` 别名（如果存在）无关。某些发行版以不同的软件包名提供 orbiton（例如 `orbiton`、`o-editor`）。快捷键与 vim/emacs 不同；请参阅内建快速帮助（先按 `Ctrl-o` 再按 `?`）。

# HISTORY

**orbiton** 由 **Alexander F. Rødseth**（xyproto）创建。该项目使用 **Go** 编写，发布于 GitHub `xyproto/orbiton`，采用 BSD 3-clause 许可证。

# SEE ALSO

[vim](/man/vim)(1), [nano](/man/nano)(1), [micro](/man/micro)(1), [emacs](/man/emacs)(1)
