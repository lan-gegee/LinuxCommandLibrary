# TAGLINE

终端中的 VS Code 风格搜索替换 TUI

# TLDR

**在当前目录启动搜索替换**

```serpl```

**在指定的项目目录中搜索替换**

```serpl --project-root [/path/to/project]```

**显示版本和配置文件位置**

```serpl --version```

# SYNOPSIS

**serpl** [_--project-root PATH_]

# PARAMETERS

**--project-root** _PATH_
> 指定搜索操作的项目根目录。默认为当前目录。

**--version**
> 显示版本信息和配置文件路径。

# DESCRIPTION

**serpl** 是一款 TUI 工具，让你在整个项目文件夹中搜索并替换文本，模仿 VS Code 的搜索替换体验。它使用 **ripgrep** 进行快速搜索，并可选配合 **ast-grep** 实现语法感知匹配。它支持多种搜索模式（简单、区分大小写、全词匹配、正则、AST Grep）和替换模式（简单、保留大小写），并在提交修改前提供交互式预览。快捷键可通过 **config.json** 文件进行配置。

# CAVEATS

需要安装 **ripgrep**。可选的 AST Grep 模式需要在安装时带上 **ast_grep** 特性标志（`cargo install serpl --features ast_grep`）。

# HISTORY

**serpl** 由 **Yassine Bridi**（yassinebridi）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S serpl```

```brew: brew install serpl```

```nix: nix profile install nixpkgs#serpl```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[scooter](/man/scooter)(1), [sed](/man/sed)(1), [rg](/man/rg)(1), [ast-grep](/man/ast-grep)(1)
