# TAGLINE

Rspamd 垃圾邮件过滤客户端

# TLDR

训练为**垃圾邮件**

```rspamc learn_spam path/to/email```

训练为 **ham**（非垃圾邮件）

```rspamc learn_ham path/to/email```

为邮件生成**分析报告**

```rspamc symbols path/to/email```

显示服务器**统计信息**

```rspamc stat```

**扫描**一封邮件

```rspamc < path/to/email```

检查**模糊哈希**

```rspamc fuzzy_check path/to/email```

# SYNOPSIS

**rspamc** [_options_] [_command_] [_arguments_]

# DESCRIPTION

**rspamc** 是 rspamd 垃圾邮件过滤系统的命令行客户端。它可以训练贝叶斯过滤器、扫描电子邮件以及查询服务器统计信息。

# PARAMETERS

**learn_spam FILE**
> 训练过滤器把该邮件识别为垃圾邮件

**learn_ham FILE**
> 训练过滤器把该邮件识别为正常邮件

**symbols FILE**
> 生成详细的垃圾邮件分析报告

**stat**
> 显示服务器统计信息

**fuzzy_add FILE**
> 将邮件添加到模糊哈希存储

**fuzzy_check FILE**
> 检查邮件是否匹配模糊哈希

**fuzzy_del FILE**
> 将邮件从模糊哈希存储中移除

**-h, --host HOST**
> 连接到指定的 rspamd 主机

**-p, --port PORT**
> 通过指定端口连接

**-P, --pass PASSWORD**
> 使用密码进行身份验证

**-j, --json**
> 以 JSON 格式输出结果

# CAVEATS

需要有正在运行的 rspamd 服务器。样本越多，训练效果越好。模糊哈希用于匹配相似的垃圾邮件模式。

# HISTORY

**rspamc** 属于 **rspamd**，一个专为高流量邮件服务器设计的快速、免费、开源的垃圾邮件过滤系统。

# INSTALL

```apt: sudo apt install rspamd```

```pacman: sudo pacman -S rspamd```

```apk: sudo apk add rspamd-client```

```zypper: sudo zypper install rspamd```

```nix: nix profile install nixpkgs#rspamd```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rspamd](/man/rspamd)(8), [rspamadm](/man/rspamadm)(1)
