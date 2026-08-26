# TAGLINE

模糊查找并运行 make、npm、just 和 task 目标

# TLDR

在当前项目中**选择并运行**目标

```fzf-make```

**显示帮助**

```fzf-make --help```

# SYNOPSIS

**fzf-make** [*options*]

# DESCRIPTION

**fzf-make** 会打开一个带预览窗口的模糊查找器，让你选择并执行构建/任务目标。支持的任务系统：

- **make**（包括 **include** 指令）
- **npm** / **pnpm** / **yarn**（包括 yarn workspaces 脚本）
- **just** recipes
- **task**（Taskfile；通过 **task --list-all --json** 列出，包括 **includes**）

请在包含相应 **Makefile**、**package.json**、**justfile** 或 **Taskfile** 的项目目录中运行。

可通过 Homebrew、AUR、Nix、**cargo install --locked fzf-make** 或 Linux 发行版二进制包（**linux_amd64** / **linux_arm64**）安装。

# PARAMETERS

可用标志因版本而异（历史记录、配置和 UI 选项随版本演进），详见 **fzf-make --help**。主要用法是交互式的，无需任何必需参数。

# CAVEATS

需要终端 UI，且所选项目类型对应的底层工具（**make**、**npm**、**task** 等）已安装。行为取决于目标的声明方式；格式错误的 Makefile 或 Taskfile 可能导致列表不完整。

# INSTALL

```brew: brew install fzf-make```

```nix: nix profile install nixpkgs#fzf-make```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[make](/man/make)(1), [just](/man/just)(1), [task](/man/task)(1), [fzf](/man/fzf)(1)

# RESOURCES

```[Source code](https://github.com/kyu08/fzf-make)```

<!-- verified: 2026-07-19 -->
