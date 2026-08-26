# TAGLINE

社会工程学渗透测试框架

# TLDR

**启动 Social Engineering Toolkit**

```sudo setoolkit```

# SYNOPSIS

**setoolkit**

**sudo setoolkit**

# MAIN MENU OPTIONS

**1) Social-Engineering Attacks**
> 鱼叉式网络钓鱼、网站攻击、凭证收集、传染性介质

**2) Penetration Testing (Fast-Track)**
> 快速利用部署工具

**3) Third Party Modules**
> 额外的社区模块

**4) Update the Social-Engineer Toolkit**
> 更新到最新版本

**5) Update SET configuration**
> 修改配置设置

**6) Help, Credits, and About**
> 文档与致谢

**99) Exit the Social-Engineer Toolkit**
> 退出应用程序

# SOCIAL ENGINEERING ATTACKS

**1) Spear-Phishing Attack Vectors**
> 带恶意附件的电子邮件攻击

**2) Website Attack Vectors**
> 克隆网站以收集凭证

**3) Infectious Media Generator**
> 创建恶意 USB/CD 载荷

**4) Create a Payload and Listener**
> 生成 Metasploit 载荷

**5) Mass Mailer Attack**
> 向多个目标发送钓鱼邮件

**6) Arduino-Based Attack Vector**
> 使用 Arduino 的 USB HID 攻击

**7) Wireless Access Point Attack Vector**
> 流氓接入点攻击

**8) QRCode Generator Attack Vector**
> 恶意二维码

**9) Powershell Attack Vectors**
> 基于 Windows PowerShell 的攻击

**10) SMS Spoofing Attack Vector**
> 伪造短信

# CONFIGURATION

**/etc/setoolkit/set.config**
> 主配置文件，控制 Apache 服务器开关、Web 界面端口、邮件设置以及 Metasploit 集成路径。

# DESCRIPTION

**setoolkit**（Social-Engineer Toolkit）是一个基于 Python 的渗透测试框架，专注于社会工程学攻击。它通过菜单驱动的界面为网络钓鱼、凭证收集和载荷投递提供自动化的攻击向量。

该工具包与 Metasploit 集成以进行载荷生成和利用。常见用例包括克隆网站以收集凭证、为鱼叉式钓鱼活动生成恶意文件，以及制作受感染的 U 盘用于物理访问攻击。

SET 为授权的渗透测试和安全意识培训而设计。它展示了攻击者如何利用人类心理而非技术漏洞，帮助组织理解并防御社会工程学威胁。

# CAVEATS

需要 root 权限才能运行。许多攻击需要额外配置（邮件服务器、域名、SSL 证书）。该工具包只能在获得明确授权的情况下使用——未经授权的使用属于违法行为。某些杀毒软件可能会标记生成的载荷。已弃用的 **se-toolkit** 命令已被 **setoolkit** 取代。

# HISTORY

Social-Engineer Toolkit 由 **TrustedSec** 的 **David Kennedy**（ReL1K）创建，首次发布于 **2009** 年。它旨在提供一个综合平台，用于测试组织对社会工程学攻击的易感性。SET 成为渗透测试中使用最广泛的工具之一，尤其适用于模拟钓鱼活动和开展安全意识评估。该项目仍在 GitHub 上积极维护。

# SEE ALSO

[msfconsole](/man/msfconsole)(1), [beef-xss](/man/beef-xss)(1), [gophish](/man/gophish)(1)
