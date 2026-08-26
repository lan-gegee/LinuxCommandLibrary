# TAGLINE

检查 Cargo.toml 清单的正确性

# TLDR

**校验当前项目的清单**

```cargo verify-project```

**校验指定清单**

```cargo verify-project --manifest-path [path/to/Cargo.toml]```

**在依赖锁定状态下校验**

```cargo verify-project --locked```

**离线校验**（不访问网络）

```cargo verify-project --frozen```

# SYNOPSIS

**cargo verify-project** [_options_]

# DESCRIPTION

**cargo verify-project** 解析并验证本地 Cargo.toml 清单文件。它输出一个 JSON 对象，指示清单在语法上是否正确且包含所有必需字段，失败时附带错误详情。

该命令适用于 CI/CD 流水线和 pre-commit 钩子，以便尽早发现清单错误。它检查语法正确性、有效的依赖声明、规范的元数据格式以及必需字段。它不会验证依赖是否真的存在于注册表中，只检查清单本身格式是否良好。清单有效时退出状态为 0，无效时为 1。

# PARAMETERS

**--manifest-path** _path_
> Cargo.toml 文件的路径。

**--locked**
> 断言 Cargo.lock 是最新的。

**--frozen**
> 断言 Cargo.lock 是最新的，并禁止访问网络。

**--offline**
> 不访问网络运行。

**-v**, **--verbose**
> 使用详细输出。

**-q**, **--quiet**
> 抑制 cargo 的输出消息。

**--config** _KEY=VALUE_
> 覆盖某个 Cargo 配置项。

**-C** _path_
> 执行前先切换到指定目录。

# OUTPUT

**成功**
```json
{"success":"true"}
```

**失败**
```json
{"invalid":"error message"}
```

# EXIT STATUS

**0**
> 清单有效。

**1**
> 清单无效。

# CAVEATS

不验证依赖是否真的存在于注册表中，只检查清单语法是否良好。适用于 CI/CD 流水线和 pre-commit 钩子。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-check](/man/cargo-check)(1)
