# TAGLINE

基于主机的文件系统完整性监控

# TLDR

初始化数据库（建立基线）

```sudo tripwire --init```

执行完整性检查

```sudo tripwire --check```

以交互模式执行完整性检查

```sudo tripwire --check --interactive```

合法变更之后更新数据库

```sudo tripwire --update --twrfile [path/to/report.twr]```

更新策略文件

```sudo tripwire --update-policy [path/to/policy.txt]```

测试配置而不做修改

```sudo tripwire --test```

# SYNOPSIS

**tripwire** {**--init** | **--check** | **--update** | **--update-policy** | **--test**} [_options_]

# PARAMETERS

**-m i**, **--init**
> 数据库初始化模式。根据当前文件系统状态创建基线数据库。

**-m c**, **--check**
> 完整性检查模式。将当前文件系统与基线数据库进行比较。

**-m u**, **--update**
> 数据库更新模式。更新数据库以反映合法的变更。

**-m p**, **--update-policy**
> 策略更新模式。应用新策略并同步数据库。

**-m t**, **--test**
> 测试模式。验证配置而不做更改。

**-I**, **--interactive**
> 完整性检查后在编辑器中打开报告，便于选择要更新的数据库条目。

**-r** _file_, **--twrfile** _file_
> 为数据库更新模式指定报告文件。

**-p** _file_, **--polfile** _file_
> 指定要使用的策略文件。

**-c** _file_, **--cfgfile** _file_
> 指定配置文件的位置。

**-v**, **--verbose**
> 启用详细输出。

**-s**, **--silent**
> 屏蔽除错误之外的所有输出。

**-n**, **--no-tty-output**
> 不将报告打印到控制台。

**-E**, **--signed-report**
> 创建经过加密签名的报告。

# DESCRIPTION

**Tripwire** 是一个基于主机的入侵检测系统 (HIDS)，用于监控文件系统的完整性。它创建一个记录文件属性的基线数据库，并定期将当前状态与该基线比较，以检测未经授权的添加、删除或修改。

该工具有多种运行模式：初始化创建基线数据库；完整性检查将当前文件与基线比较；数据库更新纳入合法的变更；策略更新则修改监控规则。所有数据库和策略文件都经过加密签名以防篡改。

Tripwire 使用两把加密密钥：站点密钥用于组织范围的策略，本地密钥则对每台服务器唯一。这样既能集中管理策略，又能保持每台服务器数据库的安全性。

完整性检查的退出码表示发生了什么变化：0（无变化）、1（新增文件）、2（文件被修改）、4（文件被删除）、8（出错）。

# CONFIGURATION

**/etc/tripwire/tw.cfg**
> 主配置文件，指定数据库位置、报告目录和邮件设置。

**/etc/tripwire/tw.pol**
> 策略文件，定义要监控哪些文件和目录以及检查哪些属性。

**/var/lib/tripwire/$(HOSTNAME).twd**
> 基线数据库文件，包含记录下来的文件系统状态。

**TRIPWIRE_SITE_KEY**
> 用于签署策略和配置文件的站点密钥路径。

**TRIPWIRE_LOCAL_KEY**
> 用于签署数据库和报告的本地密钥路径。

# CAVEATS

基线数据库必须在确认系统处于干净状态之后创建。以详细输出运行可能暴露敏感的文件路径。报告应及时审阅，因为攻击者可能在两次检查之间修改文件后又恢复原状。数据库文件应妥善保管，最好存放在只读介质上。

# HISTORY

**Tripwire** 最初由 **Gene Kim** 和 **Gene Spafford** 于 **1992 年**在**普渡大学**作为学术研究项目开发。它是最早被广泛用于 Unix 安全的文件完整性监控工具之一。开源版本后来由 Tripwire Inc. 维护，同时也有商业企业版可用。它至今仍是基于主机的入侵检测领域的基础工具。

# INSTALL

```apt: sudo apt install tripwire```

```dnf: sudo dnf install tripwire```

```zypper: sudo zypper install tripwire```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[aide](/man/aide)(1), [samhain](/man/samhain)(8), [md5sum](/man/md5sum)(1), [sha256sum](/man/sha256sum)(1)
