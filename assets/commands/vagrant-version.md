# TAGLINE

显示已安装的 Vagrant 版本并检查更新

# TLDR

**显示已安装的版本**并检查最新可用版本

```vagrant version```

**只显示已安装的版本**（简短形式）

```vagrant --version```

# SYNOPSIS

**vagrant** **version**

# DESCRIPTION

**vagrant version** 显示已安装的 Vagrant 版本，并通过网络请求检查最新的可用版本。它同时展示当前安装的版本和最新发布版本，便于了解是否有更新可用。

简短形式 **vagrant --version** 或 **vagrant -v** 只输出已安装的版本，不检查更新。

# CAVEATS

检查最新版本需要网络访问。在隔离（air-gapped）环境中更新检查可能失败。

# INSTALL

```apt: sudo apt install vagrant```

```dnf: sudo dnf install vagrant```

```nix: nix profile install nixpkgs#vagrant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vagrant](/man/vagrant)(1)
