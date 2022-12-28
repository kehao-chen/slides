---
UTC 時間

(1) 將此虛擬機的時區設置為UTC。
(2) 重啟虛擬機。
(3)再次檢查該虛擬機的激活狀態是否恢復正常。
 
微軟產品組目前正在處理此問題，此問題的修復程序可能會在 5 月底以 Windows 更新的形式提供。
 具體時間尚未確定，以上信息僅供參考。


---
不好意思在此詢問，這不算是 Azure 的技術問題而是行政流程問題。若要申請 Azure 上的應用 Internet 連出，需要提出資訊管理委員會核准例外申請單 (Azure) 並獲得各家分公司的資訊管理委員會代表簽章

---
Azure 是否可以加入到 HiLink MPLS VPN

https://hicloud.hinet.net/cmcx.html
---
AAD
Push ACR/AAD



https://docs.microsoft.com/en-us/azure/app-service/troubleshoot-diagnostic-logs

此一議題除了 App Service 議題外，還包含防火牆規則議題故在此提出。對於使用 Azure App Service 的團隊，如果不透過 Azure Pipelines self-hosted agent，而是想透過 Azure App Service Deployment Center 進行自動部署，則需要增加一條防火牆連出局情 https://oryx-cdn.microsoft.io

然而 Azure 當前的 Internet 防火牆連出規則申請，僅允許 IP 或是 CIDR 格式，並不接受 FQDN 格式。那麼針對 oryx-cdn.microsoft.io 這個 domain，化為 CIDR 格式就會有 74 條連出規則並且隨時有可能異動

這個情況不僅有 Azure App Service Deployment Center，使用 Firebase 等外部服務也會有此問題，不曉得其他團隊是如何解決還是就查找對應的 CIDR 範圍一條條提出申請？

Detecting platforms... Error: Oops... An unexpected error has occurred. · Issue #971 · microsoft/Oryx · GitHub
	
Cannot deploy an Azure Function when Azure Function App is enabled with VNET integration · Issue #1126 · microsoft/Oryx · GitHub



---
Defender for Cloud 的 storage 



---
[6/21 9:25 AM] 徐敏哲
    之前問過，Azure Stack HCI只提供NCC納管線上環境申請使用，其他請入公雲。但都已經快要Q3了，還不見Azure落地，才會提出來反應。
​[6/21 9:26 AM] 徐敏哲
    如果要入住東日本，是否可以請itPets系統將偵測告警的規則放寬?不然入公雲後，很容易就告警了

---

萬一海纜斷線，雖有備援線路，但必會阻塞變慢。如果你能撐住壓力，留在東日本也未嘗不可。

個人對 itPETS 的可用度判定機制並不瞭解，所以是響應時間超過閾值就會視為服務失效，而這個響應時間是一個固定值還是可以設定調整的？個人已初步瞭解 itPETS的可用度會列入成績考核，也因此進駐 Japan region 有可能會增加 itPETS 識別為障礙的風險


https://teams.microsoft.com/l/message/19:a23290ed56344e668aa863184fe0086c@thread.tacv2/1654073257838?tenantId=54eb9440-cf03-45fe-835e-61bd4ce515c8&groupId=a88fcc0c-e7ad-4b25-ac90-f2ed0bc64fd1&parentMessageId=1652257601102&teamName=Azure%20%E4%BD%BF%E7%94%A8%E5%BB%BA%E8%AD%B0%E8%88%87%E5%95%8F%E9%A1%8C%E8%A8%8E%E8%AB%96&channelName=%E4%B8%80%E8%88%AC&createdTime=1654073257838


在此提供個人解法，但皆為 workaround 非公認解法。第一種是自建 DNS (個人使用 CoreDNS)，針對 *.cht.com.tw 的解析指向 OA 的 DNS 服務，其他仍參考 Azure 的 DNS 服務，如此便可以正常解析 private DNS zone 的 records，也可以解析 OA 特有的 records。另一種做法是在 Azure App Service 掛上 custom domain，不使用 private DNS zone 註冊的 domain

Custom domain 申請會需要多一組 TXT record 做 domain 擁有者的驗證，之前與 DNS 管理員建邦兄諮詢，同樣使用 IS-10 申請，在說明欄位敘述該 TXT record 的內容與用途即可

 



Type
Host
Value

A
xxx.cht.com.tw
地端環境 IP

TXT
asuid.xxx.cht.com.tw
微軟提供用於身份認證值


---

這個跟 Azure Firewall 的機制有關，不能純粹看是否可以建立 TCP 連線來判斷是否有開通防火牆規則，以個人的做法是使用 tcptraceroute 與 openssl s_client 來確認
 

Azure Firewall の各ルールの動作について | Japan Azure IaaS Core Support Blog (jpaztech.github.io)

https://jpaztech.github.io/blog/network/firewall-rules/

這是由於您的Vnet是連接到VHub上的，所有的内部流量都將經過Vhub中的Azure Firewall. Telnet 80 端口會通，其實是因爲我們Firewall的特性，四層的80和443端口測試是對防火墻的80和443端口測試，并未到達目的端，所以一直是通的。

 

根據我們後臺的查看，這個firewall應該是啓用了DNS proxy功能，并且使用了自定義的DNS服務器進行解析。您提到内部域名相關的Application Rule已經添加了，不過目前看來存在解析失敗的問題。由於微軟的客戶隱私政策，我們無法查看VWAN那邊的信息，所以還煩請您聯係一下管理VWAN的同事，以便我進行一些後續的調查。



---
登入相關的問題，請洽 資訊技術分公司/企業應用系統發展處/企業基礎服務發展科，這是登入政策的管理單位

---
POC 環境 Cloud Shell

---

這是由於 Azure 公雲管理單位設定 policy 導致無法停用安全傳輸，可以向 Azure 公雲管理單位申請豁免。不過也由於 Azure Storage Account 的 NFS 不支援安全傳輸，因此實作者需要自行做好補償措施，使用 private endpoint + NSG 進行連線管控
 

 

針對 NFS 檔案共用問題進行疑難排解 - Azure 檔案儲存體 | Microsoft Learn

桌面雲VDI  需要由OA網段操作.  經過HiGate2 到  訂閱專屬的跳板機。   要Internet透過HiGate1 進來操作桌面雲VDI 應要申請eform IS05。

請教一個問題, 如果想從 azure portal 上, 使用 storage browser 查看 storage account 下的檔案, 需要做什麼樣的設定, 目前頁面長這樣

只要按照提示的要求，增加所需的 asuid.xxx.hinet.net 的 TXT record，做為 FQDN owner 的驗證，應就可以順利加入吧？

---
三級以上系統都需透過跳板機維運
	
Azure Portal 只能透過跳板機存取

---
若 Application Gateway 能接收 Internet 連入，需和其他資源分開，建置在一個獨立的 VNET 和資源群組 (未來可能與 Internet 能連接的資源都會比照處理)
	
若無法滿足 1，Application Gateway 需要拋 Log 到 SOC，且執行與防火牆等效的管控措施

可能就是要拋 NSG Flow Log 給 SOC



---
## PaaS 日誌收攏至 LS/LC

![40%](./assets/azure-monitor-2-syslog_overview.png)

[GitHub - miguelangelopereira/azuremonitor2syslog: Forward Azure monitor logs to syslog (via Event Hub)](https://github.com/miguelangelopereira/azuremonitor2syslog/)

---
個人認為比較有爭議的會是 storage 與 DNS，如果 DNS 都是使用微軟或是中華內部的 DNS 服務，那麼有需要特別啟用 Microsoft Defender for DNS 嗎？
 
目前敝單位的 Azure Defender 費用高昂，個人猜測是 storage 的用量問題，也許跟 Elasticsearch cluster 有關，但如果 storage 限制並非公開，僅有服務應用可以存取使用，有需要特別啟用 Microsoft Defender for Storage 嗎？它主要想防護的對象應該是可被公開存取的 storage，而這項在目前的規範應是不被允許的

https://learn.microsoft.com/en-us/azure/defender-for-cloud/defender-for-storage-introduction

---

> 進駐公雲安全堡壘的設備都要做日誌收容，
> 所以不管系統是幾級


[Azure 使用建議與問題討論 / 公告 📢](https://teams.microsoft.com/l/message/19:c3761d499de64d45ad8cd035582900be@thread.tacv2/1666149108017?tenantId=54eb9440-cf03-45fe-835e-61bd4ce515c8&groupId=a88fcc0c-e7ad-4b25-ac90-f2ed0bc64fd1&parentMessageId=1666149108017&teamName=Azure%20%E4%BD%BF%E7%94%A8%E5%BB%BA%E8%AD%B0%E8%88%87%E5%95%8F%E9%A1%8C%E8%A8%8E%E8%AB%96&channelName=%E5%85%AC%E5%91%8A%20%F0%9F%93%A2&createdTime=1666149108017&allowXTenantAccess=false)

---
9.Azure proxy :10.198.135.4  port 80 (防火牆需額外開通)

有proxy 需求請mail給 顏士傑、吳秉穎 做規則的開通

聯絡窗口:	資分 顏士傑(Azure Proxy管理員)

---
8.Azure DNS :10.198.250.10 (防火牆預設已開通)

---
https://learn.microsoft.com/en-us/azure/architecture/example-scenario/gateway/firewall-application-gateway#application-gateway-after-firewall


---

App GW

Rule
---

雖然 Azure Application Gateway v2 改善了這個問題，使得任何設定變更可以立即生效，但是 Azure Application Gateway v2 勢必會需要一組 Public IP 資源。在 Azure 官方的文件中，如果要禁止 Internet 的連入，則建議可以在 NSG 中加入阻擋規則

Application Gateway V2 currently does not support only private IP mode. It supports the following combinations

 


	
Private IP and Public IP
	
Public IP only

———— Frequently asked questions about Azure Application Gateway | Microsoft Docs

---
[3/6 11:27 PM] 陳科豪關於 Azure 混合雲網路架構的規劃微心得
    


TL;DR 建議直接使用 Azure 混合雲的 IP 來建立運算資源


在地端機房的網路架構，運算資源 (e.g. VM) 並不會直接使用 10.0.0.0/8 (CHT Net) 的 private IP，而是通常會建立在 172.16.0.0/12 或是 192.168.0.0/16 的網段中，若需要其他在地端環境的服務串接，或透過 SNAT 成 10.0.0.0/8 的 private IP，再與其他地端服務串接。而這樣的好處在於若之後 VM 擴增，或是 Refactoring 使得系統架構改變遷移到 Azure App Services 或是 Azure Kubernetes Services 平臺，由於地端防火牆局情申請時的來源 IP 為 SNAT IP，因此運算資源的 IP 異動並不不會需要重新申請地端地端防火牆局情規則


在 Azure 若想要達到此一目的，則需要透過 Azure Firewall 此一網路元件，然而 Azure Firewall 是需要擁有一個 Public IP 才可以建立，這違法了公司目前所制定的 Azure 管理政策，因此只能尋求其他解決方法。在 Azure 中，Azure Load Balancer 相當於 L4 switch 的存在，那是否可以作為 L4 proxy，透過 Azure Load Balancer 去存取地端資源呢？答案是不行，因為 Azure Load Balancer 限制 backend resource 必須是與 Azure Load Balancer 同一個 VNet 上的 IP/NIC，不能使用地端服務的 private IP。那 Azure Application Gateway 相當於 L7 switch 的存在，是否可以做為 L7 proxy，透過 Azure Application Gateway 去存取地端資源呢？如果需要存取的地端環境，其使用的協議為 HTTP/HTTPS/WebSocket，則答案為可以，但如果需要 SFTP、JMS、AMQP 等其他協議，則 Azure Application Gateway 尚不支援


或許有同仁可能會想到，那是否可以使用 Nginx/HAProxy 來建立軟體的 L4 proxy 呢？簡單說結論，Azure App Services (Container) 無法用於建立 L4 proxy，單獨使用 Azure Virtual Machine 或是 Azure Container Instances 則可以運作，但考慮到 high availability，個人目前想不到任何解法，因為只要再加上 Azure Load Balancer 部分的連線就會發生問題 (e.g. SFTP)


總結來說，個人建議直接使用 Azure 混合雲的 IP 來建立運算資源，除非之後有熱心的同仁可以協助找出 SNAT 的解決方案



(1 liked)Edited<https://teams.microsoft.com/l/message/19:1b87f752b87a44ef9f48d09d0a12ee61@thread.tacv2/1646580470730?tenantId=54eb9440-cf03-45fe-835e-61bd4ce515c8&amp;groupId=a88fcc0c-e7ad-4b25-ac90-f2ed0bc64fd1&amp;parentMessageId=1646580470730&amp;teamName=Azure 使用建議與問題討論&amp;channelName=01. 混合雲 (Azure與CHTNET介接) 議題&amp;createdTime=1646580470730&amp;allowXTenantAccess=false>


---

## Azure Database (PaaS)

Azure Database (PaaS) 的 CHT 參考指南
https://teams.microsoft.com/l/channel/19%3Ab0ec73b9013c42b5aac3f00f55ac24d2%40thread.tacv2/tab%3A%3Abddc1570-848e-4446-a1bc-d86e72a79cda?groupId=a88fcc0c-e7ad-4b25-ac90-f2ed0bc64fd1&tenantId=54eb9440-cf03-45fe-835e-61bd4ce515c8&allowXTenantAccess=false

---

整理 LS (Log Sensor) 與 LC (Log Collector) 於 Azure 公雲的執行方法。於公司規定，公司管理之設備需要將日誌(資安事件紀錄、內部惡意活動偵測告警紀錄、稽核軌跡紀錄)送至LS/LC，再由 LS/LC 將這些日誌送到 SOC 進行納管。



通常安全堡壘會架設LS/LC主機，而 Azure 公雲堡壘 (CHT_Azure) 的 LS/LC 負責窗口為顏士杰，日誌納管與監控需填寫表單後請士杰兄協助提出申請。



一般的 Azure 使用情境，除非 Azure AGW 或是 Azure Firewall 等網路元件，有直接對 Internet 連接之需求，否則網路的連入/連出都會透過 Azure 公雲堡壘的控管，因此無需將其連線日誌送至 LS 收容 (已與資安處楷強兄與 Azure CCoE 秉穎兄確認做法)



應用主機的日誌收容，宗霖兄已有向士杰兄確認，申請表單包含 ISDB、資產 EQ 等需填寫欄位，其中資產 EQ 需於 ICTINV 中登錄設備才會產生。目前也尚無其他系統與 Azure 公雲堡壘的 LC 介接，士杰兄建議可以待 ICTINV 登錄完成再來提出 LC 收容申請。

---

Event Hub --> Azure Function --> Syslog

---




---


CHTSOC系統日誌伺服器：之後Ａｚｕｒｅ會提供ＬＣ／ＬＳ

---
ｅｙｅｓｅｅ監控
