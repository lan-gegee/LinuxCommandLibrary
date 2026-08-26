# TAGLINE

用于加速重新编译的编译器缓存

# TLDR

**显示缓存统计信息**

```ccache -s```

**显示详细缓存统计**，包括命中率

```ccache -sv```

**清空缓存**

```ccache -C```

**设置最大缓存大小**

```ccache -M [5G]```

**显示当前配置**

```ccache -p```

**统计计数器归零**

```ccache -z```

**通过 ccache 运行编译器**

```ccache [gcc] -c [file.c]```

**设置一个配置项**

```ccache -o [max_size=10G]```

**显示缓存目录路径**

```ccache -k cache_dir```

# SYNOPSIS

**ccache** [_options_]

**ccache** _compiler_ [_compiler_options_]

# DESCRIPTION

**ccache** 是一个编译器缓存，通过缓存先前的编译结果来加速重新编译。当检测到相同的编译时，它会返回缓存的结果而不是重新编译。

支持 GCC、Clang、MSVC 及类似编译器，涵盖 C、C++、Objective-C、CUDA 和汇编。

# PARAMETERS

**-s**, **--show-stats**
> 显示缓存统计摘要。

**-sv**
> 显示详细统计，包括命中/未命中详情。

**-z**, **--zero-stats**
> 将统计计数器归零。

**-C**, **--clear**
> 清空整个缓存。

**-M**, **--max-size** _size_
> 设置最大缓存大小（例如 5G、500M）。

**-F**, **--max-files** _count_
> 设置缓存中的最大文件数。

**-p**, **--show-config**
> 显示当前配置及其来源。

**-k**, **--get-config** _key_
> 获取单个配置项的值。

**-o**, **--set-config** _key=value_
> 持久地设置一个配置项。

**-d**, **--directory** _path_
> 操作指定的缓存目录而非默认目录。

**--cleanup**
> 清理缓存使其保持在大小限制内。

**--evict-older-than** _age_
> 删除早于指定时间的文件（例如 30d、24h）。

**-V**, **--version**
> 显示版本。

# SETUP

**符号链接方法：**
```
ln -s /usr/bin/ccache /usr/local/bin/gcc
ln -s /usr/bin/ccache /usr/local/bin/g++
```

**环境变量方法：**
```
export CC="ccache gcc"
export CXX="ccache g++"
```

# CONFIGURATION

**~/.config/ccache/ccache.conf**
> 主配置文件，控制缓存大小、压缩、编译器设置和远程存储。

**/etc/ccache.conf**
> 系统级配置默认值。

# ENVIRONMENT

**CCACHE_DIR**
> 缓存目录路径（默认：~/.cache/ccache 或 ~/.ccache）。

**CCACHE_CONFIGPATH**
> 配置文件的路径。

**CCACHE_MAXSIZE**
> 最大缓存大小（覆盖配置文件）。

**CCACHE_DISABLE** / **CCACHE_NODISABLE**
> 禁用或重新启用 ccache。

# REMOTE CACHING

支持通过 HTTP、Redis 或 NFS 进行远程缓存，便于在多台构建机器之间共享。

# CAVEATS

只缓存单文件编译。多文件编译和链接会回退到真实编译器。其输出与直接编译完全一致。预编译头文件需要特殊配置。

# INSTALL

```apt: sudo apt install ccache```

```dnf: sudo dnf install ccache```

```pacman: sudo pacman -S ccache```

```apk: sudo apk add ccache```

```zypper: sudo zypper install ccache```

```brew: brew install ccache```

```nix: nix profile install nixpkgs#ccache```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gcc](/man/gcc)(1), [clang](/man/clang)(1), [make](/man/make)(1), [distcc](/man/distcc)(1), [sccache](/man/sccache)(1), [cmake](/man/cmake)(1)
