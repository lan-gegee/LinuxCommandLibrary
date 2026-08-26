# TAGLINE

将环境与规格说明文件进行比较

# TLDR

**比较两个环境**

```conda compare [env_name] [environment.yml]```

**将当前环境**与规格文件比较

```conda compare [environment.yml]```

# SYNOPSIS

**conda** **compare** [_env_name_] _file_

# DESCRIPTION

**conda compare** 分析已安装的 conda 环境与环境规格文件（通常是 environment.yml）之间的差异，报告软件包版本的不一致、缺失的软件包或文件中未指定的多余软件包。这对环境验证和漂移检测很有价值。

随着时间推移，conda 环境可能因手动安装、更新或依赖解析的变化而逐渐偏离其原始规格。compare 命令有助于发现环境何时不再匹配其文档化的规格——在科学计算和数据科学工作流中环境一致性至关重要时，这一点可能是关键性的。

该工具在协作场景下尤其有用：团队成员通过版本控制共享 environment.yml 文件。通过将当前环境与权威规格进行比较，开发者可以确认自己处于正确的环境状态，或者判断是否需要根据规格重建环境，以确保团队内部的一致性。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-env](/man/conda-env)(1), [conda-list](/man/conda-list)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/compare.html)```

<!-- verified: 2026-06-22 -->
