# Prompting Guide: Generating Complex Data Infrastructure

To generate a production-ready `docker-compose.yml` for Data Engineering (Spark, Kafka, etc.), follow this 3-step prompting strategy.

---

## Step 1: Define the Architecture (The Skeleton)
**Goal:** Establish the services, networks, and base images.

**Prompt:**
> "I am starting a Data Engineering project. Please generate a `docker-compose.yml` skeleton using the latest official images for:
> 1. A Kafka cluster (Zookeeper and 1 Broker).
> 2. A Spark cluster (1 Master and 2 Workers).
> 3. A shared network named `datamasterylab`.
> 4. Ensure all containers use the same network."

---

## Step 2: Add Logic & Connectivity (The Brain)
**Goal:** Configure environment variables and start-up dependencies.

**Prompt:**
> "Now, update the previous Docker Compose file with the following logic:
> 1. **Networking:** Configure Kafka Listeners so I can access the broker from my local machine (`localhost:9092`) and from within the Docker network (`broker:29092`).
> 2. **Stability:** Add `healthcheck` to Zookeeper and make the Kafka Broker `depend_on` Zookeeper only when it is 'healthy'.
> 3. **Persistence:** Define a volume named `spark-data` for the Spark services."

---

## Step 3: Optimization & DRY Principles (The Polish)
**Goal:** Use YAML Anchors to make the code clean and professional.

**Prompt:**
> "Finally, let's optimize the file for readability:
> 1. **YAML Anchors:** Create an `x-spark-common` anchor for the Spark Workers to avoid repeating environment variables (RAM, Cores, Master URL).
> 2. **Volumes:** Mount a local folder `./jobs` to `/opt/spark/work-dir` for all Spark services.
> 3. **Commands:** Explicitly set the `command` for Spark Master and Workers using `spark-class`."

---

## Key Keywords to Use in Your Prompts
If you want to modify the file further, include these technical terms for better results:

- **"Persistence"**: If you want your data to stay after the container stops.
- **"Port Mapping"**: To specify `host:container` ports.
- **"Environment Variables"**: To configure software settings without changing code.
- **"Resource Limits"**: To restrict RAM or CPU usage per service.

---

## Example of a "One-Shot" Mega Prompt
If you prefer to get it all in one go, use this:
> "Act as a Data Engineer. Generate a `docker-compose.yml` for a Spark and Kafka stack. Use YAML anchors for Spark workers to keep it DRY. Include healthchecks for Zookeeper and Kafka, custom networking for internal/external access, and volume mounting for a `./jobs` directory. Ensure the Spark workers are limited to 2 cores and 2GB of RAM."