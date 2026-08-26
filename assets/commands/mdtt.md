# TAGLINE

带 vim 风格按键绑定的 Markdown 表格编辑 TUI

# TLDR

从文件**编辑 markdown 表格**

```mdtt [path/to/file.md]```

以交互方式**创建新表格**

```mdtt```

# SYNOPSIS

**mdtt** [_options_] [_file_]

# DESCRIPTION

**mdtt** 是一个带 vim 风格按键绑定的终端 Markdown 表格编辑器。导航使用 **hjkl** 键，**i** 切换到插入模式编辑单元格内容，**Esc** 返回普通模式。

功能包括：使用 **o**/**vo** 添加行列、使用 **dd**/**vd** 删除行列、输出到标准输出及就地编辑文件、将单元格编辑委托给外部 **$EDITOR**，以及支持表格单元格内的 HTML 以实现富内容格式化。

# CAVEATS

只能编辑 Markdown 表格。文件中的其他 Markdown 内容会保留，但无法通过 TUI 编辑。

# HISTORY

**mdtt** 由 **szktkfm** 创建，使用 **Go** 编写。

# INSTALL

```aur: yay -S mdtt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vim](/man/vim)(1)
