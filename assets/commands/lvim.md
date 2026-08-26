# TAGLINE

预配置的 Neovim 发行版，具备类 IDE 特性

# TLDR

**启动 LunarVim**

```lvim```

**打开文件**进行编辑

```lvim [file.py]```

**在指定行打开文件**

```lvim +[10] [file.py]```

从命令行**更新 LunarVim**

```lvim +LvimUpdate +q```

在标签页中**打开多个文件**

```lvim -p [file1.py] [file2.py]```

**以 diff 模式启动**

```lvim -d [file1.py] [file2.py]```

为脚本化运行 **headless 模式**

```lvim --headless +'lua print("hello")' +q```

# SYNOPSIS

**lvim** [_options_] [_file_...]

# PARAMETERS

**+**[_num_]
> 将光标定位到指定行号。

**+/**_pattern_
> 将光标定位到首个匹配模式的行。

**-c** _command_
> 加载文件后执行命令。

**-o**[_N_]
> 打开 N 个水平分割的窗口。

**-O**[_N_]
> 打开 N 个垂直分割的窗口。

**-p**[_N_]
> 打开 N 个标签页。

**-d**
> 以 diff 模式启动。

**-R**
> 只读模式。

**--headless**
> 无 UI 启动，用于脚本化。

**--clean**
> 以最小配置启动。

**-u** _config_
> 使用替代的配置文件。

**-h**, **--help**
> 显示帮助信息。

**-v**, **--version**
> 显示版本信息。

# EDITOR COMMANDS

**:LvimUpdate**
> 将 LunarVim 更新到最新版本。

**:LvimSyncCorePlugins**
> 刷新核心插件。

**:LvimCacheReset**
> 清除缓存数据。

**:LvimInfo**
> 显示 LunarVim 信息。

**:LvimDocs**
> 打开文档。

# DESCRIPTION

**lvim**（LunarVim）是一个预配置的 Neovim 发行版，开箱即用地提供类 IDE 体验。它包含精选的插件、键位绑定和合理的默认设置，同时仍可完全自定义。

LunarVim 内置对 LSP（Language Server Protocol）的支持，提供智能代码补全、诊断和重构。Treesitter 提供高级语法高亮和代码导航。which-key 插件会根据上下文显示可用的键位绑定。

配置通过 Lua 编写，位于 **~/.config/lvim/config.lua**。全局对象 **lvim** 暴露插件、键位绑定和编辑器选项的设置。自定义插件可以通过 lvim.plugins 表添加。

由于 LunarVim 构建在 Neovim 之上，所有 Neovim 命令行选项都受支持。该编辑器继承了 Vim 的模态编辑范式，包括 Normal、Insert、Visual 和 Command-line 模式。

# CAVEATS

需要 Neovim 0.9.0 或更高版本，以及 git、make、pip、npm、node、cargo 和 ripgrep。初始安装会下载并编译多个插件，需要联网。若出现破坏性变更，更新可能偶尔需要手动干预。

# HISTORY

LunarVim 由 **Christian Chiarulli** 于 **2021 年**创建，旨在提供"电池全含"的 Neovim 体验。作为从零构建自定义 Neovim 配置之外更容易上手的替代方案而广受欢迎。注意：该项目已被**归档**，自 **2024 年**起不再积极维护。

# SEE ALSO

[nvim](/man/nvim)(1), [vim](/man/vim)(1)
