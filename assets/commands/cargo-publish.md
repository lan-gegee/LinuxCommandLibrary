# TAGLINE

将软件包上传到注册表

# TLDR

**发布到 crates.io**

```cargo publish```

**试运行而不上传**

```cargo publish --dry-run```

**不经验证发布**

```cargo publish --no-verify```

**允许未提交的更改**

```cargo publish --allow-dirty```

**发布到备用注册表**

```cargo publish --registry [my-registry]```

**发布指定软件包**

```cargo publish -p [crate_name]```

# SYNOPSIS

**cargo publish** [_options_]

# DESCRIPTION

**cargo publish** 将软件包上传到 crates.io 或其他注册表。它会创建 `.crate` 归档，验证归档能否成功构建，然后上传到注册表。需要认证，通常通过 `cargo login` 完成。

发布是永久性的，无法删除或覆盖。某个版本一旦发布，该确切的版本号就永远不能再次使用。`cargo yank` 命令可将某版本标记为弃用，阻止新项目依赖它，但对现有用户仍然可用。发布前，请确保 Cargo.toml 中的版本号已按 semver 惯例递增。

# PARAMETERS

**--dry-run**
> 执行各项检查但不上传

**--no-verify**
> 跳过构建验证

**--allow-dirty**
> 允许未提交的 VCS 更改

**--registry** _name_
> 目标注册表

**--index** _url_
> 注册表索引 URL

**--token** _token_
> API 令牌

**-p**, **--package** _spec_
> 要发布的软件包

**--target** _triple_
> 用于验证的构建目标

**-j**, **--jobs** _n_
> 并行任务数

**--features** _features_
> 为验证启用指定的特性

**--all-features**
> 启用所有特性

# CONFIGURATION

**~/.cargo/credentials.toml**
> 存储 crates.io 及其他注册表的 API 令牌。由 `cargo login` 创建。

# PREPARATION

1. 在 crates.io 创建账户
2. 验证邮箱地址
3. 生成 API 令牌
4. 运行 cargo login

# RELEASING NEW VERSIONS

1. 更新 Cargo.toml 中的版本号
2. 可选：运行 cargo package
3. 运行 cargo publish

# CAVEATS

发布不可撤销。使用 cargo yank 可将版本标记为弃用但无法删除。版本变更请遵循 semver。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-login](/man/cargo-login)(1), [cargo-package](/man/cargo-package)(1), [cargo-yank](/man/cargo-yank)(1)
