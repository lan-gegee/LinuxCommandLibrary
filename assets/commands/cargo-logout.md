# TAGLINE

删除已保存的注册表 API 令牌

# TLDR

**从 crates.io 登出**

```cargo logout```

**从指定注册表登出**

```cargo logout --registry [my-registry]```

# SYNOPSIS

**cargo logout** [_options_]

# DESCRIPTION

**cargo logout** 从本地存储中删除注册表的 API 令牌，即撤销 cargo login 保存的令牌。

# PARAMETERS

**--registry** _name_
> 要登出的注册表（默认：crates-io）

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制输出

# BEHAVIOR

从 ~/.cargo/credentials.toml 中删除指定注册表的令牌条目。不会在服务器端撤销该令牌。

# CAVEATS

要完全吊销访问权限，还需在注册表网站上重新生成令牌（crates.io 对应 https://crates.io/me）。此命令只删除本地凭据。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-login](/man/cargo-login)(1), [cargo-publish](/man/cargo-publish)(1)

# RESOURCES

```[Source code](https://github.com/rust-lang/cargo)```

```[Documentation](https://doc.rust-lang.org/cargo/commands/cargo-logout.html)```

<!-- verified: 2026-06-22 -->
