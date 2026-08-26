# TAGLINE

CMake 测试驱动程序

# TLDR

运行当前构建目录中的所有测试

```ctest```

以详细输出模式运行测试

```ctest -V```

按名称运行特定测试

```ctest -R [test_name_pattern]```

按名称排除测试

```ctest -E [exclude_pattern]```

并行运行测试

```ctest -j [4]```

设置超时时间

```ctest --timeout [60]```

列出可用的测试

```ctest -N```

重新运行失败的测试

```ctest --rerun-failed```

针对指定构建配置运行测试

```ctest -C [Release]```

# SYNOPSIS

**ctest** [_options_]

# PARAMETERS

**-V**, **--verbose**
> 详细输出。

**-R** _regex_
> 运行匹配正则表达式的测试。

**-E** _regex_
> 排除匹配正则表达式的测试。

**-j** _n_
> 并行运行测试。

**--timeout** _seconds_
> 单个测试的超时时间。

**-N**
> 仅列出测试而不运行。

**--rerun-failed**
> 只运行之前失败的测试。

**-L** _label_
> 运行具有指定标签的测试。

**--output-on-failure**
> 仅为失败的测试显示输出。

**-C** _config_, **--build-config** _config_
> 选择要测试的配置（如 Debug、Release）。

**-VV**, **--extra-verbose**
> 启用来自测试的更详细输出。

**--test-dir** _dir_
> 指定查找测试所在的目录。

**--stop-on-failure**
> 在第一次失败后停止运行测试。

# DESCRIPTION

**ctest** 是 CMake 的测试驱动程序，负责发现并运行 CMake 项目中定义的测试。它执行通过 CMake 的 **add_test()** 命令定义的测试，并提供详细的通过/失败报告。

该工具支持并行执行测试、按名称或标签过滤、超时控制以及重跑失败的测试。它与 CMake 构建系统集成，可在编译后于构建目录中运行。

ctest 常用于 CI/CD 流水线中的自动化测试，其输出可以格式化为多种持续集成系统所需的样式。它能处理测试依赖和 fixture 的搭建与清理，并可将结果导出为 JUnit XML 等多种格式。

# CAVEATS

必须在包含 CTestTestfile.cmake 的 CMake 构建目录中运行。测试必须使用 add_test() 在 CMakeLists.txt 中定义。资源限制和超时按单个测试生效，而非全局生效。

# HISTORY

ctest 由 **Kitware** 作为 **CMake** 的一部分推出，自 21 世纪初起就是 CMake 套件的组成部分。它与 CMake 同步演进，为跨平台构建提供了完善的测试基础设施。

# INSTALL

```apt: sudo apt install cmake```

```dnf: sudo dnf install cmake```

```pacman: sudo pacman -S cmake```

```apk: sudo apk add cmake```

```zypper: sudo zypper install cmake```

```brew: brew install cmake```

```nix: nix profile install nixpkgs#cmake```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmake](/man/cmake)(1), [make](/man/make)(1)
