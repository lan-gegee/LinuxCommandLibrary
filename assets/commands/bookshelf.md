# TAGLINE

面向编码智能体会话的终端书库与氛围语录

# TLDR

**打开**交互式终端书库

```bookshelf```

按需**显示一条语录**

```bookshelf quote```

**显示与某种意图相关的语录**（如重构）

```bookshelf quote --intent [refactor]```

**启用氛围语录**：每 N 个完成的智能体回合触发一次

```bookshelf ambient enable --cadence [5] --intent [refactor]```

**查看氛围模式**状态

```bookshelf ambient status```

**禁用氛围**模式

```bookshelf ambient disable```

对最近一条语录**发送反馈**

```bookshelf feedback [up|down]```

# SYNOPSIS

**bookshelf** [_subcommand_] [_options_]

# PARAMETERS

_（无子命令）_
> 打开交互式 TUI 书库（浏览书籍、搜索、收藏、阅读清单）。

**quote**
> 打印一条按需语录。**--intent** _theme_ 映射到本地标签（如 refactor、debug）用于相关性排序。

**ambient** **enable** | **disable** | **status**
> 控制编码智能体 Stop 钩子的氛围推送。**enable --cadence** _N_ 设置每多少个完成的回合之间推送一条语录。**enable --intent** _theme_ 存储氛围主题。

**feedback** **up** | **down**
> 记录对最近一条已推送语录的本地反馈。

# DESCRIPTION

**bookshelf** 是一个本地优先的 Python CLI，它在编码智能体工作流（Codex、Claude Code 及相关宿主）中呈现书籍语录，并提供完整的终端书库供浏览。氛围模式是可选的，默认关闭：通过宿主插件/钩子启用后，每隔几个完成的回合可以出现一条简短语录。语录和相关性排序全部在本地完成——选择过程不涉及任何提示词、代码、对话记录或网络调用。

交互式 **bookshelf** TUI 支持导航（**j**/**k**、方向键）、类型标签页、搜索（**/**）、阅读清单（**c**）、随机选书（**r**）、收藏（**f**）、已读/想读标记（**m**/**w**）、帮助（**?**）和退出（**q**）。收藏、清单、统计和氛围设置保存在平台应用数据目录下名为 **bookshelf** 的目录中（或由 **BOOKSHELF_DATA_HOME** 指定）。

可通过 **pipx** 从 GitHub 仓库安装（需要 **Python 3.10+**，无运行时依赖）。宿主集成以 Codex/Claude Code 插件及其他智能体市场的形式提供；这些钩子无需全局 **bookshelf** 二进制即可推送氛围语录。PyPI 上的包名计划为 **ambient-bookshelf**。

# CONFIGURATION

**BOOKSHELF_AMBIENT_ENABLED**
> 为当前进程覆盖氛围模式的开关状态（**1**/**0** 或 **true**/**false**）。优先于已保存的配置。

**BOOKSHELF_AMBIENT_CADENCE**
> 正整数：相邻两条氛围语录之间间隔的已完成回合数。

**BOOKSHELF_DATA_HOME**
> 将配置和氛围状态重定向到其他目录。

# CAVEATS

氛围推送依赖宿主的插件/钩子支持，在没有可用的安全有界语录时会静默关闭。氛围语料的长度受限（约 **220** 个 UTF-8 字节 / **32** 个单词）；按需 **quote** 则允许更宽的显示预算。目录条目的验证程度不一——参见项目的 **DATA.md**。基于意图的排序是确定性的标签映射，并非深度语义相关性的保证。

# HISTORY

由 **Amal David** 创建，是一个 MIT 许可的 Python 项目，将终端书库与面向 AI 编码智能体的可选氛围语录结合在一起。通过插件和钩子与 Codex、Claude Code 及类似宿主集成。

# SEE ALSO

[claude](/man/claude)(1), [codex](/man/codex)(1)

# RESOURCES

```[Source code](https://github.com/Amal-David/bookshelf)```

```[Homepage](https://bookshelf-8dz.pages.dev/)```

```[Documentation](https://github.com/Amal-David/bookshelf#readme)```

<!-- verified: 2026-07-24 -->
