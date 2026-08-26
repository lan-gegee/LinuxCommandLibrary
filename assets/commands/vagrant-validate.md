# TAGLINE

校验 Vagrantfile 语法

# TLDR

**校验当前目录中的 Vagrantfile**

```vagrant validate```

**校验时忽略提供者特定的配置**

```vagrant validate -p```

# SYNOPSIS

**vagrant** **validate** [_options_]

# PARAMETERS

**-p**, **--ignore-provider**
> 校验期间忽略提供者特定的配置选项。

# DESCRIPTION

**vagrant validate** 检查 Vagrantfile 是否存在语法错误。它在不创建或修改机器的情况下校验配置，因此适用于 CI/CD 流水线和提交前检查。若配置有效，它会打印 "Vagrantfile validated successfully."。

# INSTALL

```apt: sudo apt install vagrant```

```dnf: sudo dnf install vagrant```

```nix: nix profile install nixpkgs#vagrant```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[vagrant](/man/vagrant)(1), [vagrant-init](/man/vagrant-init)(1)
