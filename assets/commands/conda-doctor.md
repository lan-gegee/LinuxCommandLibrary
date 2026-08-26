# TAGLINE

环境健康检查器

# TLDR

**检查环境健康状况**

```conda doctor```

**检查特定的环境**

```conda doctor --name [env_name]```

# SYNOPSIS

**conda** **doctor** [_options_]

# PARAMETERS

**-n**, **--name** _name_
> 要检查的环境名称。

**-p**, **--prefix** _path_
> 要检查的环境路径。

# CONFIGURATION

**~/.condarc**
> 用户级 conda 配置，涵盖频道、软件包设置和求解器选项。

**/opt/conda/.condarc**
> 系统级 conda 配置。

# DESCRIPTION

**conda doctor** 对 conda 环境运行诊断检查，以发现潜在问题，例如损坏的软件包、缺失的文件或不一致的软件包状态。它通过检查软件包元数据、文件校验和以及依赖一致性来验证环境的完整性。

当环境行为异常、软件包无法导入，或在手动修改过环境目录之后，这条命令尤其有用。它能发现仅凭软件包列表难以察觉的问题。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-info](/man/conda-info)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/doctor.html)```

<!-- verified: 2026-06-22 -->
