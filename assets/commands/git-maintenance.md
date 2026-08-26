# TAGLINE

自动化仓库维护优化

# TLDR

**为当前仓库启动后台维护**

```git maintenance start```

**立即运行所有已启用的维护任务**

```git maintenance run```

**运行特定任务**

```git maintenance run --task=[prefetch]```

**仅在达到计划阈值时运行任务**

```git maintenance run --schedule```

**停止后台维护**

```git maintenance stop```

**注册仓库**以进行后台维护

```git maintenance register```

**取消注册仓库**的后台维护

```git maintenance unregister```

# SYNOPSIS

**git maintenance** _subcommand_ [_options_]

# PARAMETERS

**run**
> 立即运行一个或多个维护任务。

**start**
> 启用后台维护，并通过系统调度器安排每小时运行。

**stop**
> 禁用后台维护计划。

**register**
> 将仓库加入全局维护列表并应用推荐的任务计划。

**unregister**
> 将仓库从全局维护列表中移除。

**is-needed**
> 若需要运行维护任务则退出码为 0，否则为 1。

**--task** _TASK_
> 要运行的特定任务。可重复指定。有效任务：gc、prefetch、commit-graph、loose-objects、incremental-repack、pack-refs、reflog-expire、rerere-gc、worktree-prune。

**--schedule**
> 仅运行已到达计划时间阈值的任务。

**--auto**
> 仅在满足自动阈值时运行任务（例如 gc.auto 的松散对象数量）。

**--quiet**
> 抑制输出到 stderr 的进度信息。

**--scheduler** _SCHEDULER_
> start 使用的后台调度器：auto、crontab、systemd-timer、launchctl、schtasks（默认：auto）。

**--force**
> 与 unregister 一起使用；当仓库未注册时不报错。

**--help**
> 显示帮助信息。

# DESCRIPTION

**git maintenance** 自动管理仓库维护任务。它按需或通过计划的后台作业处理垃圾回收、commit graph 更新、预取（prefetch）和增量重打包。

后台维护无需人工干预即可持续提升仓库性能。`start` 子命令会注册仓库并设置系统调度器（根据平台不同为 crontab、systemd、launchctl 或 schtasks）来周期性运行任务。`register` 子命令配置推荐的任务计划，设置 `maintenance.strategy = incremental` 并禁用前台的自动 gc。

## 任务

- **gc** — 完整垃圾回收；将所有对象重新打包进单个包文件。开销较大。
- **prefetch** — 从所有远程抓取对象到 `refs/prefetch/`，但不更新远程跟踪分支。
- **commit-graph** — 增量更新 commit-graph 文件，加快图遍历速度。
- **loose-objects** — 分批将松散对象打包进包文件（默认每批：50000 个）。
- **incremental-repack** — 使用 multi-pack-index 重打包小型包文件。
- **pack-refs** — 将零散的引用文件合并为单个 packed-refs 文件。
- **reflog-expire** — 删除超过过期阈值的 reflog 条目。
- **rerere-gc** — 清理 rerere 缓存中的过期条目。
- **worktree-prune** — 移除过期或损坏的工作区记录。

# CONFIGURATION

**~/.gitconfig**
> 已注册仓库和计划任务的全局维护配置。

```
[maintenance]
    strategy = incremental
    auto = false
```

# CAVEATS

后台作业依赖可用的系统调度器。对大型仓库而言，`gc` 任务开销大且干扰性强；后台使用建议选择 `loose-objects` 和 `incremental-repack`。配置存储在 git config 中。

# HISTORY

git maintenance 在 **Git 2.29** 中引入，用于提供自动化仓库优化，取代手动调用 gc 的方式。

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

[git-gc](/man/git-gc)(1), [git-commit-graph](/man/git-commit-graph)(1), [git-fetch](/man/git-fetch)(1)
