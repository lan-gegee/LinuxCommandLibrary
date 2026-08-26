# TAGLINE

并排管理多个 Git 仓库

# TLDR

显示所有已注册仓库的**状态**

```gita ll```

**注册要跟踪的仓库**

```gita add [path/to/repo1] [path/to/repo2]```

**递归发现并添加**某个目录下的所有仓库

```gita add -a [path/to/parent]```

对所有已注册仓库**运行 git 命令**

```gita fetch```

对特定仓库运行**任意 git 命令**

```gita super [repo1] [repo2] -c "git [command]"```

对所有仓库运行 **shell 命令**

```gita shell -c "[command]"```

**列出**所有已注册仓库名称

```gita ls```

将仓库从跟踪中**移除**

```gita rm [repo_name]```

# SYNOPSIS

**gita** [_subcommand_] [_options_] [_repos_]

# PARAMETERS

**add** _path(s)_
> 注册要跟踪的仓库。使用 **-a** 可递归发现某目录下的所有仓库，**-b** 用于裸仓库。

**rm** _repo(s)_
> 取消仓库的注册，不再跟踪。

**ls**
> 列出所有已注册仓库的名称。

**ll**
> 显示所有仓库的详细状态，包括分支、同步状态和修改情况。

**fetch**
> 对所有已注册仓库执行 git fetch。

**pull**
> 对所有已注册仓库执行 git pull。

**super** [_repos_] **-c** _"git command"_
> 将任意 git 命令委派给指定仓库（未指定则作用于全部）。

**shell** [_repos_] **-c** _"command"_
> 在每个仓库目录中运行任意 shell 命令。

**freeze**
> 导出仓库路径和 URL，用于备份或分享。

**clone** _url_
> 克隆一个仓库并将其注册。

**group add** _repos_ **-n** _name_
> 创建一个命名的仓库组。

**group ll**
> 列出所有组及其内容。

**group rm** _name_
> 删除一个命名组。

**context** _group_
> 将后续命令限制在特定组内。使用 **none** 清除。

**info**
> 配置 **ll** 输出中显示哪些信息项。

**color**
> 管理分支状态显示的配色方案。

**flags set** _repo_ _flags_
> 为特定仓库设置自定义 git 标志。

# DESCRIPTION

**gita** 是一个用于同时管理多个 Git 仓库的命令行工具。它提供统一的仓库状态视图，并支持从任意工作目录对所跟踪的全部仓库批量执行 git 命令，无需逐个 cd 进入各仓库。

仓库通过 **gita add** 注册，其路径存储在 **$XDG_CONFIG_HOME/gita/repos.csv** 中。注册后，**gita ll** 会以彩色编码的方式汇总每个仓库的分支、同步状态（领先/落后远程多少）以及工作树修改情况。像 **fetch** 和 **pull** 这类 git 命令可以一次性委派给所有仓库，任意 git 或 shell 命令也可通过 **super** 和 **shell** 子命令运行。

仓库可以组织成命名的**组**，并通过 **context** 限定操作范围。组、配色、显示信息和自定义命令等配置文件存储在 **$XDG_CONFIG_HOME/gita/** 中。

# CAVEATS

需要 **Python 3.6+**。批处理操作在各仓库间异步执行，但需要用户交互的命令（如 **log**、**difftool**、**mergetool**）会同步运行，以避免输出错乱。默认情况下只有 **fetch** 和 **pull** 允许在不指定目标的情况下跨所有仓库运行；其他命令需要显式指定仓库名，除非自定义配置改变了这一行为。在 Windows 上必须手动启用 ANSI 颜色输出。

# HISTORY

**gita** 由 **nosarthur** 创建，于 **2018 年 1 月**首次发布。它用 **Python** 编写，通过 PyPI 分发，可用 pip、pipx 或 uv 安装。名字是 "git" 加上一个 "a"，寓意管理多个仓库。该项目采用 MIT 许可证并持续活跃维护。

# INSTALL

```nix: nix profile install nixpkgs#gita```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [mr](/man/mr)(1), [ghq](/man/ghq)(1)
