# TAGLINE

从其他包管理器迁移到 Bun

# TLDR

**从 npm/yarn/pnpm 迁移**到 Bun

```bun pm migrate```

**强制迁移**（当 bun.lock 已存在时）

```bun pm migrate --force```

# SYNOPSIS

**bun** **pm** **migrate** [_options_]

# DESCRIPTION

**bun pm migrate** 将使用 npm、yarn 或 pnpm 的项目转换为使用 Bun 的包管理器。它会读取现有的 lockfile（package-lock.json、yarn.lock 或 pnpm-lock.yaml）并创建 bun.lock 文件，保留原 lockfile 中已解析的依赖版本。

注意 `bun install` 在没有 bun.lock 时也会执行自动的 lockfile 迁移，因此该命令主要用于在不安装软件包的情况下进行显式的一次性迁移。

# PARAMETERS

**-f**, **--force**
> 覆盖已存在的 bun.lock 文件。

# CAVEATS

请检查生成的 bun.lock 以确保依赖解析结果符合预期。某些复杂依赖树的边缘情况可能需要手动调整。原 lockfile 会被保留，可在验证后手动删除。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-pm](/man/bun-pm)(1), [bun-install](/man/bun-install)(1), [npm](/man/npm)(1), [yarn](/man/yarn)(1), [pnpm](/man/pnpm)(1)
