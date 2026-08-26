# TAGLINE

将 Python 软件包上传到 PyPI

# TLDR

**上传软件包到 PyPI**

```twine upload dist/*```

**上传到 TestPyPI**

```twine upload --repository testpypi dist/*```

**附带凭据上传**

```twine upload -u [username] -p [password] dist/*```

**上传前检查软件包**

```twine check dist/*```

**上传指定文件**

```twine upload [dist/package-1.0.tar.gz]```

**以详细输出上传**

```twine upload --verbose dist/*```

# SYNOPSIS

**twine** [_upload_] [_check_] [_-r repository_] [_-u user_] [_options_] _files_

# PARAMETERS

**upload** _FILES_
> 上传软件包。

**check** _FILES_
> 检查软件包元数据。

**-r** _REPO_, **--repository** _REPO_
> 目标仓库（pypi、testpypi 或 URL）。

**--repository-url** _URL_
> 仓库 URL。

**-u** _USER_, **--username** _USER_
> 用户名。

**-p** _PASS_, **--password** _PASS_
> 密码。

**--non-interactive**
> 不提示输入凭据。

**-s**, **--sign**
> 使用 GPG 签名文件。

**-c** _FILE_, **--config-file** _FILE_
> 配置文件。

**--skip-existing**
> 跳过已上传的文件。

**--verbose**
> 详细输出。

# DESCRIPTION

**twine** 将 Python 软件包上传到 PyPI 和其他软件包索引。它是发布 Python 软件包的推荐工具。

dist 目录中的软件包文件（.tar.gz 和 .whl）会被上传。这些文件由 build 或 setuptools 等构建工具生成。

检查模式会在上传前验证软件包元数据，能发现会导致上传失败的常见问题。

TestPyPI 允许在不影响真实 PyPI 的情况下测试上传流程。可以从 TestPyPI 安装软件包来进行验证。

认证支持用户名/密码、API token 或 keyring 集成。出于安全考虑推荐使用 API token。

上传始终使用 HTTPS。早期的工具允许不安全的上传方式，twine 明确禁止了这种行为。

# CONFIGURATION

**~/.pypirc**
> PyPI、TestPyPI 及自定义索引的仓库凭据与 URL。

**TWINE_USERNAME**
> 存储认证用户名的环境变量。

**TWINE_PASSWORD**
> 存储认证密码或 API token 的环境变量。

# CAVEATS

PyPI 上的软件包名称是永久性的。版本号不能重复使用。凭据需要妥善保管。软件包必须通过校验。

# HISTORY

**Twine** 由 Python Packaging Authority 于 **2013 年**前后创建，用于取代 setuptools 中不安全的上传机制。它确保所有上传都使用 HTTPS。

# INSTALL

```dnf: sudo dnf install twine```

```pacman: sudo pacman -S twine```

```apk: sudo apk add twine```

```brew: brew install twine```

```nix: nix profile install nixpkgs#twine```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [build](/man/build)(1), [flit](/man/flit)(1)
