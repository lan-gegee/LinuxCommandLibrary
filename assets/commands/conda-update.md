# TAGLINE

软件包更新器

# TLDR

**更新所有软件包**

```conda update --all```

**更新指定软件包**

```conda update [package_name]```

**更新 conda 自身**

```conda update conda```

**在指定环境中更新**

```conda update -n [env_name] [package_name]```

**免确认更新**

```conda update -y [package_name]```

# SYNOPSIS

**conda** **update** [_options_] [_packages..._]

# PARAMETERS

**--all**
> 更新所有已安装的软件包。

**-n**, **--name** _name_
> 在具名环境中更新。

**-c**, **--channel** _channel_
> 搜索时使用的附加频道。

**-y**, **--yes**
> 不请求确认。

**--update-deps**
> 更新依赖。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda update** 将软件包更新到最新的兼容版本。它会遵循现有的软件包约束，并可能按需更新依赖。

# CAVEATS

若存在相互冲突的软件包需求，**--all** 可能失败。这种情况下请逐个更新软件包。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-install](/man/conda-install)(1), [conda-list](/man/conda-list)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Homepage](https://docs.conda.io)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/index.html)```

<!-- verified: 2026-06-23 -->
