# TAGLINE

从仓库拉取并运行 playbook

# TLDR

从 git **拉取**并运行 playbook

```ansible-pull -U [https://github.com/user/repo.git]```

运行指定的 **playbook**

```ansible-pull -U [repo_url] [playbook.yml]```

从**指定分支**拉取

```ansible-pull -U [repo_url] -C [branch_name]```

使用 **inventory** 运行

```ansible-pull -U [repo_url] -i [localhost,]```

通过 cron **定期**运行

```ansible-pull -U [repo_url] -o --sleep [60]```

# SYNOPSIS

**ansible-pull** -U _repo_url_ [_-C branch_] [_-d dest_] [_playbook.yml_]

# DESCRIPTION

**ansible-pull** 颠倒了 Ansible 常规的推送模式，由节点从中央仓库拉取配置。节点定期获取包含 playbook 的 git 仓库并在本地运行。

这适用于扩展到大量节点、引导初始化场景，或由节点自行发起配置的环境。

# PARAMETERS

**-U** _url_, **--url** _url_
> 要从中拉取的仓库 URL

**-C** _checkout_, **--checkout** _checkout_
> 要检出的分支、标签或提交

**-d** _dir_, **--directory** _dir_
> 本地检出的目标目录

**-i** _inventory_, **--inventory** _inventory_
> Inventory 文件/路径或逗号分隔的主机列表（通常为 "localhost,"）

**-m** _name_, **--module-name** _name_
> 用于检出仓库的 SCM 模块：git、subversion、hg 或 bzr（默认：git）

**-o**, **--only-if-changed**
> 仅当仓库有变更时才运行 playbook

**-s** _seconds_, **--sleep** _seconds_
> 启动前先随机等待一段时间（0 到 seconds 秒），以便错开各次运行

**--purge**
> playbook 运行完成后清除本地检出的内容

**-f**, **--force**
> 即使仓库更新失败也运行 playbook

**--full**
> 进行完整克隆而不是浅克隆

**--verify-commit**
> 校验所检出提交的 GPG 签名（仅限 git）

**--accept-host-key**
> 若仓库的主机密钥尚不存在则自动添加

# CONFIGURATION

**/etc/ansible/ansible.cfg**
> 目标节点上的系统级 Ansible 配置。

**~/.ansible.cfg**
> 每用户 Ansible 配置，覆盖系统默认值。

**ansible.cfg**
> 当前目录中的项目级配置，优先级最高。

# CAVEATS

目标节点上需要 git（或所选的 SCM）以及 ansible。私有仓库需要配置凭据。失败会使节点处于可能不一致的状态。如果未指定 playbook，ansible-pull 会依次查找以主机完全限定域名命名的文件、以其主机名命名的文件，最后是 local.yml。

# HISTORY

**ansible-pull** 的引入是为了支持基于拉取模式的配置管理，解决传统推送模式在可扩展性方面的顾虑。

# INSTALL

```dnf: sudo dnf install ansible-core```

```pacman: sudo pacman -S ansible-core```

```apk: sudo apk add ansible-core```

```zypper: sudo zypper install ansible-core```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[ansible-playbook](/man/ansible-playbook)(1), [ansible](/man/ansible)(1), [git](/man/git)(1)

# RESOURCES

```[Source code](https://github.com/ansible/ansible)```

```[Documentation](https://docs.ansible.com/ansible/latest/cli/ansible-pull.html)```

<!-- verified: 2026-06-11 -->
