def read_sam(file_path):
    reads = []

    sam_fields = ["QNAME", "FLAG", "RNAME", "POS", "MAPQ", "CIGAR", "RNEXT", "PNEXT", "TLEN", "SEQ", "QUAL"]

    try:
        with open(file_path) as fp:
            for line in fp:
                if not line.strip() or line.startswith("@"):
                    continue

                line_cols = line.strip().split('\t')
                read_data = dict(zip(sam_fields, line_cols[:11]))
                
                read_data["FLAG"] = int(read_data["FLAG"])
                read_data["POS"] = int(read_data["POS"])
                read_data["MAPQ"] = int(read_data["MAPQ"])
                read_data["TLEN"] = int(read_data["TLEN"])

                reads.append(read_data)
                
    except FileNotFoundError:
        print("File path does not point to an existing file!")
        exit(1)

    return reads

def parse_reads(reads):
    alignment_stats = {}

    alignment_stats["Total Reads"] = len(reads)
    alignment_stats["Unmapped Read Count"] = sum(read["FLAG"] & 4 != 0 for read in reads)
    alignment_stats["Mapped Read Count"] = sum(read["FLAG"] & 4 == 0 for read in reads)
    alignment_stats["Percentages"] = (alignment_stats["Mapped Read Count"] / alignment_stats["Total Reads"]) * 100

    chromosone_counts = {}

    for read in reads:
        if read["RNAME"] in chromosone_counts:
            chromosone_counts[read["RNAME"]] += 1
        else:
            chromosone_counts[read["RNAME"]] = 1

    alignment_stats["Reference Counts"] = chromosone_counts

    return alignment_stats