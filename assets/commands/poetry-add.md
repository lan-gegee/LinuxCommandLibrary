# TAGLINE

向 Poetry 项目添加依赖

# TLDR

**添加依赖**

```poetry add [package]```

**添加特定版本**

```poetry add [package]@[1.0.0]```

**添加开发依赖**

```poetry add --group dev [package]```

**从 Git 添加**

```poetry add git+https://github.com/[user]/[repo].git```

**添加多个软件包**

```poetry add [package1] [package2]```

# SYNOPSIS

**poetry add** [_options_] _packages_...

# PARAMETERS

**--group**, **-G** _group_
> 将软件包加入的依赖组（如 dev、test）。

**--dev**, **-D**
> `--group dev` 的简写。

**--optional**
> 作为可选依赖（extra）添加。

**--dry-run**
> 输出将要执行的操作而不实际执行。

**--editable**, **-e**
> 将 vcs/path 依赖以可编辑模式添加。

**--extras**, **-E** _extras_
> 为该依赖激活的 extras（允许多个值）。

**--source** _source_
> 用于安装该软件包的源名称。

**--python** _version_
> 须安装该依赖的 Python 版本约束。

**--platform** _platform_
> 须安装该依赖的平台。

**--markers** _markers_
> 描述何时应安装该依赖的环境标记。

**--allow-prereleases**
> 接受预发布版本。

**--lock**
> 不执行安装；仅更新锁文件。

# DESCRIPTION

**poetry add** 向 pyproject.toml 添加依赖并进行安装。它会自动解析版本约束并更新锁文件。

# EXAMPLES

```bash
# Add latest version
poetry add requests

# Add with version constraint
poetry add "django>=4.0"

# Add dev dependency
poetry add --group dev pytest

# Add from git branch
poetry add git+https://github.com/user/repo.git#branch

# Add with extras
poetry add fastapi --extras all

# Add local package
poetry add ../my-package --editable
```

# VERSION CONSTRAINTS

```
package         - Latest
package@1.0.0   - Exact version
package@^1.0    - Compatible (>=1.0 <2.0)
package@~1.0    - Approximately (>=1.0 <1.1)
```

# CAVEATS

会修改 pyproject.toml 和 poetry.lock。使用 --dry-run 可预览更改。

# HISTORY

poetry add 是 **Poetry** 的一部分，Poetry 是由 **Sébastien Eustace** 创建的 Python 依赖管理器。

# INSTALL

```dnf: sudo dnf install poetry```

```apk: sudo apk add poetry```

```brew: brew install poetry```

```nix: nix profile install nixpkgs#poetry```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[poetry-remove](/man/poetry-remove)(1), [poetry-install](/man/poetry-install)(1), [poetry](/man/poetry)(1)
