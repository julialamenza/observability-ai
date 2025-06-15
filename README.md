#### 🧪 Observability + AI Lab

This lab simulates a production-like environment for exploring observability and anomaly detection using synthetic logs, Prometheus, Grafana, and a Python-based AI module.

#### 📦 Components

**Log Generator**
Continuously generates synthetic logs with INFO, WARNING, and ERROR levels.

**Log Exporter**
Reads the log file in real time and exposes log_error_count and log_warning_count metrics via HTTP for Prometheus.

**Prometheus**

Collects metrics from the log exporter and anomaly detector.

**Grafana**
Connects to Prometheus to visualize metrics with prebuilt dashboards.

**Anomaly Detector**(optional)

A Python service that scans logs for anomalies and exposes detection metrics to Prometheus.

#### 🐳 How to Run the Stack

Clone this repo and from the root directory, run:
```
docker-compose up --build
```
Access the Services:

Grafana:[ http://localhost:3000](" http://localhost:3000")  (login: admin / admin)

Prometheus: [http://localhost:9090]("http://localhost:9090")

Log Exporter Metrics: [http://localhost:8000/metrics]("http://localhost:8000/metrics")

Anomaly Detector Metrics: [http://localhost:8100/metrics]("http://localhost:8100/metrics")

#### 📊 Dashboards

Grafana is preconfigured to load dashboards from grafana/dashboards.

To import manually:

**Open** Grafana UI.

Go to **Dashboards** > Import.

Upload or paste the JSON from grafana/log_dashboard_with_alert.json.

### 🧠 How Anomaly Detection Works

The anomaly detector is a Python service that continuously monitors the log file and identifies unusual behavior based on simple heuristics:

1. **Tail the Log File**
Continuously reads new lines from the shared **app.log **file.

2. **Pattern Matching**
Scans for excessive ERROR and WARNING entries and identifies spikes.

3. ** Metric Exposure**

**Publishes:**
	- anomaly_count_total: total anomalies detected
	- last_anomaly_detected: optional timestamp of latest anomaly

4.  **Heuristic-Based Logic**
Uses thresholds like "**N errors in X seconds" **but can be extended with:

- Statistical analysis

- Machine learning

- NLP-based log parsing

These metrics are exposed on **:8100/metrics **and scraped by Prometheus.

#### 📁 Project Structure📁 Project Structure


```
├── README.md
├── ai
│   ├── Dockerfile
│   └── anomaly_detector.py
├── app.log
├── docker-compose.yml
├── grafana
│   ├── dashboards
│   │   └── log_dashboard.json
│   └── provisioning
│       ├── dashboards
│       │   └── dashboards.yml
│       └── datasources
│           └── datasource.yaml
├── log-generator
│   ├── Dockerfile
│   ├── app.log
│   ├── generate_logs.py
│   └── log-generator
│       └── app.log
└── prometheus
    ├── Dockerfile
    ├── log_exporter.py
    └── prometheus.yml
```

#### 🧠 Extend the Lab (TO DO)

- Improve the anomaly detection model.

- Add email/Slack alerting via Grafana.

- Integrate real-time log sources.

- Experiment with different log formats or metrics.



#### **🛠️ Requirements**

- Docker & Docker Compose

- Python 3.8+ (if running components manually)

#### 🤝 Contributions

Feel free to fork, PR, or open issues.
