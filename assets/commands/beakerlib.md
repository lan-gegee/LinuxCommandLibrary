# TAGLINE

Shell 层级的集成测试库

# TLDR

**创建基础测试脚本**

```rlJournalStart && rlPhaseStart FAIL "Setup" && rlRun "command" && rlPhaseEnd && rlJournalEnd```

**运行命令并断言成功**

```rlRun "[command]" 0 "Command should succeed"```

**运行命令并预期失败**

```rlRun "[command]" 1 "Command should fail with exit code 1"```

**断言文件存在**

```rlAssertExists [path/to/file]```

**断言字符串相等**

```rlAssertEquals "Test value" "[actual]" "[expected]"```

**记录信息性消息**

```rlLog "Informational message"```

**备份和恢复文件**

```rlFileBackup [path/to/file] && rlRun "[modify file]" && rlFileRestore```

# SYNOPSIS

测试脚本 source BeakerLib 并使用其函数：

```source /usr/share/beakerlib/beakerlib.sh```

# FUNCTIONS

**rlJournalStart**
> 初始化测试日志；必须最先调用。

**rlJournalEnd**
> 结束日志并生成报告。

**rlPhaseStart** _type_ _name_
> 开始一个测试阶段（FAIL、WARN 或 pass 类型）。

**rlPhaseEnd**
> 结束当前测试阶段。

**rlRun** _command_ [_expected_exit_] [_comment_]
> 运行命令并检查退出码。

**rlAssertEquals** _comment_ _value1_ _value2_
> 断言两个值相等。

**rlAssertExists** _path_
> 断言文件或目录存在。

**rlAssertNotExists** _path_
> 断言文件或目录不存在。

**rlAssertGrep** _pattern_ _file_
> 断言文件中存在匹配模式的内容。

**rlLog** _message_
> 记录一条信息性消息。

**rlFileBackup** _file_...
> 备份文件以便日后恢复。

**rlFileRestore**
> 恢复之前备份的文件。

**rlServiceStart** / **rlServiceStop**
> 启动或停止系统服务。

# DESCRIPTION

**BeakerLib** 是一个 Shell 层级的集成测试库，主要用于测试 RPM 软件包和系统组件。它提供了一系列函数，可将测试组织为阶段、运行带断言的命令、管理文件和服务，以及生成结构化的测试报告。

测试组织为包含多个阶段的日志（journal）。每个阶段将相关的断言和日志归为一组。该库自动处理准备/清理、结果收集和报告生成。

BeakerLib 为 Red Hat 和 Fedora 质量保证体系所用的 **Beaker** 测试框架设计，但也可以独立用于任何基于 Shell 的集成测试。测试可生成多种格式的日志，包括 HTML 和 JUnit XML。

# CAVEATS

BeakerLib 主要面向 RHEL/Fedora 生态，在其他发行版上的可用性不一。基于 Shell 的方式可能比编译型测试框架慢。复杂断言需要多次函数调用。每个测试脚本开头都必须 source 该库。

# HISTORY

BeakerLib 由 **Red Hat** 开发，是 **Beaker** 集成测试基础设施的一部分，最初为测试 RHEL 软件包和系统组件而设计。它从 **2000 年代中期**的内部工具发展而来，随 Beaker 一起开源。该库作为 Red Hat 质量工程工具链的一部分持续维护至今。

# INSTALL

```dnf: sudo dnf install beakerlib```

```aur: yay -S beakerlib```

```brew: brew install beakerlib```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bats](/man/bats)(1)
