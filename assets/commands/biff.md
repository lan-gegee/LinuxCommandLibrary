# TAGLINE

在终端切换邮件到达通知

# TLDR

为当前终端会话**启用邮件通知**

```biff y```

为当前终端会话**禁用邮件通知**

```biff n```

**显示当前通知状态**

```biff```

# SYNOPSIS

**biff** [**y** | **n**]

# DESCRIPTION

**biff** 是一个邮件通知工具，当你的终端会话期间有新邮件到达时在命令行上提醒你。启用后，它会显示来信的发件人、主题和前几行内容，并伴随一声终端蜂鸣。

通知通过 **comsat**(8) 服务异步实现。如果系统中 comsat 未启用，biff 将不起作用。若需要同步通知，请改用 **sh**(1) 中的 **MAIL** 变量或 **csh**(1) 中的 **mail** 变量。

常见做法是在 **~/.login** 或 **~/.profile** 中加入 **biff y**，以便每次登录时启用通知。

# PARAMETERS

**y**
> 为当前终端启用邮件通知

**n**
> 为当前终端禁用邮件通知

如果不带参数，biff 会显示当前的通知状态。

# CAVEATS

**biff** 命令要求系统正在运行 **comsat**(8) 守护进程。没有它，邮件通知将无法工作。

使用 **su**(1) 可能导致 biff 出现权限问题，因为终端所有权仍属于原始用户，从而在更改通知状态时出现 "Permission denied" 错误。

# HISTORY

该命令出现于 **4.0BSD**（1980 年发布），由加州大学伯克利分校的 **John Foderaro** 编写。它以同为伯克利学生的 Heidi Stettner 所养的狗 **Biff** 命名。"Biff 会冲邮递员吠叫"这一广为流传的说法被 Stettner 本人否认，但这个名字作为邮件通知工具的名称沿用至今，颇为贴切。

在现代系统中，通知守护进程是 **GNU inetutils** 的一部分（即 in.comsat），而 biff 客户端在 Debian 和 Ubuntu 上通常随专门的 **biff** 软件包发布。

# INSTALL

```apt: sudo apt install biff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mail](/man/mail)(1), [sh](/man/sh)(1), [csh](/man/csh)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/inetutils/)```

<!-- verified: 2026-06-19 -->
