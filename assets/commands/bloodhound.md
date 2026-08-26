# TAGLINE

可视化 Active Directory 攻击路径

# TLDR

**启动 BloodHound 图形界面**（旧版 Electron 应用）

```bloodhound```

**禁用 Chromium 沙箱启动**（现代 Linux 上的常见变通方法）

```bloodhound --no-sandbox```

窗口渲染异常时**禁用 GPU 加速**

```bloodhound --no-sandbox --disable-gpu```

启动后，登录 Neo4j 数据库，并使用 GUI 的"Upload Data"按钮导入采集器生成的 JSON 或 zip 文件。

# SYNOPSIS

**bloodhound** [_electron-options_]

# DESCRIPTION

**BloodHound** 是一款安全工具，利用图论揭示 Active Directory 和 Azure 环境中隐藏的关系与攻击路径。它将复杂的信任关系、组成员身份和权限可视化——攻击者可利用这些来攻陷域管理员。

该工具由两部分组成：枚举目录对象的采集器（Windows 上的 SharpHound、Linux 上的 bloodhound-python），以及将这些数据导入 Neo4j 图数据库以供分析的 BloodHound 应用程序。

这里描述的 **bloodhound** 命令启动的是旧版 Electron 桌面 GUI。它是图形客户端，不接受任何 BloodHound 特有的命令行标志：数据库和凭证在登录界面配置，采集的数据也通过 GUI 导入。旧版已被弃用。仍在积极维护的后续版本 BloodHound Community Edition（BHCE）以 Web 应用形式发布，通过 Docker Compose（或 bloodhound-cli 辅助工具）部署，而非独立命令。

安全团队用 BloodHound 识别并修复危险配置，渗透测试人员则用它寻找提权路径。内置查询可以发现常见攻击路径，如"Shortest Path to Domain Admin"或"Kerberoastable Users"。

# CAVEATS

BloodHound 是一款强大的安全工具，使用前必须获得适当授权。从 Active Directory 收集数据可能触发安全警报。该工具展示的是理论上的攻击路径；实际利用还需要额外步骤。旧版 GUI 需要一个正在运行的 Neo4j 实例，在登录界面进行配置。在现代 Linux 桌面上，Electron 应用通常需要 **--no-sandbox** 才能启动。大型环境进行分析可能需要大量内存。旧版已不再维护；新部署应使用 BloodHound Community Edition。

# HISTORY

BloodHound 由 SpecterOps 的 **Andy Robbins**、**Rohan Vazarkar** 和 **Will Schroeder** 创建，于 **2016 年**在 **DEF CON 24** 上首次亮相。它将以前难以手工分析的复杂关系可视化，革新了 Active Directory 安全评估。该工具开源，已成为 AD 安全评估的行业标准。

# INSTALL

```nix: nix profile install nixpkgs#bloodhound```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[bloodhound-python](/man/bloodhound-python)(1), [neo4j](/man/neo4j)(1), [impacket](/man/impacket)(1), [ldapsearch](/man/ldapsearch)(1)

# RESOURCES

```[Source code](https://github.com/SpecterOps/BloodHound)```

```[Homepage](https://bloodhound.specterops.io/)```

<!-- verified: 2026-06-19 -->
