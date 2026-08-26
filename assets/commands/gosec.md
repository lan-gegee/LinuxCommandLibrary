# TAGLINE

Go 源码安全扫描器

# TLDR

**扫描**当前包及其所有子包

```gosec ./...```

**扫描**指定的包或目录

```gosec [path/to/package]```

以指定格式**写出报告**（json、yaml、csv、html、sarif 等）

```gosec -fmt [format] -out [path/to/report] ./...```

按 ID **只运行**特定规则

```gosec -include [G101,G201] ./...```

按 ID **排除**特定规则

```gosec -exclude [G104] ./...```

**跳过**一个或多个目录

```gosec -exclude-dir [vendor] ./...```

按严重级别和置信度**过滤**发现的问题

```gosec -severity [medium] -confidence [medium] ./...```

在扫描中**包含**测试文件

```gosec -tests ./...```

# SYNOPSIS

**gosec** [_options_] _package_...

# DESCRIPTION

**gosec**（Go Security Checker）通过将每个包的抽象语法树（AST）与一组内置规则进行比对，检查 Go 源码中的安全问题。每条规则都有一个形如 **Gnnn** 的标识符（例如 **G101** 表示硬编码凭据，**G401** 表示使用弱加密原语），并会报告每个匹配项所在的文件、行号、严重级别和置信度。

它专为持续集成流水线设计：结果可以输出为 JSON、YAML、CSV、SARIF、JUnit XML 等机器可读格式，并且在发现问题时可将退出状态置为非零。通过规则选择、严重级别和置信度阈值、目录排除以及行内 **#nosec** 注释，你可以把输出信号调整到项目所需的状态。

# PARAMETERS

**-fmt** _format_

> 设置输出格式：text（默认）、json、yaml、csv、junit-xml、html、sonarqube、golint、sarif。

**-out** _file_

> 把报告写入指定文件而不是标准输出。

**-include** _ids_

> 以逗号分隔、只运行的规则 ID 列表。

**-exclude** _ids_

> 以逗号分隔、要跳过的规则 ID 列表。

**-exclude-dir** _dir_

> 将某个目录排除在扫描之外；可以重复指定。

**-severity** _level_

> 只报告达到指定严重级别及以上的问题（low、medium、high）。

**-confidence** _level_

> 只报告达到指定置信度及以上的问题（low、medium、high）。

**-tests**

> 在分析中包含 Go 测试文件（**_test.go**）。

**-no-fail**

> 始终以状态码 0 退出，即使发现了问题。

# CAVEATS

gosec 执行的是静态分析，可能产生误报；对已经人工确认过的发现，可用 **#nosec** 注释或规则排除来消除告警。它可以作为补充手段，但不能取代运行时测试和 govulncheck 等依赖漏洞扫描。

# HISTORY

gosec 的前身是 **gas**（Go AST Scanner），后来更名。它由 **securego** 社区项目维护，已被广泛集成到 Go 的 CI 工具链中，包括 golangci-lint。

# INSTALL

```dnf: sudo dnf install gosec```

```apk: sudo apk add gosec```

```zypper: sudo zypper install gosec```

```brew: brew install gosec```

```nix: nix profile install nixpkgs#gosec```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[golangci-lint](/man/golangci-lint)(1), [staticcheck](/man/staticcheck)(1), [semgrep](/man/semgrep)(1), [go](/man/go)(1)

# RESOURCES

```[Source code](https://github.com/securego/gosec)```

<!-- verified: 2026-06-16 -->
