# Scapy TCP Traceroute

## Prepare Environment

### Kubernetes
> 目前僅有在 Kubernetes 準備運行環境的指南

Step 1. 編譯運行環境的 Container Image，並推送到 Container Registry

```sh
TAG=tag
HARBOR_PROJECT=HARBOR_PROJECT

podman build \
    -f Containerfile \
    -t harbor.cht.com.tw:30725/$HARBOR_PROJECT/scapy-container:$TAG \
    .

docker push harbor.cht.com.tw:30725/$HARBOR_PROJECT/scapy-container:$TAG
```

Step 2. 部署運行環境的 Pod 到 Kubernetes Cluster

```
kubectl apply -f scapy-container-pod.yaml
```

Step 3. 將 Scapy TCP Traceroute 腳本複製到運行環境的 Pod 中

```
kubectl cp scapy-tcp-traceroute.py scapy:/root
kubectl exec scapy -c -- chmod +x /root/scapy-tcp-traceroute.py
```

## Usage
### Kubernetes
> 目前僅有在 Kubernetes 使用的指南

Step 1. 複製 CSV 檔案到 Pod 中

```bash
kubectl cp /path/to/your/csv/foo.csv scapy:/root
```

CSV 檔案必須包含 header，並且至少有 `host` 與 `port` 這兩個欄位 (順序無關)，其中 `host` 欄位的值為目的端的 IP address 或 domain name，而 `port` 欄位為目的端的 port。以下便是一份合法的 CSV 檔案內容範例：

```csv
host,port,目的
10.80.71.101,443,中台(API Gateway)
10.80.71.102,443,中台(API Gateway)
10.80.71.103,443,中台(API Gateway)
10.80.71.104,443,中台(API Gateway)
10.175.224.10,19901,EAI
10.198.153.28,19901,EAI
mbr.cht.com.tw,443,CHT會員系統
cht365.webhook.office.com,443,Microsoft Teams Webhook
hwpnsqa.emome.net,8443,Hami Pay 推播
```

Step 2. 在 Scapy Pod 運行 Bash

```sh
kubectl exec -it scapy -- bash
```

Step 3. 運行 Scapy TCP Traceroute 腳本

```sh
cd ~
./scapy-tcp-traceroute.py --file foo.csv
```

若正確執行可以看到以下輸出

![scapy-tcp-traceroute.png](./scapy-tcp-traceroute.png)