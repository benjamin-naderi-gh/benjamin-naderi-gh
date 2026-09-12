## Benjamin Naderi

Co-founder of **GeoBirds**, where we build supply chain location intelligence.
We build most of our own tooling in house, from data engineering through to data
science, and we ship continuously and work to OKRs. I work across both sides of
that, hands on with the engineering and running the company.

Entrepreneurship and hardware development, with a background in manufacturing
where I have worked on systems at both small and large scale.

### The founder job

Fundraising takes up a good share of it. Writing grant and R&D proposals,
putting consortia together with research and industry partners, and working
through everything that comes attached to them: project plans, cooperation
agreements, IP arrangements, financial forecasts.

Team building is the other half. Hiring engineers, bringing in fractional and
freelance people where that suits the stage better, and keeping advisors and
investors close enough to be useful.

The rest is running the company. Operating cadence, OKRs and priorities,
payroll, bookkeeping, procurement, cloud budgets, contracts. I automate the
parts that repeat.

### How we build

Python and BigQuery, with Google Cloud Platform as our main cloud for both app
deployment and the data pipelines behind it. Azure alongside it where it earns
its place.

The pipelines are the hard part. We pull from a lot of sources, each arriving in
a different shape and form, and reconciling that is most of the work. So we
build them modular: a single source or a single slice can be refreshed
surgically, without tearing down and rerunning everything around it. That
property is worth the time it costs to design in.

We take our time over the building blocks. Solid Lego bricks first, then
everything assembled out of them, which is slower at the start and considerably
faster afterwards. A lot of my own time goes on Python packaging for exactly
that reason.

Scaling LLM endpoints is something we have got good at, open-weight models
included: batch processing, sharding, and prompt versioning.

Anything that starts as a prototype gets taken through to a production line
rather than left sitting as an experiment. We are moving development towards a
software factory model and agentic software engineering.

### Tools I build

A fair amount of what I build is not the product. Bookkeeping runs as a
pipeline, so receipts and invoices are captured, sorted and pushed through to
the ledger rather than retyped. Ingestion pipelines pull in the data sources we
depend on. Past that there is a long tail of small internal tools, for grant
scanning, OKR tracking and mailbox automation, most of which exist because some
manual process annoyed me twice.

### Community

Supporting the open source community on the organising committee of
[PyData Amsterdam](https://amsterdam.pydata.org/). That covers the annual
conference and the monthly meetups we run through the rest of the year, hosted
at companies around the city. Programme and speakers, sponsors and partners,
and the running of the events themselves.

### Projects

[**polars-crs**](https://github.com/benjamin-naderi-gh/polars-crs) detects which
coordinate reference system unlabelled x/y columns are in, from the values. A
Polars expression plugin written in Rust.

```
pip install polars-crs
```

### Away from the keyboard

Father of two, and most of my time outside work goes to my family and children.
Time with family and friends is what I protect in the calendar, including
getting out to ski together when the season allows.

Homelabs and home automation, less actively than I used to be. Reading about
history and space exploration.

I am quick at diagnosing a problem and getting it fixed, which is the same
instinct that makes debugging enjoyable. Given more hours in the day, the car
would be running properly and the microwave, which is thoroughly broken, would
have been repaired long ago.
