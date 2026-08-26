# TAGLINE

Go 包测试框架

# TLDR

**运行当前包中的测试**

```go test```

**以详细输出运行测试**

```go test -v```

**按模式运行特定测试**

```go test -run [TestName]```

**运行基准测试**

```go test -bench .```

**启用竞态检测器运行**

```go test -race```

**启用覆盖率检测运行**

```go test -cover```

**生成覆盖率分析文件**

```go test -coverprofile=[coverage.out]```

**运行所有包中的测试**

```go test ./...```

# SYNOPSIS

**go** **test** [_build/test flags_] [_packages_] [_flags for test binary_]

# PARAMETERS

**-v**
> 详细输出。

**-run** _regexp_
> 只运行匹配模式的测试。

**-bench** _regexp_
> 运行匹配模式的基准测试。

**-cover**
> 启用覆盖率分析。

**-coverprofile** _file_
> 将覆盖率写入文件。

**-race**
> 启用竞态检测器。

**-count** _n_
> 每个测试运行 n 次。

**-timeout** _d_
> 测试超时时间（默认 10m）。

**-short**
> 让测试缩短耗时较长的操作。

**-parallel** _n_
> 测试的最大并行执行数。

**-json**
> 以 JSON 格式输出结果。

# DESCRIPTION

**go test** 自动执行 Go 包的测试。它会编译并运行包含 Test*、Benchmark*、Example* 命名函数的测试文件（*_test.go）。测试可以并行运行、进行竞态检测，并生成覆盖率报告。

该命令会按需重新编译包，并缓存成功的测试结果（设置 **-count=1** 可绕过缓存）。它在测试前会对包自动运行 **go vet**，并支持子测试、表驱动测试和模糊测试，以实现全面的验证。

# CAVEATS

只要未设置 **-count=1**，未变化的测试就会复用缓存的结果。只有 `*_test.go` 文件中匹配 `Test*`、`Benchmark*`、`Example*` 和 `Fuzz*` 的函数才会被识别。

# INSTALL

```apt: sudo apt install gccgo-go```

```dnf: sudo dnf install gcc-go```

```pacman: sudo pacman -S gcc-go```

```apk: sudo apk add gcc-go```

```zypper: sudo zypper install gcc-go```

```brew: brew install go```

```nix: nix profile install nixpkgs#go```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[go](/man/go)(1), [go-build](/man/go-build)(1)

# RESOURCES

```[Documentation](https://pkg.go.dev/cmd/go#hdr-Test_packages)```

<!-- verified: 2026-07-17 -->
