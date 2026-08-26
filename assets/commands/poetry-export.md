# TAGLINE

将 Poetry 依赖导出为其他格式

# TLDR

**导出为 requirements.txt**

```poetry export -f requirements.txt -o requirements.txt```

**导出时包含开发依赖**

```poetry export --with dev -f requirements.txt```

**导出时不带哈希**

```poetry export --without-hashes -o requirements.txt```

**仅导出特定的依赖组**

```poetry export --only [main,docs] -f requirements.txt```

**导出到标准输出**

```poetry export -f requirements.txt```

**导出时包含 extras**

```poetry export -f requirements.txt -E [extra_name]```

# SYNOPSIS

**poetry** **export** [_options_]

# PARAMETERS

**-f**, **--format** _format_
> 输出格式（requirements.txt、constraints.txt、pylock.toml）。

**-o**, **--output** _file_
> 输出文件路径。省略时打印到标准输出。

**--with** _groups_
> 包含可选依赖组。

**--without** _groups_
> 排除依赖组。

**--only** _groups_
> 仅包含指定的依赖组。

**--without-hashes**
> 输出中排除哈希。

**--without-urls**
> 输出中排除源 URL。

**-E**, **--extras** _extras_
> 包含 extras。

# DESCRIPTION

**poetry export** 将锁文件导出为其他格式。它由 **poetry-plugin-export** 插件提供。主要用于生成 requirements.txt 文件，供不直接使用 Poetry 的环境使用，例如 Docker 构建或生产部署。

# CAVEATS

需要安装 **poetry-plugin-export** 插件。`--dev` 标志已被弃用，建议改用 `--with dev`。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry](/man/poetry)(1), [poetry-lock](/man/poetry-lock)(1), [poetry-install](/man/poetry-install)(1), [pip](/man/pip)(1)
