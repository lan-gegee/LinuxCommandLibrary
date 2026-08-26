# TAGLINE

Git 管理文件版本。moo 管理机器版本（每个分支/提交对应隔离的 Linux microVM）

# TLDR

为当前分支或 worktree **创建**一台机器

```moo new feat/billing```

在机器内**运行**命令

```moo run feat/billing -- npm run migrate```

把机器状态**快照**并与当前提交绑定

```moo save feat/billing```

**打开**转发到客户机端口的主机 URL

```moo open feat/billing 3000```

**销毁**一台机器

```moo drop feat/billing --force```

**检查**各机器的状态

```moo ls```

# SYNOPSIS

**moo** <verb> <name> [options]

# DESCRIPTION

moo 为每个 git 分支、worktree 或智能体尝试分配一台硬件级隔离的 Linux microVM，其中包含数据库、端口、软件包和服务。机器状态按提交保存，并在 `git checkout` 时恢复，从而让完整的运行时环境实现真正的时间旅行。

它采用写时复制技术，启动迅速，即使有很多台机器也能保持较小的存储占用。目前主要面向 macOS Apple Silicon 主机（计划支持 Linux 主机）。工作树文件会按需同步进客户机（从仓库内执行 `new`/`run`）。

四个核心动词是 new、run、save、drop。辅助管理命令有 `ls`、`open` 和 `doctor`。

# VERBS

**new** <name> [from <src>] [--detached]
> 创建或启动一台机器。若当前提交存在快照则优先使用。`<src>` 可以是 git ref/SHA、快照 ID 或另一台机器的名称。

**run** <name> -- <cmd>...
> 在机器内执行命令（服务在多次运行之间保持存活）。

**save** [<name>]
> 为当前机器状态建立快照，与当前 git 提交关联。

**drop** <name> [--force] [--snapshots]
> 销毁运行中的机器（除非加 `--snapshots`，否则快照保留）。

**ls**
> 列出机器、端口和快照。

**open** <name> [guest-port] [/path]
> 打印（并打开）转发客户机端口所对应的主机 URL。

**doctor**
> 运行主机就绪检查。

# CAVEATS

- 当前支持 Apple Silicon macOS 主机 + Linux（arm64）客户机；1.0 之前为 alpha 阶段（快照格式可能变化）。
- 在 `git checkout` 前先执行 `moo save` 以保存未持久化的运行时工作——`new` 会优先使用 HEAD 对应的快照而不是实时 overlay。
- 每台机器的网络完全隔离；需要主机可达时使用 `moo open` 或 `moo.toml` 中的 `[network] ports`。
- 基础镜像直接来自 OCI registry，无需 Docker 守护进程；不需要 Docker。

# INSTALL

```aur: yay -S moo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [docker](/man/docker)(1)

# RESOURCES

```[Source code](https://github.com/heyito/moo)```

```[Documentation](https://github.com/heyito/moo#readme)```

<!-- verified: 2026-07-11 -->
