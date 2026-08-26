# TAGLINE

Go 源码风格 linter（已废弃）

# TLDR

**对当前包进行 lint**

```golint .```

**对指定文件进行 lint**

```golint [file.go]```

**递归 lint 各个包**

```golint ./...```

**设置最低置信度**

```golint -min_confidence [0.8] ./...```

# SYNOPSIS

**golint** [_options_] [_packages_]

# PARAMETERS

**-min_confidence** _n_
> 报告问题的最低置信度（0.0-1.0）。

**-set_exit_status**
> 发现问题时以非零状态退出。

_packages_
> 要 lint 的包路径。

# DESCRIPTION

**golint** 依据 Effective Go 与 Go Code Review Comments 中的准则，检查 Go 源码中的风格问题。它侧重于命名约定、注释和代码结构。

与查找 bug 的 go vet 不同，golint 关注的是风格和可读性。其输出是建议而不是错误。该工具已被弃用，建议改用 staticcheck 或 golangci-lint。

# CAVEATS

已被弃用，请改用 staticcheck 或 golangci-lint。给出的建议属于风格层面，并非 bug。对某些项目的误报率较高。已不再积极维护。

# HISTORY

golint 由 Google 的 **Go 团队**创建，作为风格检查器使用。它于 **2021 年**被弃用，由 staticcheck 等更全面的 linter 取代。官方建议改用集成了多个 linter 的 golangci-lint。

# INSTALL

```nix: nix profile install nixpkgs#golint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [gofmt](/man/gofmt)(1), [staticcheck](/man/staticcheck)(1), [golangci-lint](/man/golangci-lint)(1)

# RESOURCES

```[Source code](https://github.com/golang/lint)```

<!-- verified: 2026-07-17 -->
