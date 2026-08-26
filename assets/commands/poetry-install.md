# TAGLINE

从锁文件安装项目依赖

# TLDR

**安装所有依赖**

```poetry install```

**不安装开发依赖**

```poetry install --without dev```

**仅安装特定的组**

```poetry install --only main,test```

**带 extras 安装**

```poetry install --extras "[extra1 extra2]"```

**完全同步环境**

```poetry install --sync```

# SYNOPSIS

**poetry install** [_options_]

# PARAMETERS

**--without** _groups_
> 排除依赖组。

**--only** _groups_
> 仅安装这些组。

**--extras**, **-E** _extras_
> 安装 extras。

**--sync**
> 同步环境（移除未列出的内容）。

**--no-root**
> 不安装项目本身。

**--dry-run**
> 显示将要安装的内容。

**-v**, **-vv**, **-vvv**
> 详细程度级别。

# DESCRIPTION

**poetry install** 读取 pyproject.toml 和 poetry.lock 来安装项目依赖。它会在需要时创建虚拟环境，确保安装的可复现性。

# EXAMPLES

```bash
# Install everything
poetry install

# Production only
poetry install --without dev,test

# Only dev dependencies
poetry install --only dev

# Don't install the project itself
poetry install --no-root

# Synchronize (remove extras)
poetry install --sync

# Dry run
poetry install --dry-run
```

# LOCK FILE

- poetry.lock ensures reproducible installs
- Generated on first install
- Updated by poetry lock or poetry update

# CAVEATS

需要 pyproject.toml。默认会创建虚拟环境。使用 --sync 可与锁文件完全一致。

# HISTORY

poetry install 是 **Sébastien Eustace** 的 **Poetry** 的一部分，提供确定性的 Python 依赖安装。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry-add](/man/poetry-add)(1), [poetry-update](/man/poetry-update)(1), [poetry-lock](/man/poetry-lock)(1)
