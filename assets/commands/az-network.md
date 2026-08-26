# TAGLINE

管理 Azure 网络资源

# TLDR

**创建 DNS 区域**

```az network dns zone create -g [resource-group] --name [example.com]```

向 DNS 区域**添加 A 记录**

```az network dns record-set a add-record -g [resource-group] --zone-name [example.com] --record-set-name [www] --ipv4-address [1.2.3.4]```

**创建应用程序安全组**

```az network asg create -g [resource-group] --name [myASG]```

**创建应用程序网关**

```az network application-gateway create --name [myAppGateway] -g [resource-group] --sku [Standard_v2]```

**列出资源组中的虚拟网络**

```az network vnet list -g [resource-group]```

**创建虚拟网络**

```az network vnet create -g [resource-group] --name [myVNet] --address-prefix [10.0.0.0/16]```

**创建网络安全组**

```az network nsg create -g [resource-group] --name [myNSG]```

# SYNOPSIS

**az network** _subcommand_ [_options_]

# DESCRIPTION

**az network** 管理 Azure 网络资源，包括虚拟网络、DNS 区域、负载均衡器、应用程序网关、VPN 网关、ExpressRoute 线路和网络安全组。

Azure 网络为云基础设施提供基础，实现 Azure 资源之间、本地环境与互联网之间的安全连接。

# SUBCOMMANDS

**Virtual Networks**
> vnet create, vnet delete, vnet list, vnet show, vnet subnet

**DNS**
> dns zone create, dns zone list, dns record-set a, dns record-set cname, dns record-set mx

**Load Balancers**
> lb create, lb delete, lb list, lb rule, lb probe, cross-region-lb

**Application Gateway**
> application-gateway create, application-gateway delete, application-gateway start, application-gateway stop

**Security**
> nsg create, nsg rule, asg create, ddos-protection

**Connectivity**
> express-route, vpn-gateway, bastion, nat gateway, public-ip

# CAVEATS

许多网络资源存在依赖关系；例如，删除虚拟网络前需要先移除所有关联的子网和已连接的资源。DNS 记录变更可能需要时间才能在全球传播。应用程序网关即使停止也会产生费用；请删除不再使用的网关。

# HISTORY

Azure 虚拟网络是最早的 Azure 服务之一，随 **2010** 年 Azure 正式发布一同推出。网络能力此后大幅扩展，包括 Azure DNS（2015）、Application Gateway、ExpressRoute 和高级安全功能。

# INSTALL

```dnf: sudo dnf install azure-cli```

```pacman: sudo pacman -S azure-cli```

```zypper: sudo zypper install azure-cli```

```brew: brew install azure-cli```

```nix: nix profile install nixpkgs#azure-cli```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[az](/man/az)(1), [az-vm](/man/az-vm)(1), [az-aks](/man/az-aks)(1)
