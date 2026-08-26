# TAGLINE

在注册表中搜索 crate

# TLDR

**搜索 crate**

```cargo search [serde]```

**返回更多搜索结果**

```cargo search [async] --limit [50]```

**搜索指定注册表**

```cargo search [package] --registry [my-registry]```

# SYNOPSIS

**cargo search** [_options_] [_query_...]

# DESCRIPTION

**cargo search** 在 crates.io 或其他注册表上对 crate 进行文本搜索。结果以 TOML 兼容格式显示，包含软件包名称、最新版本和描述，便于直接复制到 Cargo.toml 的 dependencies 区块中。

默认最多返回 10 条结果，按相关性排序。`--limit` 标志最多可将此数值提高到 100。如需更高级的浏览方式，crates.io 网站或 `cargo-seek` 等工具提供更丰富的过滤和分类功能。

# PARAMETERS

**--limit** _n_
> 结果数量（默认：10，最大：100）

**--registry** _name_
> 要搜索的注册表

**--index** _url_
> 注册表索引 URL

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制输出

**--color** _when_
> 彩色输出：auto、always、never。

**--config** _KEY=VALUE_
> 覆盖 Cargo 配置项。

**--frozen**, **--locked**, **--offline**
> 网络/锁文件行为；**--offline** 会阻止 Cargo 联系注册表索引。

# OUTPUT FORMAT

结果显示软件包名称、版本和描述：

```
serde = "1.0.130"     # A generic serialization/deserialization framework
serde_json = "1.0.68" # JSON serialization format
```

# CAVEATS

默认搜索 crates.io。若需要交互式 TUI 搜索，可考虑 cargo-seek。结果按相关性排序。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-add](/man/cargo-add)(1), [cargo-info](/man/cargo-info)(1)
