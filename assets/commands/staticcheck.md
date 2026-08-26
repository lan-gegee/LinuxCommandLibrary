# TAGLINE

先进的 Go 静态分析检查器

# TLDR

**分析当前模块中的所有包**

```staticcheck ./...```

**分析指定的包**

```staticcheck [package1] [package2]```

**仅运行特定检查**

```staticcheck -checks "SA*,ST1000" ./...```

**忽略特定检查**

```staticcheck -checks "all,-ST1003" ./...```

**以不同格式输出**

```staticcheck -f [stylish] ./...```

**显示某个检查的解释**

```staticcheck -explain [SA1019]```

**显示版本**

```staticcheck -version```

# SYNOPSIS

**staticcheck** [_flags_] [_packages_]

# PARAMETERS

**-checks** _checks_
> 要运行的检查的逗号分隔列表。支持通配符和取反。

**-f** _format_
> 输出格式：text（默认）、stylish、json、sarif 或 null。

**-fail** _checks_
> 导致发现问题时以非零值退出的检查的逗号分隔列表。

**-explain** _check_
> 显示特定检查的详细解释。

**-show-ignored**
> 包含已通过指令显式忽略的发现。

**-go** _version_
> 兼容性检查的目标 Go 版本。

**-debug.cpuprofile** _file_
> 将 CPU profile 写入文件。

**-debug.memprofile** _file_
> 将内存 profile 写入文件。

**-debug.version**
> 打印详细的版本信息。

**-version**
> 显示版本信息。

# DESCRIPTION

**staticcheck** 是 Go 语言先进的静态分析检查器。它使用超出标准 **go vet** 工具范围的复杂分析技术来查找 bug、性能问题和代码质量问题。

该工具包含 150 多项检查，按类别组织：SA（staticcheck——bug 与正确性）、S（simple——代码简化）、ST（stylecheck——风格问题）、QF（quickfix——建议改进）和 U（unused——死代码检测）。

Staticcheck 无缝集成 Go 的工具链约定，接受与 **go build** 相同格式的包。它支持通过 **staticcheck.conf** 文件进行项目级设置，并支持 **//lint:ignore** 等内联指令来抑制特定警告。

该检查器是 VS Code 的 Go 扩展的默认选择，也作为 golangci-lint 的组件包含在内。它提供机器可读的输出格式，便于 CI/CD 集成。

# CAVEATS

在某些上下文中部分检查类别默认禁用。ST 检查（风格）中一些有争议的规则默认关闭。配置文件的语法与命令行标志不同。某些检查需要分析依赖项，会增加运行时间。该工具由 Dominik Honnef 开发，由 Google 提供赞助。

# HISTORY

**Staticcheck** 由 Dominik Honnef 创建，开发工作始于他在 Google 任职期间。它在 **go vet** 和 **golint** 等早期工具的基础上演进，提供更全面的静态分析。该工具在 Go 社区获得广泛采用，成为 VS Code Go 扩展的默认检查器。现在由 Google 和 Go 团队共同赞助。

# INSTALL

```dnf: sudo dnf install staticcheck```

```pacman: sudo pacman -S staticcheck```

```apk: sudo apk add staticcheck```

```brew: brew install staticcheck```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [golangci-lint](/man/golangci-lint)(1), [gofmt](/man/gofmt)(1)
