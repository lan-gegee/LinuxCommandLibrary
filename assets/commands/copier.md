# TAGLINE

可更新的项目模板工具

# TLDR

**从模板创建项目**

```copier copy [gh:user/template] [destination/]```

**从本地模板创建项目**

```copier copy [./template] [./project]```

**更新已有项目**

```copier update```

**更新到指定版本**

```copier update --vcs-ref [v2.0.0]```

**用新的答案重新复制**

```copier recopy```

**以非交互方式回答提示**

```copier copy --data [name=myproject] [template] [dest]```

# SYNOPSIS

**copier** _command_ [_options_] [_arguments_]

# DESCRIPTION

**copier** 是一个类似于 cookiecutter 的项目模板工具，但有一个关键区别：当模板演进时，它可以更新已有的项目。这使得它非常适合维护多个基于同一共享模板的项目，因为你可以把模板中的改进和缺陷修复传播到所有派生项目。

该工具使用 Jinja2 模板引擎，支持以 Git 仓库 URL 和本地路径作为模板来源。模板通过 Git 标签进行版本管理，使项目能够追踪自己由哪个模板版本创建，并在保留本地定制的同时更新到更新的版本。

copier 在生成的项目中存储关于模板答案的元数据，使 **update** 命令能够将模板变更与你的修改智能合并。这解决了传统项目生成器的一大局限——对模板的改进无法应用到已有项目上。该工具要求 Python 3.10+，在 Python 和 Web 开发社区中尤其流行。

# COMMANDS

**copy** _template_ _destination_
> 从模板创建新项目

**update**
> 根据模板更新项目

**recopy**
> 用新的答案重新生成

# PARAMETERS

**--data** _key=value_
> 以非交互方式回答问题

**--vcs-ref** _ref_
> Git 引用（标签/分支）

**--trust**
> 信任模板（运行任务）

**--pretend**
> 仅预览而不创建文件

**--skip** _path_
> 跳过指定路径

**--force**
> 不作提示直接覆盖

**-a**, **--answers-file** _file_
> 从文件加载答案

# TEMPLATE STRUCTURE

以 .jinja 结尾的文件会被渲染。其余文件原样复制。

```
template/
├── copier.yml        # Config & questions
├── {{project_name}}/ # Dynamic directory
└── README.md.jinja   # Templated file
```

# CAVEATS

要求 Python 3.10+ 和 Git 2.27+。模板通过 Git 标签管理版本。带有任务的模板请使用 --trust。

# INSTALL

```brew: brew install copier```

```nix: nix profile install nixpkgs#copier```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cookiecutter](/man/cookiecutter)(1)
