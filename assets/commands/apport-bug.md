# TAGLINE

提交附带自动系统诊断信息的错误报告。

# TLDR

报告关于**整个系统**的错误

```apport-bug```

报告关于**特定软件包**的错误

```apport-bug [package]```

报告关于**特定可执行文件**的错误

```apport-bug [path/to/executable]```

报告关于**特定进程**的错误

```apport-bug [PID]```

报告关于 **Linux 内核**的错误

```apport-bug linux```

从现有的**崩溃文件**报告错误

```apport-bug [/var/crash/_bin_bash.1000.crash]```

# SYNOPSIS

**apport-bug** [_symptom_|_PID_|_package_|_program path_|_crash file_]

**apport-collect** _report-number_

# DESCRIPTION

**apport-bug** 向你所处发行版的缺陷跟踪系统报告问题，并利用 Apport 收集本地系统信息，帮助开发者更高效地诊断和修复问题。

推荐的做法是不带参数直接运行命令，查看已知症状列表并选择最相关的一项。这样生成的错误报告最有价值。

该工具会自动检测桌面环境，并相应地启动 **apport-gtk** 或 **apport-kde**。如果两者都不可用，或者会话不在 X11 下运行，则回退到 **apport-cli** 进行命令行交互。

# CAVEATS

仅在 Ubuntu 及基于 Ubuntu 的发行版上可用。提交错误报告需要配置好的 Launchpad 账户。**/var/crash/** 中的崩溃文件会在大约 7 天后自动删除。

# HISTORY

Apport 由 Canonical 为 Ubuntu 开发，大约在 **2006** 年首次推出，是一个自动化崩溃报告系统。后来演进出 **apport-bug** 这一面向用户的工具，用于手动提交带有自动收集的系统诊断信息的错误报告。

# SEE ALSO

[apport-cli](/man/apport-cli)(1), [apport-unpack](/man/apport-unpack)(1), [ubuntu-bug](/man/ubuntu-bug)(1)

# RESOURCES

```[Source code](https://git.launchpad.net/apport)```

```[Documentation](https://wiki.ubuntu.com/Apport)```

<!-- verified: 2026-06-11 -->
