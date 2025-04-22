#
bigquery_spark_pipeline/
│
├── configs/
│   └── pipeline_config.yaml  # 全局参数控制
│
├── jobs/
│   ├── main_pipeline.py      # 主入口
│   ├── pretreat.py           
│   ├── train_model.py        
│   ├── predict.py            
│   └── output.py             
│
├── utils/
│   ├── config_utils.py       
│   ├── spark_utils.py        
│   ├── logger.py             # 日志系统
│   └── retry.py              # 容错与重试
│
└── logs/                     # 本地测试日志



# Submit the entire Pipeline
gcloud dataproc jobs submit pyspark \
  --cluster=your-cluster-name \
  --region=your-region \
  --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar \
  gs://your-bucket/code/jobs/main_pipeline.py

# 错误处理与通知建议（高级推荐，企业级）
在生产环境中，你还可以考虑：

集成监控：Stackdriver（Cloud Logging）集中管理日志。

自动通知：在logger.error中集成自动邮件、Slack或其他告警通知。

数据校验步骤：各模块结束时，加入数据量、数据质量校验逻辑。

# 云端GCS目录结构
gs://your-bucket/
│
├── code/                     # Python脚本文件
│   ├── jobs/
│   └── utils/
│
├── models/                   # 存放模型文件
│   └── lr_model/
│
└── logs/                     # Spark运行日志（云端存储）

# 部署方式与运行方法（Dataproc）
gcloud dataproc jobs submit pyspark \
  --cluster=your-cluster \
  --region=your-region \
  --jars=gs://spark-lib/bigquery/spark-bigquery-latest_2.12.jar \
  gs://your-bucket/code/jobs/main_pipeline.py

# git

  106  git add .
  107  git commit -m "Initial commit"
  108  git remote add origin http://github.com/wfuramp/my-repo.git
  109  git push -u origin master
  110  git log
  111  git branch
  112  git push -u origin main
  113  git branch
  114  ssh-keygen -t ed25519 -C "wentai.fu@liveramp.com"
  115  ssh-keygen -t ed25519 -C "wentai.fu@liveramp.com"
  116  wentalfu@wentalfu0425mac Desktop % ssh-keygen -t ed25519 -C "wentai.fu@liveramp.com"\nGenerating public/private ed25519 key pair.\nEnter file in which to save the key (/Users/wentalfu/.ssh/id_ed25519): cat ~/.ssh/id_ed25519.pub\nEnter passphrase (empty for no passphrase): \nEnter same passphrase again: \nSaving key "cat ~/.ssh/id_ed25519.pub" failed: No such file or directory\nwentalfu@wentalfu0425mac
  117  vi /Users/wentalfu/.ssh/id_ed25519.pub
  118  git remote set-url origin git@github.com:wfuramp/my-repo.git
  119  git push -u origin main\n
  120  git pull origin main --rebase
  121  git push origin main