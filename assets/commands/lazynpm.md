# TAGLINE

npm 命令的终端 UI

# TLDR

在当前项目中**启动 npm TUI**

```lazynpm```

# SYNOPSIS

**lazynpm** [_options_]

# DESCRIPTION

**lazynpm** 是一个用于管理 npm 工作流的终端 UI。它为掌控 Node.js 项目提供了一个简洁直观的 TUI，让你无需记忆复杂的命令行语法就能管理依赖、运行脚本并执行常见的 npm 操作。

它是 **lazygit** 和 **lazydocker** 的弟弟，秉持相同的设计理念：通过交互式界面让终端工作流更加平易近人。

# CAVEATS

需要先安装 npm 和 Node.js。必须在包含 package.json 文件的目录中运行。

# HISTORY

**lazynpm** 由 **Jesse Duffield**（jesseduffield）创建，使用 **Go** 基于 gocui 库编写。

# INSTALL

```nix: nix profile install nixpkgs#lazynpm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [lazygit](/man/lazygit)(1), [lazydocker](/man/lazydocker)(1)
