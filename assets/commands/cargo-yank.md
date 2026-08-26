# TAGLINE

从注册表中撤回（yank）已推送的 crate 版本

# TLDR

**从注册表撤回某版本**

```cargo yank [crate@1.0.0]```

**使用版本标志撤回**

```cargo yank --version [1.0.0] [crate]```

**撤销撤回**

```cargo yank --undo [crate@1.0.0]```

**从其他注册表撤回**

```cargo yank --registry [my-registry] [crate@1.0.0]```

# SYNOPSIS

**cargo yank** [_options_] _crate_@_version_
**cargo yank** [_options_] --version _version_ [_crate_]

# DESCRIPTION

**cargo yank** 在注册表上将某个 crate 版本标记为已撤回。被撤回的版本不能作为新依赖使用，但已有的 Cargo.lock 文件仍可继续工作。它不会删除数据。

需要先通过 cargo login 进行身份验证。

# PARAMETERS

**--version** _version_
> 要撤回的版本

**--undo**
> 恢复被撤回的版本

**--registry** _name_
> 目标注册表

**--index** _url_
> 注册表索引 URL

**--token** _token_
> API 令牌

**-h**, **--help**
> 打印帮助信息

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制输出

**--color** _WHEN_
> 着色：auto、always、never

# BEHAVIOR

**被撤回的版本**
- 不能作为新依赖添加
- 已有 Cargo.lock 中的引用仍然有效
- 不会从注册表中删除

# WHEN TO YANK

- 意外发布
- 无意的语义化版本破坏
- 功能严重损坏
- 安全问题（建议改用 RustSec）

# BEST PRACTICE

在撤回损坏版本（1.5.0）之前，先发布修复后的版本（例如 1.5.1）。

# CAVEATS

crates.io 是永久归档；撤回只是将版本标记为不可用，并不会删除。对于安全问题，RustSec 公告的影响更小。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-publish](/man/cargo-publish)(1), [cargo-owner](/man/cargo-owner)(1)
