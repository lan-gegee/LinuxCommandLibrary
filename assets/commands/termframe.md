# TAGLINE

终端输出 SVG 截图工具

# TLDR

**将命令输出捕获为 SVG**

```termframe -o [output.svg] -- ls --color=always```

**自动检测终端尺寸**

```termframe --width auto --height auto -o [out.svg] -- [command]```

**使用指定的配色主题**

```termframe --theme "[Solarized Dark]" -o [out.svg] -- [command]```

# SYNOPSIS

**termframe** [_options_] **-o** _output.svg_ **--** _command_

# PARAMETERS

**-o**, **--output** _FILE_
> 输出 SVG 文件路径。

**-W**, **--width** _VALUE_
> 终端宽度（数字、auto 或 80..120 这样的范围）。

**-H**, **--height** _VALUE_
> 终端高度（数字、auto 或 24..50 这样的范围）。

**--theme** _NAME_
> 来自 iTerm2-Color-Schemes 的配色主题。

**--title** _TEXT_
> 设置窗口标题。

**--font-size** _SIZE_
> 调整字体大小。

**--padding** _VALUE_
> 配置窗口内边距。

**--window-style** _STYLE_
> 窗口样式（例如 macos、compact）。

**--shell** _SHELL_
> 指定要使用的 Shell。

**--config** _FILE_
> 覆盖配置文件路径（用 - 可禁用默认值）。

# DESCRIPTION

**termframe** 是一个非交互式终端模拟器：它执行一条命令，把输出渲染到虚拟终端会话中，并将结果导出为 SVG 文件。它支持完整的颜色范围（16 色、256 色、真彩色）、文本样式、字体嵌入和深色/浅色模式。

# HISTORY

**termframe** 由 **Pavel Ivanov**（pamburus）创建，使用 **Rust** 编写。

# INSTALL

```brew: brew install termframe```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[silicon](/man/silicon)(1), [t-rec](/man/t-rec)(1)
