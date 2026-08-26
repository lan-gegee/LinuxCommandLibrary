# TAGLINE

带交互式 TUI 的局域网设备发现工具

# TLDR

**启动交互式设备发现 TUI**

```whosthere```

**执行一次带超时的扫描**

```whosthere scan -t [5]```

**将扫描结果导出为 JSON**

```whosthere scan -t [5] --json --pretty > [devices.json]```

# SYNOPSIS

**whosthere** [_command_] [_options_]

# DESCRIPTION

**whosthere** 是一个局域网发现工具，使用 mDNS、SSDP 和 ARP 缓存技术识别设备，且不需要提升权限。发现的设备会通过 OUI 查询补充制造商名称。支持交互式 TUI 模式、单次扫描、JSON 导出以及带 HTTP API 的守护进程模式。

# HISTORY

**whosthere** 由 **Ramon Vermeulen**（ramonvermeulen）创建，使用 **Go** 编写。

# INSTALL

```brew: brew install whosthere```

```nix: nix profile install nixpkgs#whosthere```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[arp-scan](/man/arp-scan)(1), [nmap](/man/nmap)(1), [avahi-browse](/man/avahi-browse)(1)
