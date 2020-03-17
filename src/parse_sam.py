#!/usr/bin/env python3

import pysam


samfile = pysam.AlignmentFile('../data/ex1.bam', 'rb')

count = 0
for align_record in samfile:
    count += 1
    print(align_record)
    if count == 10:
        break

count = 0
for align_record in samfile:
    count += 1
    print(align_record.flag)
    if count == 10:
        break
