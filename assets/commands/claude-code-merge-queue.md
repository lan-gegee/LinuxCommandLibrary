# TAGLINE

面向并行 Claude Code 代理的本地合并队列

# TLDR

将其**安装**为开发依赖并**初始化**项目

```npm install --save-dev claude-code-merge-queue && npx claude-code-merge-queue init```

通过 FIFO 队列将当前 lane **落地**（land）到集成分支

```claude-code-merge-queue land```

在落地后**同步**主检出（若锁文件变化则重装依赖）

```claude-code-merge-queue sync```

在主检出上**预览**某个 lane 的实时工作树

```claude-code-merge-queue preview```

将集成分支**晋升**到生产环境（仅限人工）

```claude-code-merge-queue promote```

运行一个在全机器范围内跨所有 lane 串行化的构建

```claude-code-merge-queue build-lock -- [command]```

# SYNOPSIS

**claude-code-merge-queue** _command_ [_options_]

# DESCRIPTION

**claude-code-merge-queue** 是一个本地零成本的合并队列，适用于多个 Claude Code 代理并行落地工作的仓库。它将 rebase 并 push 的落地操作串行化，在每次落地前运行可配置的检查命令，并协调 worktree "lane"，使各代理不会在共享资源上发生竞争。

与 GitHub 的合并队列不同，它完全在开发者本机运行，不需要 pull request，且适用于任何套餐或托管方案。配置保存在 **claude-code-merge-queue.config.mjs**。**init** 会写入该配置、可选的 **CLAUDE.md** 说明、一个 WorktreeCreate 钩子以及 package 脚本。

pre-push 钩子可以拒绝对集成分支的直接推送，强制代理通过 **land** 操作。紧急绕过使用 **CLAUDE_CODE_MERGE_QUEUE_EMERGENCY_PUSH=1**。

# COMMANDS

**init**

> 检测集成分支和检查命令；写入配置、钩子和脚本。

**land**

> 通过 FIFO 队列将当前 lane rebase 后推送到集成分支。

**sync**

> 将主检出快进到已落地的内容；必要时重装依赖。

**promote**

> 将集成分支发布到生产环境。仅面向人类使用，不面向代理。

**preview** / **preview:restore**

> 将某个 lane 的工作树镜像到主检点上以便检查，无需完整构建。

**port**

> 打印某个 lane 分配到的开发服务器端口。

**prune**

> 移除已落地兄弟 lane 的 worktree。

**build-lock** -- _cmd_

> 在全机器范围的锁下运行 _cmd_，使不同 lane 的构建不会重叠。

**hook worktree-create**

> Claude Code 的 WorktreeCreate 钩子，负责分配带编号的 lane。

# CAVEATS

没有人工审查关卡——只有 **checkCommand** 通过才能落地。锁仅限单台机器。缓慢的检查命令会限制吞吐量，因为 FIFO 锁会在整个检查期间被占用。rebase 冲突会干净地中止；代理必须解决冲突后重新执行 **land**。

# SEE ALSO

[git](/man/git)(1), [npm](/man/npm)(1), [claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/funador/claude-code-merge-queue)```

```[Homepage](https://www.npmjs.com/package/claude-code-merge-queue)```

<!-- verified: 2026-07-30 -->
