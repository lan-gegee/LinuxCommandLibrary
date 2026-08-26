# TAGLINE

高度可扩展的基于 Vim 的文本编辑器

# TLDR

**打开文件**

```neovim [path/to/file]```

**打开文件并定位到指定行**

```neovim +[line_number] [path/to/file]```

**查看文件间的差异**

```neovim -d [file1] [file2]```

**以只读模式打开**

```neovim -R [path/to/file]```

# SYNOPSIS

**neovim** [_options_] [_files_...]

# DESCRIPTION

**neovim**（通常以 **nvim** 调用）是一款基于 Vim、经现代化架构重构的高度可扩展文本编辑器。它具有内置 LSP 客户端、基于 Treesitter 的语法高亮、基于 Lua 的配置与插件系统、内嵌终端模拟器以及异步任务控制。

Neovim 与大多数 Vim 配置保持向后兼容，同时提供更易维护、更可扩展的代码库。它支持通过 RPC 使用远程插件，可与外部工具和 GUI 集成。

# CONFIGURATION

**~/.config/nvim/init.lua**
> 主配置文件（基于 Lua，替代 init.vim）。

# CAVEATS

部分 Vim 插件可能不兼容。推荐的配置语言是 Lua 而非 Vimscript。

# HISTORY

**Neovim** 于 **2014 年**由 **Thiago de Arruda** 发起，是 Vim 的一个分支，目标是彻底重构和现代化。它使用 **C** 和 **Lua** 编写。

# INSTALL

```dnf: sudo dnf install neovim```

```pacman: sudo pacman -S neovim```

```zypper: sudo zypper install neovim```

```brew: brew install neovim```

```nix: nix profile install nixpkgs#neovim```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[nvim](/man/nvim)(1), [vim](/man/vim)(1), [vi](/man/vi)(1)
