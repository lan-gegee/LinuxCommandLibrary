# TAGLINE

管理 Doppler 项目和环境

# TLDR

**列出项目**（裸命令即为列表；没有 `list` 子命令）

```doppler projects```

**创建项目**并附描述

```doppler projects create [name] --description "[description]"```

**获取项目信息**

```doppler projects get [project_id]```

**重命名项目**或修改其描述

```doppler projects update [project_id] --name [new_name] --description "[description]"```

**删除项目**且不经确认提示

```doppler projects delete [project_id] --yes```

对很长的项目列表**翻页浏览**

```doppler projects --number [50] --page [2]```

# SYNOPSIS

**doppler projects** [_subcommand_] [_project_id_] [_flags_]

# SUBCOMMANDS

(none)
> 列表就是默认动作：不带子命令运行 **doppler projects** 会打印你能看到的所有项目。

**get** [_project_id_]
> 显示某个项目的详情。

**create** [_name_]
> 创建项目。**--name** 和 **--description** 也可以作为标志而不是位置参数给出。

**update** [_project_id_]
> 修改项目的 **--name** 或 **--description**。

**delete** [_project_id_]
> 删除项目及其中的全部内容。

# PARAMETERS

**-p**, **--project** _NAME_
> 要操作的项目，覆盖为当前目录配置的项目。

**--name** _NAME_ / **--description** _TEXT_
> 在 **create** 和 **update** 时设置的元数据。

**-n**, **--number** _N_
> 最多显示的项目数。默认为 100。

**--page** _N_
> 要显示的结果页码。默认为 1。

**-y**, **--yes**
> 跳过交互式确认提示直接执行。

**--json**
> 以 JSON 格式打印结果。

# DESCRIPTION

**doppler projects** 管理 Doppler 项目——Doppler 模型中的顶层容器。一个项目包含若干*环境*（development、staging、production），每个环境再包含一个或多个 *config*，真正存放密钥的是 config。

项目通常与应用或服务一一对应。由于访问控制和审计日志都以项目为单位挂接，把不同服务拆分进各自的项目，才能实现只授予某个团队访问一个服务密钥的权限，而不波及其他服务。

日常操作大多发生在 `doppler secrets` 和 `doppler run` 里；projects 子命令主要用于初始搭建、接入新服务之时，或出现在自动开通环境的脚本中。

# CAVEATS

**delete** 会连同项目内的每个 config 和密钥一并删除，而 CLI 只提示一次。传入 **--yes** 连这一次提示也会跳过，脚本因此很容易误删生产项目。项目名在整个 CLI 和 API 中都被当作标识符使用，用 **update --name** 重命名后，引用旧名称的服务令牌、CI 配置和 `doppler setup` 状态都可能失效。

# INSTALL

```brew: brew install doppler```

```nix: nix profile install nixpkgs#doppler```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[doppler](/man/doppler)(1), [doppler-secrets](/man/doppler-secrets)(1)

# RESOURCES

```[Source code](https://github.com/DopplerHQ/cli)```

```[Homepage](https://www.doppler.com)```

```[Documentation](https://docs.doppler.com/docs/cli)```

<!-- verified: 2026-07-14 -->
