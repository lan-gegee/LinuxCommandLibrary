# TAGLINE

基础设施自动化与配置管理平台

# TLDR

**生成新的 cookbook**

```chef generate cookbook [cookbook_name]```

**生成新的 recipe**

```chef generate recipe [cookbook_name] [recipe_name]```

**校验 cookbook 语法**

```chef exec cookstyle [cookbook_path]```

**在本地运行 cookbook**

```chef-client --local-mode --runlist "[recipe[cookbook::recipe]]"```

**显示已安装版本**

```chef --version```

**将 gem 安装到 Chef 中**

```chef gem install [gem_name]```

**运行 InSpec 测试**

```chef exec inspec exec [test_path]```

# SYNOPSIS

**chef** _command_ [_options_]

# DESCRIPTION

**chef** 是 Chef Workstation 的命令行界面。Chef Workstation 是一个配置管理与基础设施自动化平台。它提供开发、测试和管理 cookbook 的工具，cookbook 定义了系统配置。

Cookbook 包含用 Ruby DSL 编写的 recipe，描述系统的目标状态。Chef 将这些 recipe 应用到节点上，确保整个基础设施配置一致。其工作流包括本地开发、用 Test Kitchen 测试，以及部署到 Chef Server。

# PARAMETERS

**generate** _type_ _name_
> 生成 cookbook、recipe、模板或其他组件。

**exec** _command_
> 使用内置 Ruby 在 Chef 环境中运行命令。

**gem** _subcommand_
> 管理 Chef 环境中的 Ruby gems。

**install** _policyfile_
> 从 Policyfile 安装 cookbook。

**update** _policyfile_
> 更新 Policyfile 中的 cookbook。

**export** _policyfile_ _path_
> 导出用于部署的策略归档。

**push** _policy_group_ _policyfile_
> 将策略推送到 Chef Server。

**--version**
> 显示版本信息。

**--help**
> 显示帮助信息。

# CONFIGURATION

**~/.chef/config.rb**
> Chef Workstation 主配置文件。设置默认的 Chef Server URL、客户端密钥路径、cookbook 路径和节点名称。

**~/.chef/credentials**
> 存储 Chef Server 凭据和配置档案，用于管理多个组织。

**/etc/chef/client.rb**
> 受管节点上的 Chef 客户端配置。设置服务器 URL、节点名称、验证密钥和运行列表间隔。

# CAVEATS

开发 recipe 需要 Ruby 知识。集中管理需要搭建 Chef Server。本地模式测试需要足够的资源。Cookbook 可能有复杂的依赖关系。

# HISTORY

**Chef** 由 **Adam Jacob** 于 **2009** 年在 **Opscode**（后来的 Chef Software）创建。它与 Puppet 一起开创了"基础设施即代码"的理念。Chef 用 Ruby 和 Erlang 编写，以其灵活性而广受欢迎。**2020** 年，Chef 被 **Progress Software** 收购。其工具链已从以 knife 为中心的工作流演进为现代的 Chef Workstation。

# SEE ALSO

[knife](/man/knife)(1), [ansible](/man/ansible)(1), [puppet](/man/puppet)(1)
