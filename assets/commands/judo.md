# TAGLINE

由 YAML 驱动的 CLI 集成测试框架

# TLDR

**运行 YAML 文件中的测试**

```judo [path/to/test.yml]```

**运行测试套件目录**

```judo [path/to/tests/]```

**带超时时间运行**

```judo [path/to/test.yml] --timeout [5000]```

**生成 JUnit 报告**

```judo [path/to/test.yml] --junitreport```

# SYNOPSIS

**judo** [**--timeout** _ms_] [**--junitreport**] _file_|_directory_

# DESCRIPTION

**judo** 是一个 CLI 集成测试框架，通过简单的 YAML 或 JSON 文件测试命令行工具。它执行命令、在预期 stdout 输出出现时响应 stdin、断言退出码，并验证 stdout 和 stderr 是否包含（或不包含）特定字符串。

该框架专为 CLI 应用的自动化测试设计，仅依赖 stdin、stdout 和 stderr 三者即可工作，因此非常适合 CI/CD 流水线。

# CAVEATS

安装需要 **Node.js** 和 npm。测试场景必须以 YAML 或 JSON 格式定义。具有复杂终端处理的交互式程序可能无法完全测试。

# HISTORY

**judo** 由 **Intuit** 开发，使用 **JavaScript/Node.js** 编写。它的目标是简化自动化环境中命令行工具的集成测试。

# INSTALL

```apk: sudo apk add judo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bats](/man/bats)(1), [expect](/man/expect)(1)
