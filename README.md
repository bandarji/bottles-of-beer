# 99 Bottles of Beer

Lyrics to the song "99 Bottles of Beer" written in multiple languages. This repository
illustrates differences between computer languages by demonstrating simple
mechanics (variable assignment, looping, etc).

## Languages

Each language resides within a directory based on its name. Within each you'll find
a Dockerfile, useful for testing execution. We use Docker here to virtualize
the build environment, installing nothing on the local machine that can corrupt
operations.

#### Python

The following should work to validate the Python lyrics dump.

```bash
cd Python/
docker build -t py_99bottles .
docker run py_99bottles
docker run py_99bottles test
```
