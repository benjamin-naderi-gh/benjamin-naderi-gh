<h1 align="center">Benjamin Naderi</h1>

<p align="center">
  <b>Co-founder at GeoBirds</b> — supply chain location intelligence<br>
  I build the data and LLM infrastructure, and run the company around it.
</p>

<p align="center">
  <a href="https://www.geobirds.io"><img src="https://img.shields.io/badge/GeoBirds-0B7285?style=flat-square" alt="GeoBirds"></a>
  <a href="https://amsterdam.pydata.org/"><img src="https://img.shields.io/badge/PyData%20Amsterdam-organising%20committee-3776AB?style=flat-square&logo=python&logoColor=white" alt="PyData Amsterdam"></a>
  <a href="mailto:benjamin@geobirds.io"><img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email"></a>
  <img src="https://img.shields.io/badge/Netherlands-4C566A?style=flat-square" alt="Netherlands">
</p>

---

## 🛰️ What I do

**Build.** I am hands on with the engineering. Data platform, pipelines, and the
LLM infrastructure the product depends on.

**Fund.** Grant and R&D proposals, consortia with research and industry
partners, and everything attached to them: project plans, cooperation
agreements, IP arrangements, financial forecasts.

**Run.** Hiring engineers, and fractional and freelance people where that suits
the stage better. Operating cadence, OKRs and priorities, payroll, bookkeeping,
procurement, cloud budgets, contracts. I automate the parts that repeat.

Before this: entrepreneurship and hardware development, with a background in
manufacturing, on systems at both small and large scale.

## ⚙️ How we build

**Google Cloud Platform is home.** App deployment and the data pipelines behind
it both run there, with Azure alongside where it earns its place.

**Pipelines that refresh surgically.** We pull from a lot of sources, each
arriving in a different shape and form, and reconciling that is most of the
work. So we build them modular — a single source or a single slice can be
refreshed on its own, without tearing down and rerunning everything around it.
That property is worth the time it costs to design in.

**Lego bricks before buildings.** We take our time over the building blocks,
then assemble everything out of them. Slower at the start, considerably faster
afterwards. A lot of my own time goes on Python packaging for exactly that
reason.

**LLM endpoints at scale.** Batch processing, sharding, and prompt versioning,
open-weight models included, with some LLM feature engineering on top.

**Training and fine-tuning.** Fine-tuning models to produce the domain-specific
English text our in-house use cases need, where a general-purpose endpoint is
the wrong tool.

**Prototype to production line.** Nothing is left sitting as an experiment. We
are moving development towards a software factory model and agentic software
engineering.

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

Some hands-on experience with geospatial data and the Google Maps Platform,
which is never far away when the product is built on location.

## 🐍 Community

On the organising committee of **[PyData Amsterdam](https://amsterdam.pydata.org/)**,
supporting the open source community. That means the annual conference and the
monthly meetups we run through the rest of the year, hosted at companies around
the city — programme and speakers, sponsors and partners, and the running of the
events themselves.

## 📦 Projects

**[polars-crs](https://github.com/benjamin-naderi-gh/polars-crs)** — detect which
coordinate reference system a column of unlabelled `x`/`y` numbers is in, by
looking at the values. A Polars expression plugin written in Rust.

```python
import polars as pl
import polars_crs as plc

df = pl.DataFrame({"x": [121000.0, 92000.0], "y": [487000.0, 437000.0]})

df.select(plc.detect("x", "y")).item()
# 'EPSG:28992'   (Dutch RD New)
```

```
pip install polars-crs
```

**Internal tools.** Plenty of what I build is not the product. Bookkeeping runs
as a pipeline, so receipts and invoices are captured, sorted and pushed through
to the ledger rather than retyped. Ingestion pipelines pull in the sources we
depend on. Past that there is a long tail — grant scanning, OKR tracking,
mailbox automation — most of which exist because a manual process annoyed me
twice.

## 🎿 Off the clock

Father of two, and family gets the best hours of my week. Past that it is
friends, long tables, and getting everyone onto a mountain in winter — skiing
together is the trip we plan the rest of the year around.

Running meetups comes from the same instinct. I like a room full of people who
are pleased to see each other.

Homelabs and home automation, less actively than I used to be. Reading about
history and space exploration.

I am quick at diagnosing a problem and getting it fixed, which is what makes
debugging enjoyable. Given more hours in the day, the car would be running
properly and the microwave, thoroughly broken, would have been repaired long
ago.
