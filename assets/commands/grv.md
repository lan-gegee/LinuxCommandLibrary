# TAGLINE

查看 Git 仓库的终端界面

# TLDR

在 grv 中**打开当前仓库**

```grv```

**打开特定仓库**

```grv -repoFilePath [path/to/repo]```

**以指定日志级别打开**

```grv -logLevel [NONE|PANIC|FATAL|ERROR|WARN|INFO|DEBUG|TRACE]```

**以只读模式打开**

```grv -readOnly```

# SYNOPSIS

**grv** [**-repoFilePath** _path_] [**-workTreeFilePath** _path_] [**-logFile** _path_] [**-logLevel** _level_] [**-readOnly**] [**-version**]

# DESCRIPTION

**GRV**（Git Repository Viewer）是一个基于终端的 Git 仓库查看界面。它允许使用**类似 Vi/Vim 的按键绑定**来查看、搜索和过滤引用、提交和差异。界面提供多种视图：用于分支和标签的 ref 视图、用于浏览历史的 commit 视图，以及用于检查变更的 diff 视图。

GRV 通过 libgit2 直接读取仓库，而不是调用 git 命令，因此即使在大型仓库中也能快速导航。其行为和样式可通过 **.grvrc** 配置文件自定义。

# PARAMETERS

**-repoFilePath** _path_
> 仓库文件路径（默认："."）

**-workTreeFilePath** _path_
> 工作树文件路径

**-logFile** _path_
> 日志文件路径（默认："grv.log"）

**-logLevel** _level_
> 日志级别：NONE、PANIC、FATAL、ERROR、WARN、INFO、DEBUG、TRACE（默认："NONE"）

**-readOnly**
> 以只读模式运行 grv

**-version**
> 打印版本信息

# KEY BINDINGS

**j/k** — 下移/上移
**Enter** — 选择条目 / 打开视图
**q** — 关闭视图 / 退出
**/** — 搜索
**n/N** — 下一个/上一个搜索匹配
**Tab** — 在视图间切换
**1-5** — 跳转到特定视图

# CAVEATS

GRV 已不再积极维护（最后一次发布是 2019 年）。它通过 libgit2 直接读取 git 仓库数据，因此超大仓库可能占用大量内存。只读；不支持提交或推送等写操作。可以考虑 **lazygit** 或 **gitui** 等仍在积极维护的替代品。

# HISTORY

**GRV** 由 **Robert Burke** 创建，用 **Go** 编写。它被设计为图形化 Git 客户端的轻量替代品，为检查仓库历史和差异提供快速的终端工作流。

# INSTALL

```aur: yay -S grv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [tig](/man/tig)(1), [gitui](/man/gitui)(1), [lazygit](/man/lazygit)(1)
