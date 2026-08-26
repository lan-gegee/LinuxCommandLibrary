# TAGLINE

抑制 cron 任务输出的工具

# TLDR

**运行命令**且仅在出错时显示输出

```cronic [command] [args...]```

**静默运行 cron 任务**，失败时才报告

```cronic /path/to/script.sh```

# SYNOPSIS

**cronic** _command_ [_args..._]

# DESCRIPTION

**cronic** 是一个用于 cron 任务的 shell 脚本包装器，除非命令执行失败，否则会抑制输出。没有 cronic 时，每个产生输出的 cron 任务都会触发一封发给用户的电子邮件，导致例行成功执行的邮件充斥收件箱。

cronic 会同时捕获 stdout 和 stderr 以及退出码。如果命令成功（返回零），所有输出都会被丢弃。如果命令失败（返回非零），cronic 会显示捕获到的输出，让 cron 能够发送失败通知邮件。这种方式减少了成功任务的邮件噪音，同时确保管理员能及时得知真正的故障。

# CAVEATS

cronic 是 Chuck Houpt 编写的一个独立小 shell 脚本，不属于 moreutils 软件包；功能类似的 **chronic** 命令是 moreutils 中的对应实现。两者行为有所不同：cronic 还会把任何输出到 stderr 的内容视为失败（即使退出状态为零），因此在标记问题上更为严格。输出会被缓冲，这对运行时间极长且输出量很大的命令可能造成问题。

# INSTALL

```zypper: sudo zypper install cronic```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chronic](/man/chronic)(1), [cron](/man/cron)(8)

# RESOURCES

```[Homepage](https://habilis.net/cronic/)```

<!-- verified: 2026-06-26 -->
