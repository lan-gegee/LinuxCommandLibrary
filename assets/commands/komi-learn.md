# TAGLINE

面向编程智能体的持续记忆与自我改进层

# TLDR

为 Claude Code **安装** komi-learn 钩子

```komi-learn install```

改为为 Codex **安装**而非 Claude Code

```komi-learn install --host codex```

**运行健康检查**并暴露问题

```komi-learn doctor```

**显示**当前配置与学习进度

```komi-learn status```

**更新** komi-learn 及其智能体钩子

```komi-learn update```

**预览**更新而不应用

```komi-learn update --check```

**编辑**某个配置值

```komi-learn config set [key] [value]```

**同步**社区池经验

```komi-learn sync```

在共享前**审查**待处理的贡献

```komi-learn queue```

**遗忘**先前学到的条目（默认归档）

```komi-learn forget [topic]```

改为**永久删除**所学条目而不归档

```komi-learn forget [topic] --hard```

**卸载**钩子（用 `--purge` 可同时删除存储的数据）

```komi-learn uninstall```

# SYNOPSIS

**komi-learn** _subcommand_ [_options_]

# DESCRIPTION

**komi-learn** 是一个 Python CLI，为 **Claude Code** 和 **Codex** 等编程智能体添加记忆与自我改进循环。它安装针对各智能体的钩子，观察会话并将持久性经验保存下来供后续运行使用。

学习循环分为四个阶段。**Recall** 在会话开始时激活相关经验。**Distill** 在会话结束后分析会话记录并提取持久性经验。**Curate** 合并重复条目并归档过时内容。**Share** 可选择将用户批准的经验发布到 GitHub 托管、经加密签名的社区池中，供其他用户通过 `komi-learn sync` 拉取。

机密信息、绝对路径和一次性失败会在内容存储或共享之前被过滤。`forget` 默认归档所学内容，只有加 `--hard` 才会删除。`uninstall` 移除钩子；`--purge` 还会删除已存储的学习内容。

# PARAMETERS

**install**
> 安装智能体钩子。`--yes` 接受默认值。`--host` 选择智能体（`claude`、`codex`）。

**doctor**
> 验证安装并报告问题。

**update**
> 升级 komi-learn 及其钩子。`--check` 仅预览。

**status**
> 显示配置和学习进度。

**config**
> 以交互方式或通过 `config set <key> <value>` 调整设置。

**sync**
> 拉取社区池经验。

**queue**
> 审查待处理的共享贡献。

**forget** _topic_
> 归档一条所学内容。`--hard` 将其永久删除。

**uninstall**
> 移除钩子。`--purge` 删除所有存储的数据。

# INSTALLATION

```pip install komi-learn```

然后为目标智能体安装钩子：

```komi-learn install```

# CAVEATS

komi-learn 会在 `install` 期间修改宿主智能体的配置。升级后请运行 `komi-learn doctor` 确认钩子仍然有效。社区池是可选加入的，但请注意你排队分享的经验可能包含会话中的代码或命令片段；同步前请先审查队列。

# SEE ALSO

[claude](/man/claude), [aislop](/man/aislop)
