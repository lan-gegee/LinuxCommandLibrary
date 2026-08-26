# TAGLINE

在命令行中管理 GitHub 组织信息

# TLDR

**列出组织**

```gh org list```

**查看组织**

```gh org view [orgname]```

**列出组织成员**

```gh api orgs/[orgname]/members```

# SYNOPSIS

**gh org** _command_ [_options_]

# PARAMETERS

**list**
> 列出你所属的组织。

**view** _ORGNAME_
> 查看组织详情。

**--help**
> 显示帮助信息。

# DESCRIPTION

**gh org** 用于在命令行中管理 GitHub 组织信息。它可以查看你所属组织的成员关系、详情和设置。

该命令让你无需访问 github.com 即可查看组织信息。对于团队操作、成员管理等更复杂的组织管理任务，可使用 **gh api** 命令获得完整的 API 访问能力。

# CAVEATS

可用操作取决于你在组织中的角色。部分功能需要管理员权限。完整的组织管理可能需要借助 gh api。

# HISTORY

gh org 被加入 **GitHub CLI** 以提供基础的组织命令，补充其仓库和用户管理功能。

# INSTALL

```apt: sudo apt install gh```

```dnf: sudo dnf install gh```

```pacman: sudo pacman -S github-cli```

```apk: sudo apk add github-cli```

```zypper: sudo zypper install gh```

```brew: brew install gh```

```nix: nix profile install nixpkgs#gh```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-repo](/man/gh-repo)(1)

# RESOURCES

```[Documentation](https://cli.github.com/manual/gh_org)```

```[Source code](https://github.com/cli/cli)```

<!-- verified: 2026-07-15 -->
