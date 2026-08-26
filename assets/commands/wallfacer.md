# TAGLINE

面向 AI 编程智能体 CLI 的终端会话管理器

# TLDR

**打开**全屏会话浏览器（TUI）

```wallfacer```

在某个目录中**启动**新会话

```wallfacer new [~/work/api] --title "[Fix flaky auth tests]"```

按标题或 ID 前缀**恢复**会话

```wallfacer resume "[fix flaky auth tests]"```

**搜索**标题、提示词、目录、项目和标签

```wallfacer search [auth]```

以 JSON 格式**列出**某项目的会话

```wallfacer list --project [api] --json```

将会话移入回收站（用 **--purge** 可永久删除）

```wallfacer rm [5f2]```

# SYNOPSIS

**wallfacer**

**wallfacer** **new** [_dir_] [**--agent** _A_] [**--title** _T_] [**--project** _P_] [**--tag** _t_]

**wallfacer** **resume**|**show**|**rm** _ref_ [_options_]

**wallfacer** **list** [**--project** _P_] [**--tag** _T_] [**--agent** _A_] [**--json**]

**wallfacer** **search** _query_

**wallfacer** **rename** _ref_ _title_

**wallfacer** **tag** **add**|**rm** _ref_ _tag_...

**wallfacer** **project** **set**|**clear** _ref_ [_name_]

**wallfacer** **sync**

# DESCRIPTION

**wallfacer** 为来自 **Claude Code**、**Cursor CLI**、**Kiro CLI** 和 **Codex** 的 AI 编程会话建立索引，让你可以命名、打标签、分组、搜索、恢复或删除它们。它对智能体自身的文件是**只读的**：元数据保存在 `~/.local/share/wallfacer/` 下的本地 SQLite 数据库中。

不带子命令直接运行 **wallfacer**（当 stdout 是 TTY 时）会打开全屏浏览器：会话列表、详情面板、模糊过滤，以及用于恢复、重命名、打标签或移入回收站的按键。各子命令则是面向脚本的一次性 CLI；两种入口共享同一索引。每次执行命令前会自动重新扫描磁盘（也可通过 **wallfacer sync** 手动触发）。

`<ref>` 是 ID 前缀或精确标题；有歧义的引用会列出候选而不是猜测。在 wallfacer 之外启动的会话无需导入步骤即可被收录。**rm** 会将条目移入回收站；只有 **--purge** 才会永久删除（包括多文件布局的智能体会话）。

# PARAMETERS

**（无子命令）**
> 打开交互式 TUI 浏览器（若 stdout 不是终端则打印帮助）。

**new** [_dir_]
> 在 _dir_ 中启动会话（默认交互式询问）。支持 **--agent**、**--title**、**--project**、**--tag**。

**resume** _ref_
> 在原工作目录中重新打开会话。

**list**
> 按从新到旧列出会话。过滤器：**--project**、**--tag**、**--agent**（不区分大小写的子串匹配）。脚本场景使用 **--json**。

**search** _query_
> 搜索标题、首条提示词、目录、项目和标签。

**show** _ref_
> 显示单个会话的完整详情。

**rename** _ref_ _title_
> 设置显示标题。

**tag add**|**rm** _ref_ _tag_...
> 添加或移除标签。

**project set**|**clear** _ref_
> 分配或清除项目分组。

**rm** _ref_ [**--purge**] [**-f**]
> 移入回收站，或用 **--purge** 永久删除。

**sync**
> 强制重新扫描磁盘上的智能体会话目录。

# CONFIGURATION

**~/.local/share/wallfacer/**
> SQLite 索引和回收站。删除此目录只会移除 wallfacer 的叠加元数据，不会删除智能体的对话记录。

**WALLFACER_NO_UPDATE_CHECK=1**
> 禁用每日 GitHub 发布提醒（显示在 TUI 页脚/子命令 stderr）。

智能体扫描根目录包括 `~/.claude/projects/`、`~/.cursor/chats/`、`~/.kiro/sessions/cli/` 和 `~/.codex/sessions/`。

# CAVEATS

不会为标题/标签修改智能体自身的会话文件——这些信息只存在于 wallfacer 的数据库中。对话内容的全文搜索已在路线图上（目前只支持标题/提示词搜索）。OpenCode 适配器已列入计划但尚未发布。

# HISTORY

**wallfacer** 是 **pradipta** 开发的 MIT 许可 Go 工具。名字取自刘慈欣《黑暗森林》中的"面壁者"——那些守护着宏大到他人无法理解之计划的人。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1), [tmux](/man/tmux)(1)

# RESOURCES

```[Source code](https://github.com/pradipta/wallfacer)```

```[Documentation](https://github.com/pradipta/wallfacer/blob/main/docs/development.md)```

<!-- verified: 2026-08-06 -->
