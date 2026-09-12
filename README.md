<h1 align="center">Benjamin Naderi</h1>

<p align="center">
  <b>Co-founder at GeoBirds</b> — VC-backed supply chain location intelligence<br>
  I build the data and LLM infrastructure, make sure it ships, and run the
  company around it.
</p>

<p align="center">
  <a href="https://www.geobirds.io"><img src="https://img.shields.io/badge/GeoBirds-0B7285?style=flat-square" alt="GeoBirds"></a>
  <a href="https://www.linkedin.com/in/benjaminnaderi/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn"></a>
  <a href="https://amsterdam.pydata.org/"><img src="https://img.shields.io/badge/PyData%20Amsterdam-organising%20committee-3776AB?style=flat-square&logo=python&logoColor=white" alt="PyData Amsterdam"></a>
  <a href="mailto:benjamin@geobirds.io"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
  <img src="https://img.shields.io/badge/Netherlands-4C566A?style=flat-square" alt="Netherlands">
</p>

---

## 🛰️ What I do

**Build.** The data platform, the pipelines, and the LLM infrastructure the
product runs on. Hands on.

**Ship.** The engineering management half of the job. Features land on time, and
they go out early and rough rather than late and polished, because feedback is
worth more than a clean first release.

**Run.** Hiring, operating cadence, OKRs, and the back office. Earlier career in
entrepreneurship, hardware and manufacturing, on systems small and large.

## ⚙️ How we build

**Pipelines that refresh surgically.** A lot of sources, every one a different
shape, and reconciling them is most of the work. Built modular, so one slice
refreshes without rerunning everything around it.

**Lego bricks before buildings.** The time goes into the building blocks, and
into Python packaging. Slower at the start, much faster afterwards.

**LLMs in production.** Endpoints at scale — batching, sharding, prompt
versioning, open-weight models included — plus feature engineering, and
fine-tuning for in-house use cases where a general endpoint is the wrong tool.

**Prototype to production line.** Nothing is left sitting as an experiment. We
are moving towards a software factory and agentic software engineering.

## 🧰 Toolbox

<p>
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Rust-000000?style=flat-square&logo=rust&logoColor=white" alt="Rust">
  <img src="https://img.shields.io/badge/Polars-CD792C?style=flat-square&logo=polars&logoColor=white" alt="Polars">
  <img src="https://img.shields.io/badge/BigQuery-669DF6?style=flat-square&logo=googlebigquery&logoColor=white" alt="BigQuery">
  <img src="https://img.shields.io/badge/Google%20Cloud-4285F4?style=flat-square&logo=googlecloud&logoColor=white" alt="Google Cloud">
  <img src="https://img.shields.io/badge/Azure-0078D4?style=flat-square&logo=microsoftazure&logoColor=white" alt="Azure">
  <img src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white" alt="Docker">
  <img src="https://img.shields.io/badge/Kubernetes-326CE5?style=flat-square&logo=kubernetes&logoColor=white" alt="Kubernetes">
  <img src="https://img.shields.io/badge/Terraform-7B42BC?style=flat-square&logo=terraform&logoColor=white" alt="Terraform">
  <img src="https://img.shields.io/badge/Google%20Maps%20Platform-34A853?style=flat-square&logo=googlemaps&logoColor=white" alt="Google Maps Platform">
</p>

## 📦 Projects

**[polars-crs](https://github.com/benjamin-naderi-gh/polars-crs)** — detect which
coordinate reference system unlabelled `x`/`y` columns are in, from the values.
A Polars expression plugin in Rust.

```python
df.select(plc.detect("x", "y")).item()
# 'EPSG:28992'   (Dutch RD New)
```

**Internal tools.** We automate the repetitive parts of the business, fairly
relentlessly. Bookkeeping runs as a pipeline, receipts and invoices sorted and
pushed to the ledger rather than retyped. Past that, OKR tracking and mailbox
automation. Each one starts as a command line script and ends as a package, so
it keeps working without anyone tending it.

## 🐍 Community

On the organising committee of
**[PyData Amsterdam](https://amsterdam.pydata.org/)** — the annual conference
and the monthly meetups through the rest of the year. Programme and speakers,
sponsors, and running the events themselves.

## 🎿 Off the clock

Father of two, and family gets the best hours of my week. Past that it is
friends, long tables, and getting everyone onto a mountain in winter. Running
meetups comes from the same instinct: I like a room full of people who are
pleased to see each other. Otherwise, homelabs and reading about history and
space exploration.

Quick at diagnosing a problem and getting it fixed, which is what makes
debugging enjoyable. Given more hours in the day, the car would be running
properly and the microwave, thoroughly broken, would have been repaired long
ago.
