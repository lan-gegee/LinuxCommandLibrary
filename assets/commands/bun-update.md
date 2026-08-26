# TAGLINE

更新已安装的软件包

# TLDR

**将所有软件包更新**到最新的兼容版本

```bun update```

**更新特定软件包**

```bun update [package]```

**忽略 semver 范围**更新到最新版本

```bun update --latest```

# SYNOPSIS

**bun** **update** [_options_] [_packages..._]

# PARAMETERS

**--latest**
> 更新到最新版本，忽略 package.json 中的版本范围（同时重写清单文件）。

**--no-save**
> 更新已安装的软件包，但不修改 `package.json` 或 `bun.lockb`。

**--save-text-lockfile**
> 在二进制 lockfile 之外生成人类可读的 `bun.lock` 文本 lockfile。

**-d**, **--dev**
> 将更新限制在 `devDependencies`。

**--production**
> 将更新限制在非 dev 依赖。

**--frozen-lockfile**
> 如果 lockfile 需要变更则失败（CI 安全检查）。

**--dry-run**
> 显示将要发生的更改，而不写入磁盘。

# DESCRIPTION

**bun update** 将已安装的软件包升级到更新的版本，并刷新 `node_modules` 和 lockfile。默认它会遵循 `package.json` 中声明的 semver 范围；**--latest** 会解除该限制，并将最新的可用版本写回清单文件。

不带软件包名称调用时，会考虑所有依赖。指定一个或多个软件包则将操作限制在这些条目（及其传递依赖图）上。

# CAVEATS

**--latest** 可能引入主版本升级并破坏项目。二进制的 `bun.lockb` 不便于人工比对；请使用 `--save-text-lockfile`（或 `bun install --save-text-lockfile`）维护一个 `bun.lock` 文件以便代码审查。

# INSTALL

```pacman: sudo pacman -S bun```

```brew: brew install bun```

```nix: nix profile install nixpkgs#bun```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bun](/man/bun)(1), [bun-outdated](/man/bun-outdated)(1), [bun-install](/man/bun-install)(1)
