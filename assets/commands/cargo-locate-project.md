# TAGLINE

输出项目 Cargo.toml 的路径

# TLDR

**显示清单路径**

```cargo locate-project```

**显示工作空间根清单**

```cargo locate-project --workspace```

**以纯路径输出**

```cargo locate-project --message-format plain```

**以 JSON 输出**

```cargo locate-project --message-format json```

**从指定目录定位项目**

```cargo locate-project --manifest-path [path/to/Cargo.toml]```

# SYNOPSIS

**cargo locate-project** [_options_]

# DESCRIPTION

**cargo locate-project** 输出当前软件包的 Cargo.toml 清单文件路径。它会从当前目录开始向上层目录搜索清单文件。

# PARAMETERS

**--workspace**
> 定位工作空间根目录的 Cargo.toml 而非当前软件包

**--message-format** _format_
> 输出格式：json（默认）、plain

**--manifest-path** _path_
> Cargo.toml 的路径

**-v**, **--verbose**
> 详细输出

**-q**, **--quiet**
> 抑制日志消息

**--color** _WHEN_
> 控制彩色输出：auto、always、never

# OUTPUT

**JSON 格式（默认）**
```json
{"root":"/path/to/project/Cargo.toml"}
```

**Plain 格式**
```
/path/to/project/Cargo.toml
```

# EXIT STATUS

**0**
> 成功

**101**
> 未能找到清单

# CAVEATS

适用于需要查找项目根目录的脚本和工具。若当前及所有父目录中都找不到 Cargo.toml，则返回退出码 101。

# INSTALL

```apt: sudo apt install cargo```

```dnf: sudo dnf install cargo```

```apk: sudo apk add cargo```

```zypper: sudo zypper install cargo```

```nix: nix profile install nixpkgs#cargo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cargo](/man/cargo)(1), [cargo-metadata](/man/cargo-metadata)(1), [cargo-pkgid](/man/cargo-pkgid)(1)
