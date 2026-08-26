# TAGLINE

从多个仓库引入 Shell 配置的 Dotfiles 管理器

# TLDR

从 freshrc **构建 Shell 配置**和符号链接

```fresh```

**更新所有源仓库**并重新构建

```fresh update```

仅**更新本地 dotfiles 仓库**

```fresh update --local```

**更新特定 GitHub 用户**的仓库

```fresh update [username]```

**在 fresh 目录中搜索**配置示例

```fresh search [keyword]```

**编辑你的 freshrc** 配置文件

```fresh edit```

**清理失效符号链接**和无用的源仓库

```fresh clean```

显示 freshrc 各行的**来源引用**

```fresh show```

# SYNOPSIS

**fresh** [_command_] [_options_]

# PARAMETERS

**install**
> 构建 Shell 配置并创建符号链接。未给出命令时这是默认行为。

**update** [_filter_]
> 从源仓库拉取最新更改并重新构建。可用 **--local**、GitHub _username_ 或 _username/repo_ 过滤。

**clean**
> 移除失效符号链接和无用的源仓库。

**search** _keyword_
> 在 fresh 目录 wiki 中查询与 _keyword_ 匹配的配置示例。

**edit**
> 在默认的 **$EDITOR** 中打开 **~/.freshrc**。

**show**
> 显示 freshrc 各行及其对应的源文件。

**help**
> 显示用法文档。

# DESCRIPTION

**fresh** 是一个 dotfiles 管理器，对你的 Shell 配置而言就像 Bundler 一样工作。它把你自己的 dotfiles 以及其他用户的 GitHub 仓库中的别名、函数、补全和配置文件聚合为一个构建好的 shell 脚本和一组符号链接。

配置通过简单的 DSL 在 **~/.freshrc** 中定义。每一行指定要引入的一个源文件，可选地来自某个 GitHub 仓库。当 **fresh** 运行时，它把所有 shell 源拼接成 **~/.fresh/build/shell.sh**，并为非 shell 配置文件创建符号链接。你在 shell 的 rc 文件中 source 构建产物即可启用一切。

Fresh 支持三种被引入的内容类型：**shell 文件**（拼接到构建脚本中）、**配置文件**（通过 **--file** 创建符号链接）以及 **bin 文件**（通过 **--bin** 使其可执行）。

# FRESHRC OPTIONS

**--file**[**=**_path_]
> 链接或构建配置文件。带路径时（如 **--file=~/.vimrc**），文件会被符号链接到该位置；不带路径时，文件按原名拼接到 **~/.fresh/build/** 中。

**--bin**[**=**_path_]
> 在 **~/bin/**（或自定义路径）中创建可执行符号链接。源文件会自动被赋予可执行权限。

**--ref=**_ref_
> 将源锁定到特定的 git 分支、标签或提交哈希。

**--filter=**_command_
> 在引入前将源文件通过一条 shell 命令处理（例如 **--filter="gpg -d"**）。

**--marker=**_string_
> 在被引入内容周围添加注释标记，便于在构建产物中识别。

**--ignore-missing**
> 当源文件不可用时抑制报错。

# CONFIGURATION

Fresh 使用 **~/.freshrc** 作为配置文件。源以下列方式指定：

```
# Local file from ~/.dotfiles/
fresh aliases.sh

# File from a GitHub repository
fresh jasoncodes/dotfiles shell/aliases/git.sh

# Non-GitHub git URL
fresh git://example.com/repo.git file.conf --file=~/.config/app.conf

# Executable script
fresh freshshell/fresh contrib/completion/fresh-completion.bash --bin
```

使用 **fresh-options** 块可为多行统一应用选项：

```
fresh-options --file=~/.vimrc --marker='"'
  fresh vim/mappings.vim
  fresh vim/plugins.vim
fresh-options
```

可自定义的环境变量：

**FRESH_RCFILE** — 配置文件路径（默认：**~/.freshrc**）
**FRESH_PATH** — 安装目录（默认：**~/.fresh**）
**FRESH_LOCAL** — 本地 dotfiles 仓库（默认：**~/.dotfiles**）
**FRESH_BIN_PATH** — 可执行文件安装目录（默认：**~/bin**）
**FRESH_NO_LOCAL_CHECK** — 禁用本地引入警告
**FRESH_NO_PATH_EXPORT** — 跳过自动修改 PATH
**FRESH_NO_BIN_CONFLICT_CHECK** — 抑制多来源二进制文件冲突警告

# CAVEATS

Fresh 需要已安装 **git** 和 **bash**。所有 shell 源都会拼接进同一个文件，因此不同仓库引入的函数或别名之间的命名冲突必须手动管理。构建出的 shell 脚本必须由你在 **.bashrc** 或 **.zshrc** 中显式 source —— fresh 不会自动修改这些文件。

# HISTORY

**fresh** 由 **Jason Weathered**（jasoncodes）和 **Scott Barron**（twe4ked）创建，是以 **MIT license** 发布的开源 Shell 工具。它的灵感来自 Ruby 的 Bundler，把同样的依赖引入理念应用到了 Shell 生态中的 dotfiles 管理。

# SEE ALSO

[git](/man/git)(1), [bash](/man/bash)(1), [stow](/man/stow)(8), [dotbot](/man/dotbot)(1)
