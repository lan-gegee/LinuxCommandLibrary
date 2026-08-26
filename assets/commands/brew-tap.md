# TAGLINE

向 Homebrew 添加第三方软件仓库

# TLDR

**列出所有已添加的仓库**

```brew tap```

从 GitHub **添加**仓库

```brew tap [user]/[repo]```

从自定义 URL 添加仓库

```brew tap [user]/[repo] [https://example.com/repo.git]```

**移除**已添加的仓库

```brew untap [user]/[repo]```

用模板创建新 tap

```brew tap-new [user]/[repo]```

# SYNOPSIS

**brew tap** [_user/repo_] [_url_]

# DESCRIPTION

**brew tap** 向 Homebrew 添加第三方仓库，将可用的 formula 和 cask 扩展到核心仓库之外。已添加的仓库会在运行 **brew update** 时自动更新。

默认情况下，tap 假定使用 GitHub 仓库，但也可以指定任意 Git URL。

# USAGE

**brew tap**
> 列出当前所有已添加的仓库。

**brew tap user/repo**
> 克隆 https://github.com/user/homebrew-repo。

**brew tap user/repo URL**
> 从自定义 URL 克隆仓库。

# REPOSITORY NAMING

要使用简写形式，GitHub 仓库名必须为 **homebrew-something**。需要时会自动添加该前缀：

- **brew tap user/foobar** 会克隆 **user/homebrew-foobar**

# INSTALLING FROM TAPS

添加之后即可直接安装 formula：

```brew install formula```

显式指定 tap 来源：

```brew install user/repo/formula```

# PARAMETERS

**--full**
> 以完整 Git 仓库形式克隆（支持 git 操作）。

**--force-auto-update**
> 即使不来自 GitHub 也自动更新。

**--shallow**
> 使用浅克隆（shallow clone）。

# CAVEATS

tap 的 formula 会随 **brew update** 自动更新。当核心仓库与 tap 中存在同名 formula 时，除非使用全限定名，否则以核心仓库优先。私有仓库需要身份验证。

# SEE ALSO

[brew](/man/brew)(1), [brew-update](/man/brew-update)(1), [brew-install](/man/brew-install)(1)

# RESOURCES

```[Source code](https://github.com/Homebrew/brew)```

```[Homepage](https://brew.sh)```

```[Documentation](https://docs.brew.sh)```

<!-- verified: 2026-06-22 -->
