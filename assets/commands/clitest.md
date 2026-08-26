# TAGLINE

Doctest 风格的 Unix 命令行自动化测试工具

# TLDR

从文件**运行测试**

```clitest [examples/intro.txt]```

**显示帮助**

```clitest --help```

通过 Docker **运行**

```docker run --rm -t aureliojargas/clitest [tests.txt]```

# SYNOPSIS

**clitest** [*options*] *testfile*...

# DESCRIPTION

**clitest** 是一个可移植的 POSIX shell 脚本，它测试 Unix 命令行的方式与 Python **doctest** 测试交互式会话相同。你编写一个看起来像 shell 会话记录的文本文件（**$** 提示符、命令、期望的标准输出）。**clitest** 执行每条命令并检查输出是否完全匹配。

没有特殊的 DSL：测试文件使用熟悉的 CLI 语法。适合为 shell 工具和教程做文档化及回归测试。

安装方式是下载脚本、执行 **chmod +x** 并放到 **PATH** 中，或使用 Docker 镜像 **aureliojargas/clitest**。

# PARAMETERS

*testfile*

> 一个或多个测试会话记录文件的路径。

各选项（进度显示、前缀、环境变量以及失败行为）因版本而异，请参阅 **clitest --help**。

# EXAMPLE TEST FILE

```
$ echo "Hello World"
Hello World
$ cd /tmp
$ pwd
/tmp
```

# CAVEATS

输出必须完全匹配（空白字符和 locale 都有影响）。命令会在你的 shell 环境中真实运行；避免破坏性示例。交互式程序和 TUI 应用不适合。脚本本身可移植于各种 sh，但个别测试可能依赖 Linux 实用工具。

# INSTALL

```dnf: sudo dnf install clitest```

```pacman: sudo pacman -S clitest```

```brew: brew install clitest```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bats](/man/bats)(1), [shunit2](/man/shunit2)(1), [expect](/man/expect)(1)

# RESOURCES

```[Source code](https://github.com/aureliojargas/clitest)```

<!-- verified: 2026-07-19 -->
