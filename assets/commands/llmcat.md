# TAGLINE

将文件和目录整理成适合 LLM 使用的内容

# TLDR

**打开**交互式 fzf 选择器并将所选内容复制到剪贴板

```llmcat```

**复制**单个文件并附带格式化的头部

```llmcat [path/to/file.txt]```

**遍历**目录并复制每个未被忽略的文件

```llmcat [./src]```

**仅打印**目录树，不包含文件内容

```llmcat --tree-only [./src]```

在 **.gitignore** 之上**添加**自定义忽略模式

```llmcat -i [*.log] -i [*.tmp] [./src]```

**包含**隐藏文件并跳过 **.gitignore** 规则

```llmcat --hidden --no-ignore [./src]```

**显示**复制到剪贴板的内容

```llmcat -p [./src]```

# SYNOPSIS

**llmcat** [_options_] [_path_]

# PARAMETERS

**-i**, **--ignore** _PATTERN_
> 向忽略列表添加 glob 模式（可重复使用；采用 **fd** 的 glob 格式）。

**-t**, **--tree-only**
> 只输出目录树，不含文件内容。

**-p**, **--print**
> 除复制到剪贴板外，还将复制的输出打印到 stdout。

**-n**, **--no-ignore**
> 遍历目录树时忽略 **.gitignore** 文件。

**-H**, **--hidden**
> 包含隐藏文件和目录。

**-q**, **--quiet**
> 静默模式——复制到剪贴板但不打印任何内容。

**-h**, **--help**
> 显示用法信息。

**-v**, **--version**
> 打印版本号并退出。

# INTERACTIVE KEYBINDINGS

```
Tab        Mark / unmark file
Shift-Tab  Unmark file
Ctrl-/     Toggle preview pane
Ctrl-D     Switch to directory mode
Ctrl-F     Switch to file mode
Enter      Confirm selection
Esc        Exit without copying
```

# DESCRIPTION

**llmcat** 将源码文件打包成单个对 LLM 友好的文本块并复制到系统剪贴板。每个文件都带有包含其路径的头部包装，这样 **ChatGPT** 或 **Claude** 等聊天助手就能识别每个片段来自哪个文件。默认情况下，目录遍历会遵循 **.gitignore**，并可通过 **-i** 添加额外的忽略模式。

不带路径调用时，llmcat 会打开一个由 **fzf** 驱动的模糊选择器，带实时预览窗格，支持通过 **Tab** 多选文件。带路径参数时，它会跳过选择器并以非交互方式处理目标，这在 shell 脚本和编辑器集成中很有用。

# CAVEATS

llmcat 的交互式选择器依赖 **fzf**，剪贴板功能依赖系统剪贴板工具（macOS 上是 **pbcopy**，Linux 上是 **xclip** 或 **wl-copy**）。超大目录的输出可能超出 LLM 的上下文窗口——请将 **--tree-only** 与有针对性的 **-i** 模式结合使用，或先通过 token 计数工具处理。GitHub 上还有几个同名的无关项目也叫 *llmcat*；本页面记录的是 **azer/llmcat** 实现。

# HISTORY

**llmcat** 由 **Azer Koçulu**（**azer**）创建，发布于 **github.com/azer/llmcat**。它是 2024–2025 年间围绕"把代码粘贴到聊天助手"这一工作流涌现的多款 "cat for LLMs" 工具之一。

# SEE ALSO

[fzf](/man/fzf)(1), [bat](/man/bat)(1), [fd](/man/fd)(1), [pbcopy](/man/pbcopy)(1), [xclip](/man/xclip)(1)
