# TAGLINE

保存用于认证的注册表 API 令牌

# TLDR

**登录 crates.io**（令牌从标准输入读取）

```cargo login```

**以参数形式提供令牌登录**

```cargo login [token]```

**登录指定的注册表**

```cargo login --registry [my-registry]```

# SYNOPSIS

**cargo login** [_options_] [_token_]

# DESCRIPTION

**cargo login** 运行一个凭据提供程序来保存用于注册表认证的令牌。使用 `cargo publish` 发布 crate 时必须先登录。令牌从标准输入读取。默认情况下，令牌存储在 `$CARGO_HOME/credentials.toml` 中。

对于 crates.io，可在 https://crates.io/me 获取你的令牌

# PARAMETERS

**--registry** _name_
> 要认证的注册表（默认：crates-io）

**-v**, **--verbose**
> 详细输出。指定两次可获得更多细节。

**-q**, **--quiet**
> 抑制输出。

**--color** _when_
> 控制彩色输出（auto、always、never）。

**--config** _KEY=VALUE_
> 覆盖某个 Cargo 配置项。

# TOKEN STORAGE

**默认位置**
> ~/.cargo/credentials.toml

**格式**
```toml
[registry]
token = "your-api-token"
```

# CREDENTIAL PROVIDERS

在 ~/.cargo/config.toml 中配置：

```toml
[registry]
global-credential-providers = [
    "cargo:token",
    "cargo:libsecret",
    "cargo:macos-keychain",
    "cargo:wincred"
]
```

# ENVIRONMENT

**CARGO_REGISTRIES_<NAME>_TOKEN**
> 通过环境变量提供令牌

**CARGO_REGISTRY_TOKEN**
> 默认注册表的令牌

# CAVEATS

务必保管好令牌。cargo:token 提供程序以未加密方式存储令牌。如需更高的安全性，请使用系统钥匙串提供程序。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-publish](/man/cargo-publish)(1), [cargo-logout](/man/cargo-logout)(1)
