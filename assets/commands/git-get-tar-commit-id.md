# TAGLINE

从 tar 归档中提取提交 ID

# TLDR

**从归档中提取提交 ID**

```git get-tar-commit-id < [archive.tar]```

# SYNOPSIS

**git** **get-tar-commit-id** < _archive_

# DESCRIPTION

**git get-tar-commit-id** 从由 git archive 创建的 tar 归档中提取提交 ID。提交 ID 在生成归档时被存储于归档的 pax 扩展头中。

该命令从 stdin 读取输入，如果找到则输出 40 字符的 SHA-1 哈希。它对于分发归档且需要验证源码版本的构建系统特别有用。该命令只对由 git archive 创建的归档有效，因为标准 tar 归档不包含 git 元数据。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-archive](/man/git-archive)(1)

# RESOURCES

```[Source code](https://github.com/git/git)```

```[Homepage](https://git-scm.com/)```

```[Documentation](https://git-scm.com/docs/git-get-tar-commit-id)```

<!-- verified: 2026-07-17 -->
