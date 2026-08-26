# TAGLINE

管理 Bun 的全局软件包缓存

# TLDR

**输出** Bun 全局模块缓存的路径

```bun pm cache```

**清空**整个全局模块缓存

```bun pm cache rm```

# SYNOPSIS

**bun pm cache** [**rm**]

# DESCRIPTION

**bun pm cache** 管理 Bun 的全局模块缓存目录，所有从 npm 软件仓库下载的软件包都存储在那里。不带参数运行时会输出缓存目录的绝对路径。**rm** 子命令会删除整个缓存内容。

默认缓存位置是 **~/.bun/install/cache**，软件包存储在名为 **\${name}@\${version}** 的子目录中。当 **bun install** 运行时，它会先检查这个全局缓存，并通过硬链接、clonefile 或复制的方式使用缓存副本，而不是从网络获取。

缓存位置可以通过 **BUN_INSTALL_CACHE_DIR** 环境变量或 **bunfig.toml** 中的 **[install.cache]** 配置节来覆盖。

# CONFIGURATION

**bunfig.toml** 中的缓存设置

```
[install.cache]
dir = "~/.bun/install/cache"
disable = false
disableManifest = false
```

**dir** 设置自定义缓存目录。**disable** 阻止从全局缓存加载。**disableManifest** 强制从软件仓库解析最新版本。

# CAVEATS

没有选择性清除缓存的功能；**bun pm cache rm** 是全有或全无的操作，会移除整个全局缓存。要删除特定的软件包，需手动删除 **~/.bun/install/cache/\<package\>@\<version\>** 下对应的目录。历史上该命令要求在包含 **package.json** 的目录中运行，即使它操作的是全局缓存。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-pm-trust](/man/bun-pm-trust)(1), [npm-cache](/man/npm-cache)(1)
