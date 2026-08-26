# TAGLINE

软件包卸载器

# TLDR

**移除一个软件包**

```conda remove [package_name]```

**从指定环境中移除**

```conda remove -n [env_name] [package_name]```

**移除整个环境**

```conda remove -n [env_name] --all```

**移除多个软件包**

```conda remove [package1] [package2]```

**免确认移除**

```conda remove -y [package_name]```

# SYNOPSIS

**conda** **remove** [_options_] [_packages..._]

# PARAMETERS

**-n**, **--name** _name_
> 从具名环境中移除。

**--all**
> 移除整个环境。

**-y**, **--yes**
> 不请求确认。

**--force**
> 强制移除，不做依赖检查。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda remove** 从 conda 环境中卸载软件包。配合 **--all** 则移除整个环境。

不再需要的依赖可能会残留；可用 **conda clean** 清除它们。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-install](/man/conda-install)(1), [conda-clean](/man/conda-clean)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/remove.html)```

<!-- verified: 2026-06-22 -->
