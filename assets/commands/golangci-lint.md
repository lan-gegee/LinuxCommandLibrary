# TAGLINE

快速的 Go linter 聚合器

# TLDR

在当前项目中**运行所有已启用的 linter**

```golangci-lint run```

**对指定的包运行 linter**

```golangci-lint run ./cmd/... ./internal/...```

在默认配置之外**启用特定 linter**

```golangci-lint run --enable errcheck --enable gocritic```

**只运行特定 linter**（禁用其他所有）

```golangci-lint run --disable-all --enable gosimple --enable govet```

**显示所有可用的 linter** 及其状态

```golangci-lint linters```

使用指定的配置文件**运行**

```golangci-lint run -c [.golangci.yml]```

在支持的地方自动**修复问题**

```golangci-lint run --fix```

以 JSON 格式**输出结果**

```golangci-lint run --out-format json```

# SYNOPSIS

**golangci-lint** _command_ [_options_]

# PARAMETERS

**run**
> 在当前项目上运行 linter。

**linters**
> 列出可用的 linter 及其启用/禁用状态。

**cache**
> 缓存管理命令（clean、status）。

**version**
> 显示版本信息。

**--enable** _LINTER_
> 启用特定的 linter。可多次指定。

**--disable** _LINTER_
> 禁用特定的 linter。可多次指定。

**--disable-all**
> 先禁用所有 linter，再用 --enable 选择性地启用。

**--fix**
> 在 linter 支持的情况下自动修复问题。

**--out-format** _FORMAT_
> 输出格式：colored-line-number（默认）、json、tab、checkstyle、github-actions 等。

**--timeout** _DURATION_
> 总运行的超时时间。默认：**1m**。

**--new**
> 只显示新代码中的问题（基于 git）。

**--new-from-rev** _REV_
> 只显示自给定 git 修订版本以来的改动中的问题。

**-c** _FILE_, **--config** _FILE_
> 配置文件的路径。

**--no-config**
> 不读取任何配置文件。

**-j** _N_, **--concurrency** _N_
> 并发运行的 linter goroutine 数量。默认为 CPU 数量。

**--help**
> 显示帮助信息。

# DESCRIPTION

**golangci-lint** 是一个高速的 Go linter 运行器，把数十个 linter 聚合到一个工具里。它提供并行执行、结果缓存和统一配置，用于检查风格、bug、性能和安全问题。

通过 .golangci.yml 可以进行项目级配置，选择 linter 并定制规则，从而不必再分别单独运行各个 linter。运行结果会被缓存，加快后续执行。

# CONFIGURATION

**.golangci.yml** / **.golangci.yaml**
> 项目级配置文件，用于选择 linter 以及设置规则、严重级别和排除项。

# CAVEATS

首次运行时因要构建缓存可能较慢。默认启用的 linter 集合会随版本变化而改变。为了获得可复现的结果，请在 CI 中固定所用的版本。部分 linter 之间可能存在冲突。

# INSTALL

```dnf: sudo dnf install golangci-lint```

```pacman: sudo pacman -S golangci-lint```

```apk: sudo apk add golangci-lint```

```zypper: sudo zypper install golangci-lint```

```brew: brew install golangci-lint```

```nix: nix profile install nixpkgs#golangci-lint```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go-vet](/man/go-vet)(1), [staticcheck](/man/staticcheck)(1), [gofmt](/man/gofmt)(1), [go](/man/go)(1)
