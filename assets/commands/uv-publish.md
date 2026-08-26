# TAGLINE

将 Python 软件包发布到 PyPI

# TLDR

将 dist/ 中的所有发行版**发布**到 PyPI

```uv publish```

**发布到 TestPyPI**

```uv publish --publish-url https://test.pypi.org/legacy/```

使用 pyproject.toml 中命名的索引来**发布**

```uv publish --index [name]```

使用 API 令牌**发布**

```uv publish --token [pypi-token]```

**发布指定文件**

```uv publish [dist/package-1.0.tar.gz] [dist/package-1.0-py3-none-any.whl]```

**发布**并跳过已上传的文件

```uv publish --check-url https://pypi.org/simple/```

# SYNOPSIS

**uv** **publish** [_options_] [_files_...]

# PARAMETERS

**--publish-url** _url_
> 目标软件仓库上传端点的 URL。

**--index** _name_
> 发布到 pyproject.toml 中配置的命名索引。

**--token** _token_
> 身份验证令牌（如 PyPI API 令牌）。环境变量：UV_PUBLISH_TOKEN。

**--username** _user_
> 软件仓库用户名。环境变量：UV_PUBLISH_USERNAME。

**--password** _pass_
> 软件仓库密码。环境变量：UV_PUBLISH_PASSWORD。

**--check-url** _url_
> 用于检查已有软件包的索引 URL；跳过相同的上传并处理并行竞争。

**--trusted-publishing** _value_
> 配置可信发布（always、never）。支持 GitHub Actions 和 GitLab CI/CD。

**--keyring-provider** _provider_
> 使用 keyring 进行身份验证（subprocess）。

**--no-attestations**
> 禁用自动上传证明文件（attestation）。环境变量：UV_PUBLISH_NO_ATTESTATIONS。

# DESCRIPTION

**uv publish** 将 Python 软件包上传到 PyPI 或其他软件仓库。默认发布 dist/ 目录中找到的 wheel 和源代码发行版。支持通过 API 令牌、用户名/密码、可信发布（GitHub Actions、GitLab CI/CD）或 keyring 进行身份验证。

提供 **--check-url** 时，uv 会跳过与软件仓库中已有内容完全相同的文件，因此并行 CI 上传是安全的。

# SEE ALSO

[uv](/man/uv)(1), [uv-build](/man/uv-build)(1), [twine](/man/twine)(1), [pip](/man/pip)(1)
