# System Design Study Guide (v2)

## Table of Contents

- [System Design Study Guide (v2)](#system-design-study-guide-v2)
  - [Reference Architecture: Minimal Cloud Dependencies](#reference-architecture-minimal-cloud-dependencies)
  - [Secrets & Config Management](#secrets--config-management)
  - [Networking Stack](#networking-stack)
  - [Application Layer](#application-layer)
  - [Datastores](#datastores)
  - [Messaging and Queues](#messaging-and-queues)
  - [Observability](#observability)
  - [Protocol Overview](#protocol-overview)
  - [CI/CD Pipeline](#cicd-pipeline)
  - [Edge/IoT Deployment Notes](#edgeiot-deployment-notes)
  - [Capacity Planning](#capacity-planning)
  - [Practice & Study Tools](#practice--study-tools)

---

## Reference Architecture: Minimal Cloud Dependencies

Designed for full application stack deployment without reliance on centralized cloud services.

- Kubernetes for orchestration
- GitHub Actions for CI/CD
- Helm for templated deployments
- NGINX + GeoIP2 for region-based routing
- Redis for caching
- RabbitMQ for job queues
- MongoDB for object/document storage
- MySQL for structured relational data
- Prometheus + Grafana for observability
- Container registry: GitHub Packages (or self-hosted)

## Secrets & Config Management

- **Kubernetes Secrets**: Base64-encoded, useful for small secrets. Not encrypted at rest.
- **Sealed Secrets (Bitnami)**: Encrypt secrets for Git, decrypted by K8s controller at runtime.
- **Environment Files**: Used locally in `.env`, but avoid committing.
- **Manual injection via kubectl**: For one-off or secure deployment workflows.

## Networking Stack

- **NGINX**: Reverse proxy, load balancer, SSL termination, GeoIP-based routing
- **Alpine Linux**: Lightweight base image for containers
- **DNS**: Managed within Kubernetes via CoreDNS or external DNS provider
- **GeoIP2 Routing**:
  - Main app domain routes to regional subdomains (e.g., `us.app.com`, `eu.app.com`)
  - Optionally use CDN (e.g., Cloudflare) for edge presence

## Application Layer

- **Application containers**: Built using Alpine-based images
- **Redis**: Used for fast in-memory caching (e.g., sessions, frequent lookups)
- **MongoDB**: Preferred for JSON-like document storage (schema-flexible)
- **MySQL**: Used where structured, transactional, and relational data is required
- **RabbitMQ**: Asynchronous job queueing, task distribution

## Datastores

- **Redis**: Cache layer, ephemeral memory store
- **MongoDB**: Document storage, sharding for scale, flexible schema
- **MySQL**: Transactions, foreign key constraints, reporting, analytics

## Messaging and Queues

- **RabbitMQ**
  - Used for background jobs, long-running tasks (e.g. PDF generation)
  - Pub/sub and work queues
  - Durable message delivery
- **Kafka** (when used):
  - For high-throughput, persistent event streams
  - Suitable for real-time analytics, multi-stage pipelines

## Observability

- **Prometheus**:
  - Metrics pulled via HTTP
  - Sidecar setup per service container
  - AlertManager for notification hooks
- **Grafana**:
  - Visualize Prometheus data with dashboards
  - Alert rules and historical analysis
- **Log Management**:
  - stdout logs via `kubectl logs`
  - For large setups, ELK stack (Elasticsearch + Logstash + Kibana)

## Protocol Overview

- **HTTP/REST**: Common for frontend/backend, browser-native
- **WebSockets**: Realtime, bidirectional comms (e.g., chats, dashboards)
- **gRPC**: High-performance RPC, schema-based, good for internal services
- **MQTT**: Lightweight pub/sub protocol for IoT (used with ESP32)
- **UDP**: Low-latency, lossy communication (games, VOIP)

## CI/CD Pipeline

- **GitHub Actions**:
  - Linting and test automation
  - Container image builds
  - Kubernetes deploy validation
  - Push updates to the cluster
- **Container Registry**:
  - GitHub Packages
  - Self-hosted options
- **GitHub Alternative**:
  - GitLab CE for self-managed pipelines and registries

## Edge/IoT Deployment Notes

- **ESP32 + Paxcounter**: Captures WiFi/Bluetooth signals for passive presence monitoring
- **LoRa (Long Range Radio)**: Low power, long distance, no IP stack
- **LilyGO Boards**: Integrated ESP32 + LoRa + display, great for field use
- **Meshtastic**:
  - Community mesh firmware over LoRa
  - Works peer-to-peer, offline
- **Data Aggregation**:
  - Gateways receive sensor data
  - Queued for upstream via MQTT or local Kafka

## Capacity Planning

- **Back-of-the-envelope calculation**:
  - Estimate requests/sec, storage, throughput
  - Plan based on peak usage, replication factors
- **Latency references**:
  - https://github.com/sirupsen/napkin-math
  - https://gist.github.com/jboner/2841832
- **Test yourself**:
  - https://computers-are-fast.github.io/

## Practice & Study Tools

- **Design prompts**:
  - Design a privacy-first chat app
  - Build a global sensor network without using AWS
- **Interview-ready questions**:
  - When do I use RabbitMQ vs Kafka?
  - How do I shard MongoDB for regional data?
  - How do I handle secrets in GitOps?
- **Quick access links**:
  - [GeoIP in NGINX](https://www.cleverti.com/blog/how-to-build-a-load-balancer-based-on-user-s-location-with-nginx-and-geoip2/)
  - [Caching with Redis](https://codeforgeek.com/caching-a-mongodb-database-with-redis/)
  - [GitHub Packages](https://github.com/features/packages)
  - [Prometheus Docs](https://prometheus.io/docs/)
  - [Grafana Docs](https://grafana.com/docs/)

---

> Study built from real-world experience and edge-first systems. Focused on what you’ve used, not just what’s trendy.

