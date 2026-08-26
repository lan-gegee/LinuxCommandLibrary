# TAGLINE

面向 C/C++ 和 Rust 的共享编译缓存

# TLDR

**启动服务器**

```sccache --start-server```

**显示统计信息**

```sccache --show-stats```

**停止服务器**

```sccache --stop-server```

**统计信息清零**

```sccache --zero-stats```

**配合 cargo 使用**

```RUSTC_WRAPPER=sccache cargo build```

**配合 cmake 使用**

```cmake -DCMAKE_C_COMPILER_LAUNCHER=sccache -DCMAKE_CXX_COMPILER_LAUNCHER=sccache [..]```

**显示高级统计信息**（包括缓存位置）

```sccache --show-adv-stats```

以 JSON **格式显示统计信息**

```sccache --show-stats --stats-format json```

# SYNOPSIS

**sccache** [_--start-server_] [_--stop-server_] [_--show-stats_] [_options_]

# PARAMETERS

**--start-server**
> 启动服务器守护进程。

**--stop-server**
> 停止服务器。

**--show-stats**
> 显示缓存统计信息。

**--zero-stats**
> 重置统计信息。

**--show-adv-stats**
> 显示高级统计信息。

**--dist-auth** _TOKEN_
> 向分布式构建服务器进行身份验证。

**--dist-status**
> 显示分布式构建状态。

**--stats-format** _FMT_
> 设置统计信息的输出格式（text 或 json）。

# CONFIGURATION

**SCCACHE_DIR**
> 本地缓存目录路径（默认：Linux 上为 ~/.cache/sccache，macOS 上为 ~/Library/Caches/sccache）。

**SCCACHE_CACHE_SIZE**
> 本地缓存的最大大小（例如 "10G"）。

**SCCACHE_REDIS**
> 用于跨机器共享缓存的 Redis 服务器 URL。

**SCCACHE_BUCKET**
> 用于基于 AWS 共享缓存的 S3 存储桶名称。

**SCCACHE_GCS_BUCKET**
> 用于基于 GCS 共享缓存的 Google Cloud Storage 存储桶。

**SCCACHE_MEMCACHED**
> 用于共享缓存的 Memcached 服务器 URL（例如 "tcp://hostname:port"）。

**SCCACHE_ERROR_LOG**
> 重定向服务器错误日志输出的路径。

**SCCACHE_LOG**
> 服务器的日志级别（例如 "debug"、"trace"）。

**SCCACHE_RECACHE**
> 设置后覆盖已有的缓存条目。

**RUSTC_WRAPPER**
> 设为 "sccache" 可通过 cargo 为 Rust 构建启用缓存。

# DESCRIPTION

**sccache** 是一款支持 C、C++、Rust 及其他语言的编译器缓存。它缓存编译结果以加速重新构建。

服务器以守护进程方式运行，缓存编译输出。相同输入的后续编译会立即返回缓存的结果。

本地缓存将结果存储在磁盘上。云后端（S3、GCS、Redis、Azure）可实现跨机器和 CI 的共享缓存。

通过 RUSTC_WRAPPER 集成 Rust，缓存 rustc 的调用。cargo 构建系统会自动使用该包装器。

C/C++ 集成使用编译器启动器或包装脚本。CMake 的 launcher 变量提供了干净的集成方式。

分布式编译可将任务调度到多台机器上执行。这使构建的扩展能力超越单机并行。

# CAVEATS

非确定性构建会降低命中率。某些编译器选项会导致无法缓存。云存储存在延迟。服务器必须处于运行状态。

# HISTORY

**sccache** 由 **Mozilla** 自 **2016 年**前后开始开发，用于 Firefox 构建。它凭借云存储和 Rust 支持，成为 ccache 的替代品。

# INSTALL

```apt: sudo apt install sccache```

```dnf: sudo dnf install sccache```

```pacman: sudo pacman -S sccache```

```apk: sudo apk add sccache```

```zypper: sudo zypper install sccache```

```brew: brew install sccache```

```nix: nix profile install nixpkgs#sccache```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ccache](/man/ccache)(1), [cargo](/man/cargo)(1), [rustc](/man/rustc)(1), [cmake](/man/cmake)(1), [make](/man/make)(1)
