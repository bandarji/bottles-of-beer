# 99 Bottles of Beer

Lyrics to the song "99 Bottles of Beer" written in multiple languages. This repository
illustrates differences between computer languages by demonstrating simple
mechanics (variable assignment, looping, etc).

## Languages

Each language resides within a directory based on its name. Within each you'll find
a Dockerfile, useful for testing execution. We use Docker here to virtualize
the build environment, installing nothing on the local machine that can corrupt
operations.

#### Go

The following should work to validate the Go lyrics dump.

```bash
cd Go/
docker build -t go_99bottles .
docker run go_99bottles
docker run go_99bottles test
```

#### Python

The following should work to validate the Python lyrics dump.

```bash
cd Python/
docker build -t py_99bottles .
docker run py_99bottles
docker run py_99bottles test
```

#### Rust

```bash
cd Rust/
docker build -t rust_99bottles .
docker run rust_99bottles
docker run rust_99bottles test
```

#### TCL (F5 Networks iRule)

Create a virtual service. The iRules directory contains two code examples, one
that returns HTML, another that returns plain text.

```bash
tmsh create / ltm virtual vip.99bottles.10000 { \
     destination x.x.x.x:10000 ip-protocol tcp \
     mask 255.255.255.255 rules { irule.99bottles } \
     profiles add { tcp {} http {} } }
```

Use cURL to view the song lyrics.

```bash
curl -x '' -s04 http://x.x.x.x:10000/
```
