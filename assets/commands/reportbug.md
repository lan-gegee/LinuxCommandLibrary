# TAGLINE

报告 Debian 软件包中的缺陷

# TLDR

为某个软件包生成**缺陷报告**

```reportbug package```

报告**一般性问题**（非特定软件包）的缺陷

```reportbug other```

将缺陷报告写入**文件**而不是发送邮件

```reportbug -o filename package```

**查询已有缺陷**而不提交报告

```reportbug --query-only [package]```

以指定**严重级别**报告缺陷

```reportbug --severity [serious] [package]```

在缺陷报告中**附加文件**

```reportbug --attach [screenshot.png] [package]```

# SYNOPSIS

**reportbug** [_options_] _package_

# PARAMETERS

**-o**, **--output** _file_
> 将缺陷报告写入文件，而不是通过电子邮件发送。

**--severity** _level_
> 设置缺陷严重级别：critical、grave、serious、important、normal、minor、wishlist。

**--query-only**
> 查询已有缺陷而不提交报告。

**--attach** _file_
> 在缺陷报告中附加文件。

**--include** _file_
> 将文件内容包含在消息正文中。

**--tag** _tag_
> 为报告添加标签。

**--email** _address_
> 设置发件人邮箱地址。

**--smtphost** _host_
> 使用指定的 SMTP 服务器。

**--mode** _mode_
> 操作模式：novice、standard、advanced、expert。

**--template**
> 将模板报告输出到 stdout。

# DESCRIPTION

**reportbug** 是基于 Debian 的发行版的官方缺陷报告工具。它生成包含系统信息的缺陷报告，并通过电子邮件发送到 Debian 缺陷跟踪系统（Debian Bug Tracking System）。

该工具会引导用户提供有关缺陷及受影响软件包的必要信息。

# CAVEATS

发送报告需要配置电子邮箱。基础设施或一般性问题请使用 "other" 作为软件包名。

# HISTORY

属于 **Debian** 质量保障基础设施的一部分。为 Debian 生态提供标准化的缺陷报告流程。

# INSTALL

```aur: yay -S reportbug```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[apt](/man/apt)(8), [dpkg](/man/dpkg)(1)
