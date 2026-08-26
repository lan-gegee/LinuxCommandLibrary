# TAGLINE

在 Linux aarch64 上运行 macOS ARM64 二进制文件（用户态翻译层）

# TLDR

**安装** CLI 并**确保** guest bottle 就绪

```cargo install kakehashi```

```kh bottle ensure```

向 bottle **安装** Darwin guest 工具

```kh install 7zip```

```kh install curl```

**运行** Darwin 二进制文件（guest 参数放在 **--** 之后）

```kh run 7zz -- --help```

```kh run 7zz -- a demo.7z README.md```

**检查** Mach-O 二进制文件而不执行它

```kh inspect [path/to/binary] --sections --imports```

**跟踪** guest 二进制文件的系统调用

```kh trace [path/to/binary] -- [args]```

# SYNOPSIS

**kh** [**-v**...] [**--json**] _subcommand_ [_options_] [_args_]

# DESCRIPTION

**kh** 是 **Kakehashi** 的命令行前端。Kakehashi 是一个用户态翻译层，能够在 **Linux aarch64** 上加载 Darwin **Mach-O** 二进制文件（macOS ARM64），映射独立的 **libSystem** 并翻译 BSD 系统调用，从而让真实的 guest 工具无需 JIT 即可运行。

实际执行需要 **Linux aarch64** 环境（裸机、VM 或 Docker/Colima）。试加载和检查可在任何主机上进行，包括 macOS。guest 工具被安装到单一的 **bottle** 中（默认位于 XDG 数据目录下，通常为 **~/.local/share/kakehashi/bottle/**），该目录提供类 macOS 的文件系统布局；**/Volumes/linux/…** 桥接到主机根目录。

已验证的 guest 工具包括 Darwin 版 **7zz**（7-Zip）和 **curl**。不承诺支持完整的 Apple 框架、GUI 应用、codesign 或与 curl 完全对等的功能特性。使用 **cargo install kakehashi** 安装（需要 Rust 1.88+）。

# PARAMETERS

**-v**, **--verbose**
> 提高日志详细程度（可重复）。设置后会覆盖 **KAKEHASHI_LOG**。

**--json**
> 在子命令支持时输出 JSON。

**inspect** [_path_] [**--sections**] [**--imports**] [**--find** _substr_] [**--load-commands**] [**--image**] [**--page-size** _bytes_] [**--host-page-size**]
> 静态检查 Mach-O 文件而不执行。

**run** _path_ [**--root** _dir_] [**--max-syscalls** _n_] [**--expect-code** _code_] [**--guest-page-size** _bytes_] [**--dry-load**] [**--**] [_guest_args_…]
> 在翻译层下运行 Mach-O 二进制文件。guest 的 argv 跟在程序名之后（当使用已安装的 bottle 名称如 **7zz** 时通常位于 **--** 之后）。

**trace** _path_ [**--root** _dir_] [**--max-events** _n_] [**--**] [_guest_args_…]
> 捕获 guest 二进制文件的系统调用/陷入事件。

**bottle create|ensure|destroy|path|status**
> 管理已注册的 bottle（**ensure** 会在缺失时创建并刷新 libSystem）。

**install** _package_
> 向 bottle 安装 guest 工具。软件包包括 **7zip**、**curl**、**xcode-tools**（别名 **clt**、**git**），或 **list**。

# CONFIGURATION

**KAKEHASHI_ROOT** / **--root**
> Bottle 根路径。

**KAKEHASHI_DATA_DIR**, **KAKEHASHI_CONFIG_DIR**, **KAKEHASHI_CACHE_DIR**
> 覆盖 XDG 风格的数据、配置和缓存目录位置。

**KAKEHASHI_LIBSYSTEM**
> 不使用内嵌副本时，指定 guest **libSystem.B.dylib**（或独立等价物）的路径。

**KAKEHASHI_LOG**
> 未设置 **-v** 时的跟踪过滤器（默认 **warn**）。

**KAKEHASHI_HYPERCALL**
> Hypercall 路径对 guest 线程默认开启；仅在调试时设为 **0**。

**KAKEHASHI_FORCE_DOWNLOAD**, **KAKEHASHI_7ZZ**, **KAKEHASHI_CURL**, **KAKEHASHI_XCODE_TOOLS_VERSION**
> 控制 **kh install** 对可选 guest 工具的下载和版本选择。

# CAVEATS

实际的 **run**/**trace** 需要 **Linux aarch64**（4 KiB 或 16 KiB 页大小）。与 Darling 无关；不要期望 GUI、codesign 或完整的 Apple Security.framework 支持。系统调用密集的多文件工作负载可能比原生 Linux 工具慢数倍。实验性项目 —— guest 支持范围仍在扩大。

# HISTORY

**Kakehashi** 是一个以 CLI 优先的开源用户态 Darwin→Linux aarch64 翻译层（Apache-2.0）。其发布的二进制名称为 **kh**。

# SEE ALSO

[darling](/man/darling)(1), [wine](/man/wine)(1), [cargo](/man/cargo)(1), [7z](/man/7z)(1), [curl](/man/curl)(1)

# RESOURCES

```[Source code](https://github.com/wie-project/kakehashi)```

```[Documentation](https://github.com/wie-project/kakehashi/tree/main/docs)```

<!-- verified: 2026-08-02 -->
