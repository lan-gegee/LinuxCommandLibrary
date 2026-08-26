# TAGLINE

通过 git 分支共享 Claude Code 会话

# TLDR

**将本地会话发布**到共享分支

```ccgs push```

**只推送指定会话**（按 id 或名称）

```ccgs push [session_id]```

**拉取共享会话**到本地项目

```ccgs pull```

**无需安装直接运行**（通过 npx）

```npx claude-git-sessions pull```

**按名称删除共享会话**且不提示确认

```ccgs delete [name] --yes```

**与团队共享记忆事实**

```ccgs memory push```

# SYNOPSIS

**ccgs** _command_ [_targets ..._] [_options_]

# DESCRIPTION

**ccgs**（claude-git-sessions）通过将 **Claude Code** 会话记录存储在现有仓库内的**孤儿 git 分支**（名为 @ccgs/<name>）上，实现团队间的会话共享，无需服务器或额外基础设施。会话以其 Claude Code 会话 UUID 为键，因此不同作者不会冲突。

该工具针对临时索引使用底层 git 管道命令（**hash-object**、**write-tree**、**commit-tree**、**push**），因此绝不会触碰工作树或当前分支，即使仓库处于脏状态也能正常工作。在 **pull** 时，每份会话记录的 cwd 字段会被重写，以便 **claude --resume** 能从仓库根目录正常恢复。同一机制也用于存储共享的记忆事实。

# COMMANDS

**pull** [**--force**] [**--exclude-memory**]
> 从分支获取会话（默认还包括共享记忆）到本地项目。--force 会覆盖本地较新的会话。

**push** [_targets ..._] [**--exclude-memory**]
> 将本地会话发布到分支。可以指定具体会话；不给目标则推送全部。首次推送时会创建孤儿分支。

**delete** _id|name_ [**--yes**] [**--local**]
> 按 UUID、UUID 前缀（4 个以上字符）或唯一名称删除会话。除非给出 --yes 否则会提示确认；除非给出 --local，否则只影响共享分支。

**memory push** [**--all**]
> 发布记忆事实；默认共享项目事实和参考事实，--all 还包括用户事实和反馈事实。

**memory pull** [**--all**] [**--force**]
> 获取共享记忆事实并将其合并到本地记忆目录。

# OPTIONS

**-b**, **--branch** _name_
> 选择会话集 / 分支后缀（默认：default）。

**--remote** _remote_
> 要使用的 Git 远程（默认：origin）。

**-v**, **--version**
> 打印版本。

**-h**, **--help**
> 显示帮助。

# CAVEAT

需要 **Node 20+** 和 **git 2.5+**。会话存放在一个与主分支没有任何共同历史的分支上；推送会将会话记录内容发布到远程，因此请像对待任何共享的对话数据存储一样对待该远程。

# HISTORY

**ccgs** 是一款开源工具，由 **Ingram Technologies** 用 **TypeScript** 编写，以 **claude-git-sessions** 之名发布于 npm，采用 **MIT** 许可证。

# SEE ALSO

[claude](/man/claude)(1), [git](/man/git)(1), [npx](/man/npx)(1), [npm](/man/npm)(1)
