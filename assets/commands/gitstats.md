# TAGLINE

从 Git 仓库生成统计信息

# TLDR

**为仓库生成统计数据**

```gitstats [repo_path] [output_dir]```

为最近 10 次提交**生成统计数据**

```gitstats -c commit_begin='HEAD~10' [repo] [output]```

**设置项目名称**和作者数量上限

```gitstats -c project_name='[MyProject]' -c max_authors=[20] [repo] [output]```

# SYNOPSIS

**gitstats** [_options_] _repository_ _output_directory_

# PARAMETERS

**-c** _key=value_
> 配置选项。可以指定多次。

### 配置键

**project_name**
> 在生成页面上显示的项目名称。默认：仓库目录的 basename。

**max_authors**
> 作者列表中显示的作者数量上限。

**authors_top**
> 显示多少位头部作者。

**max_domains**
> 按提交统计的域名列表中显示的域名数量上限。

**max_ext_length**
> 文件扩展名的最大长度。

**commit_begin**
> 统计范围的起始提交。

**commit_end**
> 统计范围的结束提交。

**start_date**
> 通过 --since 传给 git 的起始日期。

**processes**
> 提取数据时使用的并发进程数。

**style**
> 要使用的 CSS 样式表。

# DESCRIPTION

**gitstats** 从 Git 仓库生成统计信息，并创建带图表的 HTML 报告，展示提交活跃度、作者贡献、文件数量和代码行数随时间的变化。

输出是一个静态 HTML 站点，可在任何浏览器中查看，直观呈现项目历史和贡献者行为模式。

# INSTALL

```nix: nix profile install nixpkgs#gitstats```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-log](/man/git-log)(1), [git-summary](/man/git-summary)(1)
