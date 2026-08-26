# TAGLINE

管理注册表上 crate 的所有者

# TLDR

**列出 crate 所有者**

```cargo owner --list [crate_name]```

**按用户名添加所有者**

```cargo owner --add [username] [crate_name]```

**移除所有者**

```cargo owner --remove [username] [crate_name]```

**添加 GitHub 团队作为所有者**

```cargo owner --add github:[org]:[team] [crate_name]```

# SYNOPSIS

**cargo owner** [_options_] [_crate_]

# DESCRIPTION

**cargo owner** 管理 crate 在 crates.io 或其他注册表上的所有者。所有者可以发布新版本、撤回（yank）已有发行版，以及添加或移除其他所有者。所有所有权变更都需要通过 API 令牌进行认证。

所有者分为两类：具名用户和团队。具名用户拥有完整权限，包括管理其他所有者；而团队只能发布和撤回版本。可以使用 `github:org:team` 语法添加 GitHub 团队作为所有者，但只有该团队的成员才能执行此操作。

# PARAMETERS

**-a**, **--add** _login_
> 添加用户或团队作为所有者

**-r**, **--remove** _login_
> 移除用户或团队的所有者身份

**-l**, **--list**
> 列出当前所有者

**--registry** _name_
> 要使用的注册表

**--index** _url_
> 注册表索引 URL

**--token** _token_
> 用于认证的 API 令牌

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制输出

# CONFIGURATION

**~/.cargo/credentials.toml**
> 存储用于注册表认证的 API 令牌。由 `cargo login` 创建。

# OWNER TYPES

**具名所有者（用户）**
> 完整权限：发布、撤回、添加/移除所有者

**团队所有者**
> 受限权限：仅能发布和撤回

# TEAM SYNTAX

```
github:organization:team-name
```

必须是该团队的成员才能添加它。

# ENVIRONMENT

**CARGO_REGISTRY_TOKEN**
> 用于认证的 API 令牌

# CAVEATS

只有现有的所有者才能修改所有权。用户必须已登录 crates.io。团队无法添加或移除其他所有者。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-publish](/man/cargo-publish)(1), [cargo-login](/man/cargo-login)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-owner.html)```

<!-- verified: 2026-06-22 -->
