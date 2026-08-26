# TAGLINE

极速的通用模糊查找器 TUI

# TLDR

**模糊搜索当前目录中的文件**

```tv```

**搜索文件内容**

```tv text```

**查找 git 仓库**

```tv git-repos```

# SYNOPSIS

**tv** [_options_] [_channel_] [_path_]

# DESCRIPTION

**television** 是一个快速、便携且可深度定制的模糊查找器，灵感来自 Neovim 的 Telescope 插件。它通过"频道（channels）"系统对文件、文本、git 仓库、环境变量、Docker 容器等进行实时搜索。它使用 nucleo 模糊匹配库和 ratatui 进行渲染。

# HISTORY

**television** 由 **Alex Pasmantier**（alexpasmantier）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S television```

```brew: brew install television```

```nix: nix profile install nixpkgs#television```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[fzf](/man/fzf)(1)
