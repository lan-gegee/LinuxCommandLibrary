# TAGLINE

跨机器执行命令、传输文件并控制智能体的局域网守护进程

# TLDR

**初始化**配置并生成 API 密钥

```loopsy init```

**启动**守护进程

```loopsy start```

**停止**守护进程

```loopsy stop```

**显示**守护进程状态

```loopsy status```

与局域网内的另一台机器**发起配对**（会显示 6 位数字码）

```loopsy pair```

在已知地址处与对端**完成配对**

```loopsy pair [192.168.1.50]```

**列出**已配对的手机

```loopsy phone list```

以自定义 TTL **签发手机配对令牌**

```loopsy mobile pair --ttl [seconds]```

**跟踪**审计日志

```loopsy logs -f```

**运行守护进程健康检查**

```loopsy doctor```

# SYNOPSIS

**loopsy** _command_ [_subcommand_] [_options_]

# DESCRIPTION

**loopsy** 是一个小型守护进程和 CLI，通过 **mDNS** 发现本地网络中的其他 Loopsy 守护进程，让用户完成一次性配对，随后在机器之间提供一组精简的能力：执行命令、建立长期存活的 PTY 会话、传输文件、浏览对端文件系统、共享键值状态，以及交换带已读回执的符合协议的消息。

这些能力还通过 **MCP** 暴露给 AI 编程智能体（Claude Code、Codex CLI、Gemini CLI、Opencode 等），因此运行在一台机器上的智能体可以直接操控另一台已配对的机器。

配对使用 **ECDH (P-256)** 和一个由两名用户肉眼比对的 6 位短认证串，类似于 **Signal** 的安全号码，用于防范局域网内的中间人攻击。

# COMMANDS

**init**
> 生成本地配置和 API 密钥。

**start** / **stop** / **status**
> 本地守护进程的生命周期控制。

**enable** / **disable**
> 安装或移除自启动单元（launchd、systemd 或任务计划程序）。

**doctor**
> 对配置、守护进程、MCP 集成及对端进行健康检查。

**logs** [**-f**]
> 打印审计日志；**-f** 表示跟随新条目。

**key show** / **key generate**
> 显示或轮换本地 API 密钥。

**pair** [_address_]
> 不带地址时，在本机发起配对并打印 6 位验证码。带地址时，向指定的对端完成配对。

**peers add** _address_
> 不经 mDNS 发现，手动注册对端。

**phone list**
> 列出本设备已配对的手机。

**phone revoke** _id_
> 在服务端吊销一台已配对的手机。

**mobile pair** [**--ttl** _seconds_]
> 为手机签发配对令牌，打印二维码和 4 位验证码。

**relay configure** _url_
> 将守护进程指向另一个中继服务器（用于跨网络场景）。

# OPTIONS

**--ttl** _seconds_
> 所签发配对令牌的有效期。

**--lan**
> 将守护进程暴露到本地网络（非默认行为）。

**-f**
> 跟随日志输出（配合 **logs** 使用）。

# CONFIGURATION

守护进程将配置和 API 密钥存储在用户的配置目录下（由 **loopsy init** 创建）。**loopsy enable** 安装的自启动单元采用平台原生机制：macOS 上为 **launchd**，Linux 上为 **systemd --user**，Windows 上为**任务计划程序**。

# CAVEATS

确认配对前务必在**两台**机器上比对 6 位数字码——正是这个短认证串在保护你免受局域网内主动攻击者的威胁。使用 **--lan** 将守护进程暴露出去会扩大其攻击面；请只在可信网络中使用。用 **loopsy key generate** 轮换 API 密钥会使现有的智能体集成失效。

# HISTORY

**loopsy** 由 **leox255** 开发，是一个连接机器与 AI 编程智能体的开源局域网桥接工具，通过 **npm** 分发。其配对交互设计借鉴了 **Signal** 与 **Magic Wormhole**。

# SEE ALSO

[ssh](/man/ssh)(1), [mosh](/man/mosh)(1)
