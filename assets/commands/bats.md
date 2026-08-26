# TAGLINE

Bash 脚本自动化测试框架

# TLDR

**运行**测试文件

```bats [test.bats]```

**运行**目录中的所有测试

```bats [tests/]```

**TAP 格式**输出

```bats --tap [test.bats]```

**美观**格式化

```bats --pretty [test.bats]```

**按测试名过滤**

```bats --filter ["pattern"] [test.bats]```

# SYNOPSIS

**bats** [_options_] _test-file_...

# DESCRIPTION

**bats**（Bash Automated Testing System）是一个符合 TAP 规范的 Bash 脚本测试框架。它提供简洁的语法来编写测试，并以可读性良好的输出执行它们。

该工具为 Shell 脚本实现测试驱动开发和持续集成提供了支持。

# PARAMETERS

**-c**, **--count**
> 只统计测试数量而不运行

**-f**, **--filter** _pattern_
> 按名称模式过滤测试

**-t**, **--tap**
> 以 TAP 格式输出

**-p**, **--pretty**
> 美观地打印输出

**-r**, **--recursive**
> 递归运行测试

**-j**, **--jobs** _num_
> 并行作业数（需要 GNU parallel）

**-F**, **--formatter** _name_
> 输出格式化器（pretty、tap、tap13、junit）

**-T**, **--timing**
> 为测试添加计时信息

**-x**, **--trace**
> 在执行时打印测试命令（类似 set -x）

**--filter-tags** _tags_
> 只运行匹配所有逗号分隔标签的测试

**--filter-status** _status_
> 按上次运行的状态运行测试（failed、missed）

**-o**, **--output** _dir_
> 报告文件的写入目录

**--no-tempdir-cleanup**
> 保留测试输出的临时目录

**--print-output-on-failure**
> 测试失败时自动打印 $output

**-v**, **--version**
> 显示版本号

# TEST SYNTAX

```bash
#!/usr/bin/env bats

@test "addition works" {
  result="$(echo 2+2 | bc)"
  [ "$result" -eq 4 ]
}

@test "files exist" {
  [ -f "/etc/hosts" ]
}
```

# ASSERTIONS

使用标准 bash 测试运算符：
- **[ -f file ]** - 文件存在
- **[ "$a" = "$b" ]** - 字符串相等
- **[ $n -eq 4 ]** - 数值相等

# HELPER FUNCTIONS

**run** _command_
> 运行命令并捕获输出/状态

**load** _file_
> 加载辅助库

**skip** [_reason_]
> 跳过当前测试

# CAVEATS

测试在子 shell 中运行（副作用受限）。没有内置断言库（需使用 test-helper）。并行执行可能出现顺序问题。调试可能比较棘手。

# HISTORY

**bats** 由 Sam Stephenson 于 **2011** 年创建，借鉴了其他语言中类似工具的设计，旨在为 bash 脚本提供一个简单的测试框架。该项目后来被社区分叉并维护为 **bats-core**。

# INSTALL

```dnf: sudo dnf install bats```

```pacman: sudo pacman -S bats```

```apk: sudo apk add bats-core```

```zypper: sudo zypper install bats```

```brew: brew install bats-core```

```nix: nix profile install nixpkgs#bats```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[bash](/man/bash)(1), [shellcheck](/man/shellcheck)(1)
