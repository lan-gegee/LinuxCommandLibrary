# TAGLINE

Exercism 编程练习平台的 CLI 工具

# TLDR

**使用令牌进行配置**

```exercism configure --token=[your_token]```

**下载练习题**

```exercism download --track=[python] --exercise=[hello-world]```

**提交解答**

```exercism submit [solution.py]```

**列出可用的语言赛道**

```exercism tracks```

**显示工作区路径**

```exercism workspace```

**在浏览器中打开练习**

```exercism open [path/to/exercise]```

# SYNOPSIS

**exercism** _command_ [_options_]

# PARAMETERS

**configure**
> 使用 API 令牌配置 CLI。

**download**
> 下载练习题。

**submit**
> 提交解答以供评审。

**tracks**
> 列出可用的语言赛道。

**workspace**
> 显示工作区目录。

**open**
> 在浏览器中打开练习。

**--track** _name_
> 编程语言赛道。

**--exercise** _name_
> 练习名称。

**--token** _token_
> 用于认证的 API 令牌。

**--force**
> 覆盖已存在的文件。

# DESCRIPTION

**exercism** 是 Exercism 的命令行工具。Exercism 是一个通过练习学习编程语言的平台。该 CLI 用于下载练习、提交解答并管理本地工作区。

它与 Exercism 网站集成，让你可以结合导师反馈反复打磨练习。它支持数十种编程语言赛道。

# CONFIGURATION

**~/.config/exercism/user.json**
> 存储 API 令牌、工作区路径和用户偏好。

# CAVEATS

需要 Exercism 账户和 API 令牌。下载时需要联网。应正确配置工作区路径。部分练习要求特定的语言版本。

# HISTORY

**Exercism** 由 **Katrina Owen** 于 **2013 年**创立，是一个刻意练习编程的平台。CLI 让你可以在离线状态下完成练习，并与 Web 平台集成以便提交和获得导师指导。

# INSTALL

```dnf: sudo dnf install exercism```

```brew: brew install exercism```

```nix: nix profile install nixpkgs#exercism```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git](/man/git)(1), [npm](/man/npm)(1), [pip](/man/pip)(1)

# RESOURCES

```[Source code](https://github.com/exercism/cli)```

```[Homepage](https://exercism.org/)```

<!-- verified: 2026-07-15 -->
