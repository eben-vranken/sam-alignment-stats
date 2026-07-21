<h1 align="center">🧬 SAM Alignment Stats</h1>

<p align="center">
    A command-line utility to compute basic alignment statistics from a SAM file.
</p>

<p align="center">
    <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="MIT License"></a>
</p>

A modular, zero-dependency Python CLI built to perform basic sequencing alignment QC. It parses a SAM file, classifies each read as mapped or unmapped using its FLAG field, and reports overall mapping rate and per-reference read counts.

## Install

Clone the repository directly:
```bash
git clone https://github.com/eben-vranken/sam-alignment-stats.git
cd sam-alignment-stats
```

## Usage

Pass the path to a SAM file as the only argument.

```bash
python sam-alignment-stats.py data/test_file.sam
```

### Example Output

Given a SAM file with a mix of mapped and unmapped reads across several reference sequences:

```
Total Reads:                   10
Unmapped Read Count:           3
Mapped Read Count:             7
Percentages:                   70.0
Reference Counts:              {'chr1': 3, 'chr2': 2, 'chrX': 2}
```

## Configuration Matrix

| Argument | Option / Choices | Default | Description |
| --- | --- | --- | --- |
| `file` | *File path* | *None* | Path to the SAM file to be parsed. Required, positional. |

## Feature Set

* **SAM Parsing:** Reads a file line by line, skipping header lines (`@`), and splits each alignment line into its 11 mandatory fields.
* **Flag-Based Mapping Classification:** Uses a bitwise check against the FLAG field (bit 4) to determine whether each read is mapped or unmapped.
* **Mapping Rate Calculation:** Computes the percentage of reads that mapped successfully.
* **Per-Reference Read Counts:** Tallies mapped reads by reference sequence (RNAME), excluding unmapped reads from the count.

## Limitations

This parser expects well-formed, tab-delimited SAM alignment lines with at least the 11 mandatory fields. It does not validate CIGAR strings, parse optional tags, or support BAM (binary) input.

## License

MIT