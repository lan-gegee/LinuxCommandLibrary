# TAGLINE

将依赖导出为 requirements 格式

# TLDR

**导出为 requirements.txt 格式**

```uv export > requirements.txt```

**导出到指定文件**

```uv export --output-file [requirements.txt]```

**导出时不包含开发依赖**

```uv export --no-dev > requirements.txt```

**导出时不包含哈希值**

```uv export --no-hashes > requirements.txt```

**导出为 pylock.toml 格式（PEP 751）**

```uv export --format pylock.toml --output-file [pylock.toml]```

**导出为 CycloneDX SBOM**

```uv export --format cyclonedx1.5 --output-file [sbom.json]```

**导出脚本的依赖**

```uv export --script [script.py]```

# SYNOPSIS

**uv** **export** [_options_]

# PARAMETERS

**--format** _format_
> 输出格式：requirements.txt（默认）、pylock.toml 或 cyclonedx1.5。

**--locked**
> 导出前断言锁文件是最新的。

**--frozen**
> 导出时不更新锁文件。

**--no-dev**
> 排除开发依赖。

**--no-hashes**
> 输出中不包含哈希值。

**-o**, **--output-file** _file_
> 写入指定文件而不是标准输出。

**--script** _file_
> 导出 PEP 723 脚本的依赖。

# DESCRIPTION

**uv export** 将项目依赖导出为多种格式。默认格式是 requirements.txt，与 pip 兼容。它还支持 pylock.toml（PEP 751）以及用于安全审计与合规的 CycloneDX SBOM。对于不使用 uv 的部署环境非常有用。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [uv-lock](/man/uv-lock)(1), [uv-run](/man/uv-run)(1), [pip](/man/pip)(1)
