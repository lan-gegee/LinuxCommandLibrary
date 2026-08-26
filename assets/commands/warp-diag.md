# TAGLINE

Cloudflare WARP 诊断与故障排除工具

# TLDR

**运行完整诊断**并创建 zip 报告

```warp-diag```

**运行诊断**并在输出文件名中**加入时间戳**

```warp-diag --add-ts```

**运行诊断并保存**到指定目录

```warp-diag --output [path/to/directory]```

以交互方式向 Cloudflare **提交反馈**

```warp-diag feedback```

# SYNOPSIS

**warp-diag** [_options_] [_subcommand_]

# PARAMETERS

**--output** _directory_
> 将诊断 zip 文件保存到指定目录。

**--add-ts**
> 在输出文件名中添加时间戳。

**feedback**
> 以交互方式向 Cloudflare 提交反馈。

# DESCRIPTION

**warp-diag** 收集 Cloudflare WARP 客户端的诊断信息并将其打包成 zip 文件。它会收集 WARP 客户端日志、系统网络配置、DNS 设置、连接测试结果和客户端状态，帮助排查连接问题。

生成的 zip 文件可提供给 Cloudflare 支持团队进行分析。

# CAVEATS

需要已安装 Cloudflare WARP 客户端（warp-svc）。某些诊断可能需要 root/管理员权限。zip 文件可能包含敏感的网络配置细节。

# SEE ALSO

[warp-cli](/man/warp-cli)(1)
