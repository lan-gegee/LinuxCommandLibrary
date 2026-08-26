# TAGLINE

从命令行发送 macOS 通知

# TLDR

**发送基本通知**

```terminal-notifier -message "[Task completed]"```

**带标题和副标题发送**

```terminal-notifier -title "[Build]" -subtitle "[Success]" -message "[All tests passed]"```

**带提示音发送**

```terminal-notifier -message "[Done]" -sound default```

**发送并点击后打开 URL**

```terminal-notifier -message "[New issue]" -open "[https://github.com]"```

**发送并点击后激活应用**

```terminal-notifier -message "[Sync complete]" -activate [com.apple.AddressBook]```

**从管道输入发送**

```echo "[Build finished]" | terminal-notifier```

**对通知分组**（替换之前的通知）

```terminal-notifier -group "[build]" -message "[Completed]"```

# SYNOPSIS

**terminal-notifier** [_-title title_] [_-subtitle subtitle_] [_-message message_] [_-sound name_] [_-group id_] [_-activate bundleid_] [_-open url_]

# PARAMETERS

**-message** _text_
> 通知的消息正文（除非使用管道输入，否则必填）

**-title** _text_
> 通知标题（默认为 "Terminal"）

**-subtitle** _text_
> 通知副标题

**-sound** _name_
> 播放 /System/Library/Sounds 中的声音；"default" 为系统默认

**-group** _id_
> 分组标识；同一分组同一时间只显示一条通知

**-activate** _bundleid_
> 点击通知时激活指定的应用

**-open** _url_
> 点击通知时打开 URL

**-remove** _id_
> 移除具有指定分组 ID 的通知

**-list** _id_
> 列出具有指定分组 ID 的通知

# DESCRIPTION

**terminal-notifier** 可以从命令行发送 macOS 用户通知。它让脚本和终端命令能够显示原生系统通知，并自定义内容、声音和点击动作。

通知可以包含标题、副标题、消息正文和声音。点击动作可以打开 URL、激活应用或执行回调。分组标识允许替换先前的通知而不是不断叠加。

该工具适用于在长时间运行的进程（如构建、下载或计划任务）完成时发出提醒。

# CAVEATS

常驻通知（警报样式）需要在系统设置 > 通知 > terminal-notifier 中手动配置。不支持动作按钮；需要此功能请使用 **alerter**。需要 macOS 10.10 或更高版本。

# HISTORY

terminal-notifier 由 **Eloy Durán**（julienXX）创建，是一个把 macOS 通知引入命令行工作流的开源工具。它在将原生通知集成到开发工具链方面广受欢迎。

# INSTALL

```brew: brew install terminal-notifier```

```nix: nix profile install nixpkgs#terminal-notifier```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[notify-send](/man/notify-send)(1)
