# TAGLINE

myrepos — 在大量仓库上一次性运行版本控制命令

# TLDR

**更新所有已注册的仓库**

```mr update```

**检查所有仓库的状态**

```mr status```

以同一条消息在所有仓库中**提交更改**

```mr commit -m "[message]"```

将当前仓库**注册**到 `~/.mrconfig`

```mr register```

在每个仓库内**运行任意命令**

```mr run [git fetch]```

只在当前目录子树内的仓库上运行

```mr -d [.] status```

**列出已配置的仓库**

```mr list```

从共享的 `.mrconfig` **引导检出全新副本**

```mr checkout```

**使用非默认的配置文件**

```mr -c [/path/to/mrconfig] update```

**串行运行**（禁用默认的并行任务）

```mr -s update```

# SYNOPSIS

**mr** [_options_] _command_ [_command args_]

# PARAMETERS

**-c** _CONFIG_
> 使用 _CONFIG_ 代替 `$HOME/.mrconfig`。

**-d** _DIR_
> 只对位于 _DIR_（或其最近的上级目录）的仓库进行操作。

**-t** _SECONDS_
> 每个子命令在 _SECONDS_ 秒后超时。

**-j** _N_
> 并行运行 _N_ 个任务（默认 1，`-j0` 表示无限制）。

**-s**
> 遇到第一个错误即停止（使用 `-j` 时也会转为串行执行）。

**-i**
> 交互模式：每次操作前先提示确认。

**-n**
> 限制递归：只处理路径位于当前目录之下的仓库。

**-p** _DIR_
> 运行前先切换到目录 _DIR_。

**-f**
> 即使仓库被标记为 `skip` 也强制执行操作。

**-v**
> 详细输出。

**-q**
> 安静模式：抑制 mr 及其子进程的标准输出。

**-m**
> 提交消息（用于 `commit`）。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# COMMON COMMANDS

**checkout** — 克隆配置中列出的每个仓库。
**update** — 按仓库分别执行 `git pull --rebase` / `svn update` / `hg pull -u` 等。
**status** — 显示每个仓库的工作区状态。
**commit** — 提交（用 `-m` 设置消息）。
**push** / **pull** / **fetch** — 各版本控制系统的封装命令。
**diff** / **log** — 按仓库查看差异或日志。
**run** _CMD_ — 在每个仓库目录中运行 _CMD_。
**register** [_DIR_] — 将仓库（默认为当前目录）加入配置。
**list** — 显示将要被操作的仓库。
**config** [_REPO_] [_KEY_ [_VALUE_]] — 读/写配置键。
**bootstrap** _URL_ — 从 URL 获取 `.mrconfig` 并运行 `checkout`。
**online** / **offline** — 将仓库标记为可达/不可达，供之后的 `--online-only` 运行使用。
**help** — 显示某个特定命令的帮助。

# CONFIGURATION

主配置文件为 **~/.mrconfig**，此外也包括当前目录树中的任意 `.mrconfig`。

每个小节对应一个仓库；`[DEFAULT]` 小节保存默认值。命令以 shell 块的形式定义：

```
[src/vim]
checkout = git clone git@github.com:you/vim .
update = git pull --rebase
skip = [ "$1" = "fetch" ] && ! mr_any_args
```

开箱即支持的后端：git、subversion、mercurial、bazaar、cvs、darcs、fossil、veracity、git-svn、unison。可以通过编写匹配的动作来添加自定义后端。

# DESCRIPTION

**mr**（myrepos）用于在一组异构仓库集合上统筹版本控制操作。它从一个或多个 `.mrconfig` 文件读取各仓库的动作定义并执行它们，因此一条 `mr update` 就能一次性拉取数十个 git 仓库、一个 svn 检出和一个 mercurial 克隆。并行执行（`-j`）、超时（`-t`）和按仓库的 `skip` 规则使它在大规模场景下也很实用。

# CAVEATS

需要 Perl。并行模式下输出会交错；需要整洁日志时请使用 `-j1`（默认值）。`mr commit` 只提交已暂存（或已被跟踪，取决于具体 VCS）的更改——它不会添加新文件。

# HISTORY

**mr** / **myrepos** 由 **Joey Hess** 创建，目前由 **Richard Hartmann**（RichiH）维护。自 2000 年代后期起就进入 Debian 软件包体系，是 `vcsh` 和 `gita` 等工具的精神先驱。

# INSTALL

```dnf: sudo dnf install myrepos```

```pacman: sudo pacman -S myrepos```

```apk: sudo apk add myrepos```

```zypper: sudo zypper install mr```

```brew: brew install myrepos```

```nix: nix profile install nixpkgs#mr```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [vcsh](/man/vcsh)(1), [gita](/man/gita)(1)
