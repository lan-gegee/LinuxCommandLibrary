# TAGLINE

生成并输出 lockfile 的哈希值

# TLDR

**输出当前 lockfile 的哈希值**

```bun pm hash```

**输出用于计算 lockfile 哈希的字符串**

```bun pm hash-string```

**输出当前 lockfile 中存储的哈希值**

```bun pm hash-print```

# SYNOPSIS

**bun** **pm** **hash** | **hash-string** | **hash-print**

# DESCRIPTION

**bun pm hash** 生成并显示当前 lockfile（bun.lock）的哈希值。这可用于缓存失效判断、CI 流水线，以及验证依赖在多次运行之间是否发生了变化。

相关的子命令 **hash-string** 和 **hash-print** 提供更多信息：**hash-string** 输出送入哈希函数的原始字符串，而 **hash-print** 读取并显示已存储在 lockfile 中的哈希值，无需重新计算。

# CAVEATS

哈希是根据 lockfile 内容计算的，因此任何手动编辑都会改变哈希值，即使实际的依赖树并未改变。该命令要求项目中存在有效的 lockfile；如果缺失，请先运行 **bun install**。Bun 1.2 之前的版本使用二进制 lockfile 格式（bun.lockb）；较新的版本使用基于文本的 bun.lock 格式。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-pm](/man/bun-pm)(1), [bun-install](/man/bun-install)(1)
