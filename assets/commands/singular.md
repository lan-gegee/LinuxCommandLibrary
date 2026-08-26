# TAGLINE

面向软件仓库的自主多智能体编排引擎

# TLDR

从检出目录**安装**引擎（创建 `~/.singular/bin/singular`）

```bash install.sh```

**准备**当前 Git 仓库（pin、脚手架、迁移、doctor、可选测试；绝不实际执行）

```singular setup```

**检查**解释器、引擎 pin 和仓库配置

```singular doctor```

**运行**一轮 reconcile 周期（import、recover、integrate、dispatch、snapshot）

```singular reconcile --actuate```

驱动单个任务走完 planner、worker 和 audit

```singular drive [TASK-0001]```

启动自动驾驶循环（墙钟预算为 `SINGULAR_MAX_HOURS`）

```singular auto```

打印编排状态

```singular status```

写入 STOP 使 worker 不再被派发

```singular stop```

# SYNOPSIS

**singular** _command_ [_args_]

# PARAMETERS

**setup** [**--json**] [**--no-test**] [**--test-async**]
> 从普通 Git 仓库到经过验证的 STOPPED 消费者的一条幂等路径。解析引擎 pin，必要时安装匹配的本地检出，先写入 `.singular-state/STOP`，然后搭脚手架、迁移、运行 doctor，并可选地记录一次回归运行。绝不实际执行。

**init**
> 在当前仓库中生成 `singular.config.json`、`docs/orchestration/` 和 `.singular-version` 脚手架。

**doctor** [**--json**] [**--repair-model-cache**]
> 结构化预检。JSON 检查项具有稳定的 `id`、`severity`、`requiredFor` 和 `remediation`。

**reconcile** [**--dry-run** | **--apply** | **--actuate** | **--status** | **--drain**]
> L0 协调器：导入暂存的 planner 任务、恢复过期的租约、整合已完成的分支、派发前沿 worker、做快照。**--actuate** 执行整个周期。**--drain** 等待分离运行的 worker。

**auto** [**--once**]
> 自主驾驶循环。遵循 `SINGULAR_MAX_HOURS`（默认 12）。

**drive** _TASK-XXXX_
> 让一个任务依次通过 L1 规划、L2 worker、门禁和审计。

**status**
> 编排状态（与 `reconcile --status` 相同）。

**integrate** [**--task** _TASK-XXXX_] [**--dry-run**]
> 将已接受的 worker 分支合并到目标分支。

**stop** [**--wait**[=_S_]] / **resume** / **wake** [**--keep-stop**]
> 协作式暂停、重启和退避/小睡重置。

**human-gate** **request** | **approve** | **status**
> 与所有者和制品哈希绑定的人工审批记录（首选 schema v2 路径）。

**gate validate** _FILE_
> 报告门禁结果文件中的每一处契约违规。

**test** [**--status** [**--json**] | **--wait** | **--no-wait** | **--new-run** | **--rerun-failures**]
> 受监督的引擎回归测试套件。需要引擎**检出**（安装在 `~/.singular/versions/` 下的副本不附带测试）。证据落在当前仓库的 `.singular-state/test-runs/` 下。

**update** [_VERSION_]
> 将本仓库 pin 到 `.singular-version`。不带参数时，pin 到机器上的 `current` 版本。

**migrate** [**--dry-run**]
> 通过引擎的 `migrations/` 链提升 `singular.config.json` 中的 `schemaVersion`。

**version**
> 打印 CLI 版本和解析出的引擎主目录。

**console** [**--ensure** | **--status** | **--stop**]
> 本地可视化服务器（默认 `http://127.0.0.1:8765`）。URL 持久保存在 `.singular-state/console.url`。

**metrics** [**--json**] [**--runs-dir** _DIR_] [**--events-file** _FILE_]
> 从事件日志读取只读的上下文指标。

**gc** [**--dry-run**]
> 限制运行历史长度、清理已整合的 worktree、轮转事件日志。

**help**
> 打印启动器用法。只有设置 `SINGULAR_CTX_GRAPH=1` 或 `SINGULAR_CTX_EXPERIMENT=1` 时才会出现 `graph` 和 `experiment-report`。

其他运维命令还包括 **recover**、**validate-dag**、**next-area**、**promote-gate**、**health**、**gates**、**lease**、**plan**、**ask**、**report**、**supersede**、**unpark**、**breaker**、**clear-backoff** 和 **accept-packet**。

# DESCRIPTION

**singular** 是 Singular 的命令行启动器。Singular 是一个 bash 和 Python 编排引擎，可在 Git 仓库上并行运行自主 AI 编程智能体。你在命令行输入的二进制是 **singular**；上游检出名为 **singular-lite**。它与 Singularity/Apptainer 容器无关。

引擎在每台机器上安装一次（从检出目录执行 `bash install.sh`），装入 `SINGULAR_HOME`（默认 `~/.singular`）：包含 `versions/<ver>/` 下的版本树、`current` 符号链接以及 `bin/singular`。每个消费者仓库通过 `.singular-version` pin 引擎版本（覆盖 `singular.config.json` 中的 `engineVersion`）。启动器解析该 pin，将 `SINGULAR_ROOT` 绑定到仓库，并执行匹配的引擎脚本。

调度分三层。**L0** 是唯一的源头循环（`reconcile`）：导入 planner 提案、恢复过期租约、整合完成的分支、派发工作、快照。**L1** planner 为每个 DAG 区域产生一批任务。**L2** worker 在隔离的 `git worktree` 中的按任务分支上运行单个任务并写出状态包。配置好的 **gate** 命令（例如测试套件）在 worker 之后运行；审计模型审查状态包；决策器根据 `(failure-class, retries-left)` 映射出重试、修改范围、上报或搁置。

默认启用分离派发（`SINGULAR_DETACHED_DISPATCH=1`）：`reconcile` 预租前沿任务，在独立会话中生成 worker，并在几秒内返回。收割进程会在后续周期归因完成情况。将该变量设为 `0` 可回到旧的同步批量等待模式。

前提条件：**Bash >= 4**、**python3**、**git**，以及 `PATH` 上至少一个已配置的 runner CLI（`claude`、`codex` 或配置中指定的其他 runner）。macOS 的系统 `/bin/bash` 是 3.2，请安装较新的 bash，并可选地将 `SINGULAR_BASH_BIN` 设置为其绝对路径。启动器以 **GPL-3.0** 许可发布。

# CONFIGURATION

**singular.config.json**
> 每仓库声明式配置：`targetBranch`、`gateCommand`、`runner`、`areas`、`promoter`、`worktreeCopyPaths`、`modules`、能力/角色档案、证据限制、bootstrap 命令和 `legacyCompatibility`。起始模板的 `gateCommand` 为 `false`，因此在设置真实的健康检查之前，新仓库会以失败关闭的方式运作。

**singular.config.sh**
> 可选的 shell 扩展（计算值、函数）。

**.singular-state/config.local.sh**
> 被 gitignore 的运维覆盖项和机密。

**.singular-version**
> 本仓库的权威引擎 pin。

**SINGULAR_HOME**
> 机器级安装根目录（默认 `~/.singular`）。必须是绝对路径。

**SINGULAR_ENGINE_HOME**
> 覆盖解析出的引擎树（对检出运行 `singular test` 时必需）。

**SINGULAR_BASH_BIN** / **SINGULAR_CODEX_BIN**
> Bash >= 4 及特定 Codex 二进制的绝对路径。`SINGULAR_BASH_BIN` 仅用于 bootstrap，在 `singular.config.json` 内部会被忽略。

**SINGULAR_MAX_CONCURRENT**（默认 3）/ **SINGULAR_MAX_DISPATCH**（默认 5）/ **SINGULAR_MAX_HOURS**（默认 12）
> worker 槽位、每轮 reconcile 周期的任务数以及自主运行的墙钟预算。

**SINGULAR_DETACHED_DISPATCH**（默认 1）/ **SINGULAR_AUTO_INTEGRATE**（默认 1）/ **SINGULAR_PUSH**
> 分离 worker、自动合并已接受分支，以及是否推送。直接命令默认 `SINGULAR_PUSH=0`；`singular auto` 默认为 `1`。

**SINGULAR_TARGET_BRANCH**
> 整合分支。执行 actuate 周期时必需（也可在 JSON 中设置）。

**SINGULAR_CTX_GRAPH** / **SINGULAR_CTX_EXPERIMENT**
> 选择性开启的标志，用于暴露 `singular graph` 和 `singular experiment-report`。

# CAVEATS

不是 **singularity**(1)（容器）。macOS 用户必须安装 Bash >= 4，否则启动器会以 `SINGULAR_BASH_UNSUPPORTED` 退出。`singular test` 拒绝已安装（非检出）的引擎树。`setup` 只会从机器上已有的匹配引擎检出来安装缺失的 pin——没有下载步骤。默认 promoter 只认识其内置的节点注册表；省略 `promoter` 的自定义 DAG 会在第 0 层之后卡住并报 `promotion: no promotable frontier gates`。Singular 会执行仓库配置的 shell 命令并在 worktree 中启动编程智能体——在不受信任的仓库中运行前请先检查配置和任务文件。Schema v2 会拒绝未绑定的 `accept-waiver` / `promote-gate --operator` 路径，除非 `legacyCompatibility.unboundWaivers` 为 `true`。

# HISTORY

Singular 由 **alex-reysa** 在 **singular-lite** 仓库中开发（GPL-3.0）。机器级启动器是一个 Bash 脚本（`cli/singular`），负责解析 pin 的引擎版本并执行 `engine/*.sh`。引擎版本由仓库的 `VERSION` 文件标识（编写文档时为 0.19.x 系列）；内嵌的 CLI 版本字符串与之独立。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [aider](/man/aider)(1), [git](/man/git)(1), [git-worktree](/man/git-worktree)(1)

# RESOURCES

```[Source code](https://github.com/alex-reysa/singular-lite)```

<!-- verified: 2026-08-18 -->
