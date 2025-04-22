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
