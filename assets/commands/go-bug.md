# TAGLINE

打开 Go 问题跟踪器并附上系统信息

# TLDR

**打开 bug 报告页面**

```go bug```

# SYNOPSIS

**go bug**

# DESCRIPTION

**go bug** 在网页浏览器中打开 Go 问题跟踪器，并预填系统信息。它会收集 Go 版本、平台和环境细节，以简化 bug 报告流程。

该命令自动收集相关的诊断信息并将浏览器打开到 GitHub issue 表单，从而简化向 Go 项目报告问题的过程。

# CAVEATS

会打开浏览器。信息可能包含环境变量。提交前请先检查。

# HISTORY

go bug 被加入 **Go** 工具链，通过自动收集环境信息来简化 bug 报告。

# SEE ALSO

[go](/man/go)(1), [go-version](/man/go-version)(1)

# RESOURCES

```[Documentation](https://pkg.go.dev/cmd/go#hdr-Start_a_bug_report)```

```[Source code](https://github.com/golang/go)```

<!-- verified: 2026-07-17 -->
