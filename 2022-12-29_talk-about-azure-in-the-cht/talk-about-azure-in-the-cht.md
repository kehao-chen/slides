---
marp: true
title: Azure 入雲淺談
description: 公司資訊系統入 Azure 公雲踩坑經驗分享
theme: uncover
paginate: true
_paginate: false
---

# Azure 入雲淺談
### 公司資訊系統入 Azure 公雲<br/>踩坑經驗分享

陳科豪

![bg left:30% 65%](./assets/azure-logo.png)

---

## 你的公雲不是你的公雲

> 公雲放到公司的規範及框架中之後，
> 就不見得是你以為的公雲了

---
## 法律與規章

- L-0150 中華電信資通系統營運持續管理規範V01-2022.04
- 使用公雲服務資安作業要點V1-2021.09
- 資通安全管理規範與實施細則V14- 2022.08
- 系統進駐公雲安全作業要點V001-2021.09

---

## 無法在 Azure Portal 使用的功能

- 🚫 Cloud Shell
- 🚫 Storage Browser (Storage Account)
- 🚫 Kudu service (App Service)
- 🚫 Kubernetes Resources (Kubernetes Services)
- etc.

---
## Network Issues

![](./assets/network-issues-meme.png)

---
## Azure ExpressRoute

![](./assets/expressroute-connection-overview.png)

[Azure ExpressRoute Overview:<br>Connect over a private connection | Microsoft Learn](https://learn.microsoft.com/en-us/azure/expressroute/expressroute-introduction)


---
## Azure ExpressRoute

![](./assets/azure-expressroute-explain.png)


---

## 中華電信多雲交換平台 (CMCX)

![](./assets/cmcx_pic02.png)

[中華電信多雲交換平台 (CMCX)](https://www.hicloud.hinet.net/cmcx.html)

---
## HiLink MPLS VPN 的成本支出

- Azure Expressroute 到資分 CMXC 頻寬
- 資分 CMCX 固定頻寬
- 網分與資分 CMCX 間的 HiLink 頻寬

---
## Azure 日本東部地區

CMCX (新北板橋區) -> Azure 日本東部機房 (東京埼玉縣)
- 物理距離：2,000 公里的距離
- 網路延遲：30 ~ 70 ms 的延遲

---

![bg fit :60%](./assets/no-azure-in-new-taipei.png)

---
## CHT 機房網路進出規範

> 21.1.5 機房內部網路與外部網路 (含 CHTNet) 間應設置網路防火牆或相同功能之設備管制網路封包進出。
> 21.1.7 封閉網路之建置，須經單位主管核定，並由各機構資訊或網路權責單位負責設置與管理，並定期監控網路封閉狀態。
> —— 資通安全管理規範與實施細則V14- 2022.08

---
## Hub-spoke network topology

![](./assets/azure-hub-spoke.png)

[Hub-spoke network topology in Azure -<br>Azure Architecture Center | Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/hybrid-networking/hub-spoke?tabs=cli)

---

![](./assets/route-injection-split-route-server-with-firewall.png)

[Default route injection in spoke VNets |<br>Microsoft Learn](https://learn.microsoft.com/en-us/azure/route-server/route-injection-in-spokes)


---
## Azure 負載平衡方案決策樹

![](./assets/load-balancing-decision-tree.png)

[Load-balancing options -<br>Azure Architecture Center | Microsoft Learn](https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/load-balancing-overview#decision-tree-for-load-balancing-in-azure)

---
## 建議使用 Azure App GW v2
- 依據負載**自動擴展**
- 最多 5 倍的 TLS 卸載效能提升
- 更快的佈建和更新速度


[What is Azure Application Gateway v2? |<br>Microsoft Learn](https://learn.microsoft.com/en-us/azure/application-gateway/overview-v2)

---
##  App GW v2 的合規性

> But if you'd like to use Application Gateway V2 with only private IP, you can follow the process below:
>  - Don't create any listeners for the public frontend IP address.
>  - Create and attach a **Network Security Group** for the Application Gateway subnet

[Frequently asked questions about Azure Application Gateway | Microsoft Learn]()

---
## App GW v2 的 UDR 設定

> An incorrect configuration of the route table could result in asymmetrical routing in Application Gateway v2. Ensure that all management/control plane traffic is sent **directly to the Internet and not through a virtual appliance**. Logging, metrics, and CRL checks could also be affected.

---
## App GW 密碼套件設定 (v2 版本)

```sh
RG=YOUR_RESOURCE_GROUP
APP_GW=YOUR_APP_GW

az network application-gateway ssl-policy set \
    --resource-group $RG \
    --gateway-name $APP_GW \
    --name AppGwSslPolicy20220101S \
    --policy-type Predefined
```

[az network application-gateway ssl-policy |<br>Microsoft Learn](https://learn.microsoft.com/en-us/cli/azure/network/application-gateway/ssl-policy?view=azure-cli-latest#az-network-application-gateway-ssl-policy-set-examples)

---
## App GW 密碼套件設定 (v1 版本)


```sh
RG=YOUR_RESOURCE_GROUP
APP_GW=YOUR_APP_GW

az network application-gateway ssl-policy set \
    --resource-group $RG \
    --gateway-name $APP_GW \
    --policy-type Custom \
    --min-protocol-version TLSv1_2 \
    --cipher-suites TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384 \ 
        TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256 \
        TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384 \
        TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
```

---
## App GW 密碼套件設定

![](./assets/ssl-labs.png)

---
## CHT 資訊系統連出規範

> 17.2.4 機房內資通訊處理設備不應主動連出網際網路 (含間接連接，如：透過 Proxy 連出網際網路)，若因業務需求無法禁止，應限定採用「點對點」與管制服務埠之機制。並提出具體理由，陳報各分公司 (院) 資安督導副首長核准，或由資安督導副首長授權資安專責主管審查並定期陳報資安督導副首長相關資料。
> —— 資通安全管理規範與實施細則V14- 2022.08

---
## Azure 防火牆連出規則 (HTTPS)
![](./assets/nc-fetnet.png)

---
## Azure 防火牆允連規則 (HTTPS)
![](./assets/curl-fetnet-openssl-error.png)

---
## Azure 防火牆連出規則 (HTTPS)
![](./assets/tcptraceroute-fetnet.png)

---
## Azure 防火牆連出規則 (HTTPS)

若無相符的網路規則，而且通訊協定是 HTTP、HTTPS 或 MSSQL，則封包會依據 **應用程式規則** 的優先順序進行評估

[Azure Firewall の各ルールの動作につい |<br>Japan Azure IaaS Core Support Blog](https://jpaztech.github.io/blog/network/firewall-rules/)

---
## Azure 防火牆連出規則 (HTTPS)

```bash
./scapy-tcp-traceroute.py -f rules.csv
```

![](./assets/scapy-tcp-traceroute.png)




---
## 自建 VNet

#### 需求情境
網路/運算元件可以依據負載**自動擴展**，<br>但每新建一組實例便需要一組 IP Address

#### 執行難點
  - VNet Peering
  - SNAT

---
## 自建 VNet - 以 PMS 為例



---
## 資料庫遷移

### TODO：

---
## Azure PaaS 日誌收容

> 進駐公雲安全堡壘的設備都要做日誌收容，
> 所以不管系統是幾級


[Azure 使用建議與問題討論 / 公告 📢](https://teams.microsoft.com/l/message/19:c3761d499de64d45ad8cd035582900be@thread.tacv2/1666149108017?tenantId=54eb9440-cf03-45fe-835e-61bd4ce515c8&groupId=a88fcc0c-e7ad-4b25-ac90-f2ed0bc64fd1&parentMessageId=1666149108017&teamName=Azure%20%E4%BD%BF%E7%94%A8%E5%BB%BA%E8%AD%B0%E8%88%87%E5%95%8F%E9%A1%8C%E8%A8%8E%E8%AB%96&channelName=%E5%85%AC%E5%91%8A%20%F0%9F%93%A2&createdTime=1666149108017&allowXTenantAccess=false)

---
## Azure PaaS 日誌收容

![](./assets/azure-monitor-2-syslog_overview.png)

[GitHub - miguelangelopereira/azuremonitor2syslog: Forward Azure monitor logs to syslog (via Event Hub)](https://github.com/miguelangelopereira/azuremonitor2syslog/)

---
## IP Address 168.63.129.16

> The VM Agent requires outbound communication over ports 80/tcp and 32526/tcp with WireServer (168.63.129.16). **These should be open in the local firewall on the VM.** The communication on these ports with 168.63.129.16 is not subject to the configured network security groups.

[What is IP address 168.63.129.16? |<br>Microsoft Learn](https://learn.microsoft.com/en-us/azure/virtual-network/what-is-ip-address-168-63-129-16)

---
### Azure File Share 不同層級小檔讀寫效能

| Storage                     | Operation     | Throughput |
| --------------------------- | ------------- | ---------- |
| Azure File Share (Standard) | Reads<br>Writes  | 4.1 MB/s<br>4.3 MB/s   |
| Azure File Share (Premium)  | Reads<br>Writes | 42 MB/s<br>33 MB/s    |

[Azure Container Apps: working with storage - Microsoft Community Hub](https://techcommunity.microsoft.com/t5/fasttrack-for-azure/azure-container-apps-working-with-storage/ba-p/3561853)

---
## Microsoft Defender for Storage

[](./assets/defender-for-storage-pms-billing.png)



---
## Azure AD Application Developer

> Azure AD 應用程式註冊，<br>使用 AKS create、Service Prinicipal、Azure Pipeline Create Resource，您可能會需要這個權限

[Application Developer 權限申請 (office.com)](https://forms.office.com/r/aEHei3tRiD)

---
## Azure 使用建議與問題討論

![](./assets/qr-code_azure-use-suggestion.png)

---
## Q&A Session

![](./assets/qa.png)

---
## Freepik - Flaticon

- [Azure icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/azure)
- [Qa icons created by Freepik - Flaticon](https://www.flaticon.com/free-icons/qa)