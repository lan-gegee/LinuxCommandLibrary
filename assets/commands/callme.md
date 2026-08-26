# TAGLINE

让 AI 代理和脚本拨打或发短信到你的 iPhone

# TLDR

用 Call Me 应用提供的号码**配对**一次

```callme pair [5551234567]```

**拨打**电话并等待语音回答（转写为文字）

```callme call "[Deploy staging or prod first?]"```

发送**短信**/推送通知

```callme text "[Build green, PR merged.]"```

输出**设置**说明

```callme setup```

显示 App Store 链接的**二维码**

```callme qr```

读取已配对的**号码**

```callme number```

# SYNOPSIS

**callme** {_pair_|_call_|_text_|_listen_|_events_|_setup_|_qr_|_number_|...} [_args_]

# PARAMETERS

**pair** _number_
> 将 iOS 应用中的 10 位 Call Me 号码保存到 `~/.aiphone/config.json`

**call** _message_
> 发起 CallKit 通话；TTS 读出问题；阻塞直到语音回答被转写完成

**text** _message_
> 向手机发送推送通知风格的消息

**listen** / **events**
> 为非插件形式的代理会话获取回复

**setup**
> 输出配对和使用步骤

**qr**
> 输出应用下载链接的可扫描二维码

**number**
> 输出当前已配对的号码

# DESCRIPTION

**callme** 是一个小型的 bash+curl CLI，将终端代理和脚本连接到 **Call Me** iOS 应用（前身为 AI Phone）。配对后，代理可以拨打你的真实 iPhone、通过 TTS 说出问题并收到转写为文本的语音回答，也可以发送异步短信。

凭据保存在 `~/.aiphone/config.json`（权限 0600）中，而不是放在代理指令文件里。还有一个 Claude Code 插件变体，可将同样的流程安装到交互式会话中。

# CAVEATS

需要 Call Me iOS 应用以及能访问 Call Me 服务。通话会一直阻塞直到被接听——没有超时机制不适合无人值守的自动化场景。电话号码属于凭据；不要提交配置文件。

# HISTORY

这是 radres 开发的 **Call Me** iPhone 应用的代理集成方案；独立技能位于开源仓库的 `skill/callme` 目录下。

# SEE ALSO

[curl](/man/curl)(1), [jq](/man/jq)(1)

# RESOURCES

```[Source code](https://github.com/radres/call-me)```

```[Homepage](https://apps.apple.com/app/id6789575165)```

<!-- verified: 2026-07-28 -->
