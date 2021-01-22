# -*-coding:utf-8 -*-
# @Time:2020/8/17 16:21
# @Author:a'nan
# @Email:934257271
# @File:wf_task_info.py
import  requests

from middleware import wf_login

login_token = wf_login.LoginToken().login_token()
auth_token = wf_login.LoginToken().auth_token(login_token)
url = "http://irregular-app-detect-workflow.test.k8ss.cc/v1/graph"
request_body = {"query":"query task($taskId: String!)\n{  task(taskId: $taskId) \n  {   \n  app\n  completedAt  \n  createdAt    \n  expiredAt   \n  priority     \n  taskId   \n \n  outputs \n  updatedAt   \n  }\n}",
                        "variables":{"taskId":"a0f61190-311a-4ce2-b9d0-7f0a2783a7b0"},"operationName":"task"}
headers = {'Authorization':'bearer {}'.format(auth_token)}
headers1 = {'Authorization':'bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.'
                            'eyJkc3AiOiIlRTYlQUMlQTclRTklOTglQjMlRTklOTQlOTAiLCJlbWwiOiJvdXlhbmdydWlAYW50aXkuY24iLCJleHAiOjE1OTc2NzM1OTksIm5iZiI6MTU5NzY1MTY5OSwidWlkIjoib3V5YW5ncnVpMSJ9.DtLrptg7E5LiEgbLrdHkPGzJzOOU88-Q-CZCQDNYPdA'}
print(headers)
res = requests.post(url=url, json=request_body, headers=headers)
print(res.json())

