# Deploy LINE Chatbot to Cloud Function

1. Change to Folder `23-line-chatbot-for-chat-with-data`
```
cd 23-line-chatbot-for-chat-with-data
```


2. Copy and Edit `line_secret.yml.example`

```
cp line_secret.yml.example line_secret.yml
```

3. Upload file `sa.json` to folder `private`

4. Edit `scripts/init.sh` for deploy

```
cp scripts/init.sh.example scripts/init.sh
```

5.  Deploy you Cloud Run Function 

```
 ./scripts/deploy.sh 
```

6. Check Cloud Function Deploy at https://console.cloud.google.com/functions/list?referrer=search&project=dataaibootcamp

![alt text](../assets/23-deploy-cloud-function-result.png)

7. Copy Cloud Function Endpoint to use as web hook
![alt text](../assets/23-deploy-cloud-function-result.png) 

8. Add and verify webhook
![alt text](../assets/23-link-webhook-from-deploy-success.png)
![alt text](../assets/23-3-add-web-hook-to-line-console.png)

