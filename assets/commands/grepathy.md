# TAGLINE

将 AI 编码智能体的决策提炼为可提交的 why 文件

# TLDR

在仓库中**初始化**钩子和 `.ai/why`

```grepathy init```

**查看状态**：提炼情况与健康状态

```grepathy status```

**运行健康检查**（doctor）

```grepathy doctor```

**显示 why 条目**中适用于某个路径的内容

```grepathy context [path]```

立即**提炼并提交** why 笔记（绝不推送）

```grepathy sync```

临时**禁用** grepathy 钩子

```grepathy off```

重新**启用** grepathy 钩子

```grepathy on```

从项目中**移除** grepathy

```grepathy uninstall```

# SYNOPSIS

**grepathy** _command_ [_options_]

# DESCRIPTION

**grepathy** 记录智能体所写代码背后的 *why*，让人类和未来的智能体无需翻查聊天记录即可审阅这些决策。它会在**本地**读取编码智能体的会话记录，提取其中的决策，并在 **.ai/why/** 下写入一个按分支组织的 markdown 文件供你随代码一起提交。

它设计为通过 git/Claude Code 钩子运行，而非任务进行中的智能体日志记录：在某个分支的工作结束后，grepathy 提炼出一份 why 包，展示给人类审阅，并尊重对条目的永久编辑或删除。它不会阻止推送、不会暂存无关文件，也绝不会替你执行推送。项目智能体文档中的一个指针加上一个编辑前钩子，可以在智能体触及匹配路径时注入相关的 why 条目。

以隐私为先：会话记录留在本机；只有脱敏后的 markdown 摘要才会进入仓库。摘要避免引用用户消息、清除密钥，并在你审阅之前先经过确定性的扫描器检查。

目前撰写 why 文件针对的是 Claude Code 的会话数据；任何人都可以读取已提交的 markdown。安装和使用需要 Node.js 20+，可通过 **npx grepathy** 或本地构建使用。

# PARAMETERS

**init**
> 安装钩子和目录。可安全重复运行。可能会提议回填已有的会话。

**status**
> 报告提炼状态以及哪些内容看起来已过期。

**doctor**
> 对安装和配置进行健康检查。

**context** _path_
> 打印适用于给定文件或路径的 why 包条目。

**sync**
> 立即提炼并提交 why 内容（同样绝不推送）。

**distill**
> 仅运行提炼而不走完整的 sync 流程（见 **--help**）。

**repair**
> 修复 grepathy 状态或钩子。

**off** / **on**
> 临时禁用或重新启用钩子。

**uninstall**
> 从仓库中移除 grepathy 集成。

# CAVEATS

它无法阻止智能体重构掉重要代码；只能捕获源码中不可见的推理过程。写入端目前仅面向 Claude Code。why 文件的质量取决于摘要器和你在提交前的审阅。本地会话记录一旦被智能体删除，空缺或过期的内容便无法恢复。

# SEE ALSO

[git](/man/git)(1), [claude](/man/claude)(1)

# RESOURCES

```[Source code](https://github.com/evansjp/grepathy)```

<!-- verified: 2026-07-15 -->
