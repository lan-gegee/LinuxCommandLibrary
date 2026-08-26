# TAGLINE

输出完整限定的软件包标识

# TLDR

**显示当前软件包的包 ID**

```cargo pkgid```

**显示某个依赖的包 ID**

```cargo pkgid [serde]```

**显示某依赖特定版本的包 ID**

```cargo pkgid [serde@1.0.0]```

**使用指定的 Cargo.toml 显示包 ID**

```cargo pkgid --manifest-path [path/to/Cargo.toml] [serde]```

**从 URL 显示包 ID**

```cargo pkgid [https://github.com/rust-lang/crates.io-index#serde]```

# SYNOPSIS

**cargo pkgid** [_options_] [_spec_]

# DESCRIPTION

**cargo pkgid** 输出依赖图中某个软件包的完整限定包 ID 标识。输出的规范格式包括源 URL、软件包名称和版本，可与其他 Cargo 命令（如 `cargo update -p`）配合使用。

当依赖树中存在同一软件包的多个版本、需要消歧时，此命令最为有用。它接受部分形式的标识（如仅名称或名称加版本），并根据锁文件进行解析。使用此命令前必须存在 Cargo.lock 文件且依赖已获取。

# PARAMETERS

**-p**, **--package** _spec_
> 要查询的软件包

**--manifest-path** _path_
> Cargo.toml 的路径

**--locked**
> 断言使用的依赖及版本与生成现有 Cargo.lock 时完全一致

**--offline**
> 阻止 Cargo 访问网络

**--frozen**
> 等价于同时指定 --locked 和 --offline

**--color** _when_
> 控制彩色输出：auto（默认）、always 或 never

**-v**, **--verbose**
> 详细输出。指定两次可获得非常详细的输出。

**-q**, **--quiet**
> 不打印 cargo 日志消息

# SPEC FORMATS

**name**
> bitflags

**name@version**
> bitflags@1.0.4

**url**
> https://github.com/rust-lang/cargo

**url#version**
> https://github.com/rust-lang/cargo#0.33.0

**url#name**
> https://github.com/rust-lang/crates.io-index#bitflags

**url#name@version**
> https://github.com/rust-lang/cargo#crates-io@0.21.0

# FULL SPEC FORMAT

```
registry+https://github.com/rust-lang/crates.io-index#regex@1.4.3
```

# CAVEATS

标识有歧义时会报错。存在多个版本时可添加版本限定符来消歧。需要锁文件且依赖已获取。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-metadata](/man/cargo-metadata)(1)
