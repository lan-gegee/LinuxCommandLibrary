# TAGLINE

列出、搜索和创建 git 别名

# TLDR

**列出**所有别名

```git alias```

**搜索**匹配某个模式的别名

```git alias [pattern]```

**创建**一个别名

```git alias [co] "[checkout]"```

在全局配置中**创建**别名

```git alias --global [st] "[status -sb]"```

仅为当前仓库**创建**别名

```git alias --local [dc] "[diff --cached]"```

**创建**一个运行 shell 命令的别名

```git alias [amend] "[!git commit --amend --no-edit]"```

# SYNOPSIS

**git alias** [_options_]

**git alias** [_options_] _search-pattern_

**git alias** [_options_] _alias-name_ _command_

# PARAMETERS

**--global**
> 在全局（用户）配置中显示或创建别名。

**--local**
> 在仓库配置中显示或创建别名。

_search-pattern_
> 只显示匹配该模式的别名。模式会传给 **grep**，因此它是正则表达式，而不是通配符。

_alias-name_ _command_
> 创建一个将 _alias-name_ 映射到 _command_ 的别名。

# DESCRIPTION

**git alias** 是 git-extras 提供的辅助工具，用于管理 git 配置中的 **[alias]** 区段。它是 **git config** 的薄封装，但语法足够简短，可以随口使用。

不带参数时，它列出 git 可见的所有别名，格式为 **name = command** 并排序。带一个参数时过滤该列表。带两个参数时创建别名：**git alias co checkout** 会让 **git co** 运行 **git checkout**。

以 **!** 开头的别名将作为 shell 命令而非 git 子命令运行，需要串联命令或接受参数的别名就是这样写的。

不带 **--global** 或 **--local** 时，列表操作显示所有配置层级的合并视图，而创建操作会写入普通 **git config** 会写入的位置——当你在仓库内时通常就是仓库的 **.git/config**。

# CONFIGURATION

**~/.gitconfig**
> 全局别名，由 **--global** 写入，位于 **[alias]** 区段。

**.git/config**
> 仓库本地别名，由 **--local** 写入。

# CAVEATS

尽管内置帮助把 **--global** 描述为"系统配置"，它实际写入的是你的用户配置（**~/.gitconfig**）。真正的系统级配置是 **git config --system**，这个封装并未提供。

创建同名别名会静默覆盖已有别名；没有确认提示，除了重新写入值之外也无法撤销。

搜索模式不加引号直接传给 **grep**，因此 **.** 和 ***** 等字符是正则元字符，匹配范围可能超出预期。

别名不能遮蔽 git 内置命令。**git alias status "log"** 能被配置接受，但 git 仍会运行真正的 **status**。

传入超过两个参数会报错，因此多词命令必须作为一个参数加引号。

# HISTORY

**git alias** 是 **git-extras** 的一部分，由 **TJ Holowaychuk** 于 **2010 年**创建，现由社区维护。它所封装的 Git 自身别名机制自 git 早期就已存在于 **git config** 中。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-config](/man/git-config)(1), [git-extras](/man/git-extras)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/tj/git-extras)```

```[Documentation](https://github.com/tj/git-extras/blob/master/Commands.md#git-alias)```

<!-- verified: 2026-07-16 -->
