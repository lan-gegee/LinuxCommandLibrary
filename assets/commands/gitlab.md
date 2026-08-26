# TAGLINE

GitLab API 的 Python 命令行客户端

# TLDR

**列出项目**

```gitlab project list```

**创建项目**

```gitlab project create --name "[name]"```

**列出项目的合并请求**

```gitlab project-merge-request list --project-id [id]```

**创建合并请求**

```gitlab project-merge-request create --project-id [id] --source-branch [feature] --target-branch [main] --title "[title]"```

**使用 YAML 输出**

```gitlab -o yaml project list```

**使用配置文件中指定的 GitLab 实例**

```gitlab -g [instance-name] project list```

# SYNOPSIS

**gitlab** [_options_] _object_ _action_ [_parameters_]

# OBJECTS

**project**
> 管理项目。

**project-merge-request**
> 管理合并请求。

**project-issue**
> 管理议题。

**user**
> 管理用户。

**group**
> 管理群组。

**group-member** / **project-member**
> 管理群组/项目成员。

# PARAMETERS

**--project-id** _id_
> 项目 ID。

**--name** _name_
> 资源名称。

**--title** _title_
> 标题。

**--source-branch** _branch_
> 源分支。

**--target-branch** _branch_
> 目标分支。

**-o**, **--output** _FORMAT_
> 输出格式：`legacy`（默认）、`yaml` 或 `json`。

**-f**, **--fields** _FIELDS_
> 要显示字段的逗号分隔列表。

**-c**, **--config-file** _FILE_
> 使用指定的配置文件而非默认搜索路径。

**-g**, **--gitlab** _NAME_
> 要使用的 GitLab 实例，在配置文件中定义。

**-v**, **--verbose**
> 显示所获取对象的详细信息。

# DESCRIPTION

**gitlab** 是 python-gitlab 提供的 CLI，用于与 GitLab API 交互。它可在命令行中管理项目、合并请求、议题、用户、群组及其他 GitLab 资源。

该工具遵循对象-动作模式：先指定 GitLab 对象类型，再指定对其执行的动作（例如 `list`、`create`、`get`、`update`、`delete`）。

# CONFIGURATION

**~/.python-gitlab.cfg**
> 用户配置文件（INI 格式），在 `[global]` 区块和每个实例各自的区块中保存 GitLab 实例 URL、私有令牌和默认设置。

**/etc/python-gitlab.cfg**
> 系统级配置文件，查找顺序先于用户配置。

# INSTALL

```pacman: sudo pacman -S gitlab```

```apk: sudo apk add py3-gitlab```

```nix: nix profile install nixpkgs#gitlab```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[glab](/man/glab)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/python-gitlab/python-gitlab)```

```[Documentation](https://python-gitlab.readthedocs.io/en/stable/cli-usage.html)```

<!-- verified: 2026-07-17 -->
