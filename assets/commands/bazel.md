# TAGLINE

快速、可扩展的多语言构建系统

# TLDR

**构建**目标

```bazel build [//path/to:target]```

**运行**二进制文件

```bazel run [//path/to:binary]```

**测试**目标

```bazel test [//path/to:tests]```

**查询**依赖

```bazel query "deps([//path/to:target])"```

**清理**构建产物

```bazel clean```

递归构建**所有**目标

```bazel build //...```

显示构建环境的**信息**

```bazel info```

# SYNOPSIS

**bazel** _command_ [_options_] [_targets_]

# DESCRIPTION

**bazel** 是一个快速、可扩展的构建系统，支持多语言项目和超大规模代码库。它由 Google 基于其内部的 Blaze 系统开发，提供可重现的构建、远程缓存和分布式执行。

该工具专为 monorepo 以及需要严格依赖管理和增量构建的项目而设计。

# PARAMETERS

**build** _target_
> 构建指定目标

**run** _target_
> 构建并运行可执行目标

**test** _target_
> 构建并运行测试

**query** _expression_
> 查询构建图

**cquery** _expression_
> 查询已配置的构建图（分析之后）

**aquery** _expression_
> 查询动作图

**clean**
> 删除构建产物

**fetch** _target_
> 拉取外部依赖

**coverage** _target_
> 为测试生成代码覆盖率报告

**version**
> 打印 Bazel 版本

**shutdown**
> 停止 Bazel 服务器

**info**
> 显示构建环境信息

**--jobs** _n_
> 并行作业数

**--config** _name_
> 使用 .bazelrc 中的配置

**--remote_cache** _url_
> 远程缓存 URL

**--disk_cache** _path_
> 磁盘缓存位置

**--compilation_mode** (_-c_) _mode_
> 编译模式：fastbuild、dbg 或 opt

**--keep_going** (_-k_)
> 出错后继续构建

**--verbose_failures**
> 显示失败命令的完整命令行

# TARGET SYNTAX

- **//path/to:target** - 特定目标
- **//path/to:all** - 软件包中的所有目标
- **//...** - 递归的所有目标
- **@repo//path:target** - 外部仓库

# FEATURES

- 增量构建
- 远程缓存
- 分布式执行
- 密封构建
- 多语言支持（Java、C++、Go、Python 等）
- 依赖分析
- 可重现构建

# BUILD FILES

BUILD 或 BUILD.bazel 文件定义目标：
```python
cc_binary(
    name = "hello",
    srcs = ["hello.cc"],
)
```

# CONFIGURATION

**~/.bazelrc**
> 用户级构建选项和配置标志。

**WORKSPACE** 或 **WORKSPACE.bazel**（Bzlmod 则为 **MODULE.bazel**）
> 定义外部依赖和项目边界的根文件。

**.bazelrc**
> 项目级构建选项、配置组和默认标志。

# CAVEATS

学习曲线陡峭。项目中处处需要 BUILD 文件。初始配置复杂。对小型项目而言可能大材小用。构建耗时包含分析阶段。基于 JVM（内存占用高）。

# HISTORY

**Bazel** 由 Google 于 **2015** 年作为其内部 Blaze 构建系统的开源版本发布，旨在处理大规模的多语言 monorepo。

# INSTALL

```apt: sudo apt install bazel-bootstrap```

```pacman: sudo pacman -S bazel```

```brew: brew install bazel```

```nix: nix profile install nixpkgs#bazel```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[make](/man/make)(1), [cmake](/man/cmake)(1), [ninja](/man/ninja)(1), [gradle](/man/gradle)(1), [buck](/man/buck)(1)
