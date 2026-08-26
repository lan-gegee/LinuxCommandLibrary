# TAGLINE

将命令输出和文件通过管道发送到 Slack 频道

# TLDR

**运行首次 OAuth 设置**

```slackcat --configure```

**向频道发送一次性消息**

```slackcat -c [channel] -m "[hello]"```

**将 stdin 通过管道**作为 snippet 发送到 Slack

```[command] | slackcat -c [channel]```

**上传文件**

```slackcat -c [channel] [file.txt]```

**覆盖上传的文件名 / 文件类型**

```slackcat -c [channel] -n [log.py] --filetype [python] [file.py]```

**同时打印到 stdout**（tee 模式）

```[command] | slackcat -c [channel] --tee```

**将 tail 输出流式传输**到 Slack

```tail -f [/var/log/app.log] | slackcat -c [channel] --stream```

**试运行**（不真正发布）

```[command] | slackcat -c [channel] --noop```

**使用配置文件中的其他 profile**

```slackcat -p [profile] -c [channel] [file]```

# SYNOPSIS

**slackcat** [_-c channel_] [_-m message_] [_options_] [_file_]

# PARAMETERS

**-c**, **--channel** _CHANNEL_
> 目标频道（公开/私密）或群组。除非已在配置中设置，否则必需。

**-m**, **--message** _TEXT_
> 将 _TEXT_ 作为消息发布（不读取 stdin 或文件）。

**-n**, **--filename** _NAME_
> 上传 snippet 时覆盖在 Slack 中显示的文件名。

**--filetype** _TYPE_
> 用于语法高亮的显式 Slack 文件类型（`python`、`shell`、`javascript` 等）。管道输入 stdin 时很有用。

**--comment** _TEXT_
> 附加到 snippet 上传的初始评论。

**-p**, **--profile** _NAME_
> 使用 slackcat 配置文件中的指定 profile。

**--tee**
> 将输入同时复制到 stdout 和 Slack。

**--stream**
> 将输入视为实时流；新数据到达时持续发布更新，而不是缓冲成单个 snippet。

**--noop**
> 不实际上传；打印将要发送的内容。

**--configure**
> 运行交互式 OAuth 配置，以创建/更新 slackcat 配置。

**-h**, **--help**
> 显示帮助。

**-v**, **--version**
> 显示版本。

# CONFIGURATION

**~/.slackcat**
> INI 风格的配置，包含 `[default]` 和命名 profile 区段。可用的键包括 `token`、`team`、`default_channel`。

Slack token 必须具有 `files:write`、`chat:write` 及相关 scope。`slackcat --configure` 会引导完成设置这些权限的 OAuth 流程。

# CAVEATS

需要 Slack 应用/用户 token。Slack 对上传和聊天消息有速率限制（因套餐级别而异）。非常大的文件或高频流可能触及每条消息 1 MB 的 snippet 限制——出现这种情况时 `--stream` 会轮换到新的 snippet。

# HISTORY

**slackcat** 由 **Bradley Cicenas**（`bcicen`）创建，采用 **Go** 编写。源码：github.com/bcicen/slackcat。

# INSTALL

```brew: brew install slackcat```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[curl](/man/curl)(1), [tee](/man/tee)(1), [jq](/man/jq)(1)
